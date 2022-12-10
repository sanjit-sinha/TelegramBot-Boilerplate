from bs4 import BeautifulSoup
import httpx


async def katbin_paste(text: str) -> str:
	"""
	paste the text to katb.in website.
	"""
	
	katbin_url = "https://katb.in"
	client = httpx.AsyncClient()
	response = await client.get(katbin_url)
	
	soup = BeautifulSoup(response.content, "html.parser")
	csrf_token = soup.find('input', {"name":"_csrf_token"}).get("value")
	
	try:
		paste_post = await client.post(katbin_url, data={"_csrf_token":csrf_token, "paste[content]":text}, follow_redirects=False)
		output_url = f"{katbin_url}{paste_post.headers['location']}"
		await client.aclose()
		return output_url
	
	except: return "something went wrong while pasting text in katb.in."
	
