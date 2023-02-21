from httpx import AsyncClient
from bs4 import BeautifulSoup
from telegraph.aio import Telegraph


async def katbin_paste(text: str) -> str:
    """
    paste the text in katb.in website.
    """

    katbin_url = "https://katb.in"
    client = AsyncClient()
    response = await client.get(katbin_url)
    soup = BeautifulSoup(response.content, "html.parser")
    csrf_token = soup.find("input", {"name": "_csrf_token"}).get("value")
    try:
        paste_post = await client.post(
            katbin_url,
            data={"_csrf_token": csrf_token, "paste[content]": text},
            follow_redirects=False)
        output_url = f"{katbin_url}{paste_post.headers['location']}"
        await client.aclose()
        return output_url
    except:
        return "something went wrong while pasting text in katb.in."


async def telegraph_paste(content: str, title="TelegramBot") -> str:
    """
    paste the text in telegra.ph (graph.org) website (text should follow proper html tags).
    """

    telegraph = Telegraph(domain="graph.org")
    
    await telegraph.create_account(short_name=title)
    html_content = "<pre>" + content.replace("\n", "<br>") + "</pre>"
    try:
        response = await telegraph.create_page(title=title, html_content=html_content)
        response = response["url"]
    except:
        response = await katbin_paste(content)

    try: await telegraph.revoke_access_token()
    except: pass
    return response


async def telegraph_image_paste(filepath: str) -> str:
    """
	paste the image in telegra.ph (graph.org) website. 
	"""
    telegraph = Telegraph(domain="graph.org")
    try:
        image_url = await telegraph.upload_file(filepath)
        return "https://graph.org/" + image_url[0]["src"]
    except Exception as error:
        return "something went wrong while posting image."
	
