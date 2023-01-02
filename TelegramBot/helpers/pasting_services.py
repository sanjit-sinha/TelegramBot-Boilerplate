from bs4 import BeautifulSoup
from telegraph.aio import  Telegraph
import httpx



async def katbin_paste(text: str) -> str:
	"""
	paste the text in katb.in website.
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

	

async def telegraph_paste(content: str) -> str:
	"""
	paste the text in telegra.ph (graph.org) website.
	"""
	
	telegraph = Telegraph(domain="graph.org")
	await telegraph.create_account(short_name='TelegramBot')
	
	html_content = "<p>" + str(content).replace('\n', '<br>') + "</p>"
	
	try:
		response = await telegraph.create_page(title="TelegramBot",  html_content=html_content)
		response = response["url"]
	except:
		response = await katbin_paste(content )
	
	return response
