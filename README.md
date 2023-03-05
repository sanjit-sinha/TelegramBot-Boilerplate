<div align="center">
<h1>Telegram Bot Boilerplate<br>[ Pyrogam version ]</h1>
<img src="https://telegra.ph/file/4621c1419e443ebb01b2b.jpg" align="center" style="width: 100%" />
</div>

------

<div align="center">
<h1><b>About this repository?</b></h1>
</div>

This repository serves as a template for creating a new Telegram bot using Python. It aims to save time for those starting new projects from scratch, and provides a helpful resource for those who are new to the Telegram API and want to learn and understand basic file structure. The repository includes a Pluggable boilerplate that is easy to use and customize for your own project. You can use the repository as a template or fork it to begin a new project. The following are some of the features of this repository:

- Fully asynchronous code: The code in this repository makes use of libraries such as httpx, aiofiles, pyrogram and mongodb motor to enable fully asynchronous execution. This means that the code can perform multiple tasks concurrently, improving the performance and efficiency of the bot.

- Pre-built features: This repository contains a range of pre-built plugins, functions, and decorators to assist you in getting started. Some examples include commands for broadcasting, pasting, checking spam counter, evaluating/executing code, checking database and server stats, and more..

- Pluggable plugins: The code in this repository is designed to be modular and extensible, allowing you to easily add new functionality to the bot by creating and integrating plugins.

- Ratelimiting: To prevent FloodWait errors, the code in this repository includes ratelimiting functionality that uses the leaky bucket algorithm and the pyrate_limiter library to limit the number of requests that can be made by users in a given time period.

- MongoDB support: The code in this repository includes support for storing data in a MongoDB database, allowing you to easily keep track of users and channels associated with the bot."


_____

<div align="center">
<h1><b>More information and links</b></h1>
</div>
<img src="https://telegra.ph/file/db914ce03059dca6e2e02.gif" align="right" width="150">

<p>
<b>This bot uses the Pyrogram framework, which is based on the MTProto protocol, to communicate with the Telegram API. .</b>
<br>
<br>
Pyrogram is a modern, elegant , much faster and asynchronous MTProto API<a href="https://docs.pyrogram.org/topics/mtproto-vs-botapi"> (MTproto vs botapi)</a> framework.
<br>
<br>
<a href="https://docs.pyrogram.org/"><strong>Pyrogram Documentation</strong></a> | <a href="https://t.me/pyrogramchat"><strong>Pyrogram Support Group</strong></a> | <a href="https://core.telegram.org/api"><strong>Telegram API Documentation</strong></a>
<br>
<br> Some other libraries and Framework: <a href="https://github.com/python-telegram-bot/python-telegram-bot"><strong>Python Telegram Bot</strong></a> | <a href="https://github.com/LonamiWebs/Telethon"><strong>Telethon</strong></a> | <a href="https://core.telegram.org/bots/samples"><strong>List of libraries and frameworks using various type of languages.</strong></a>
<br>
<br>
Join <a href="https://t.me/ani_support"><strong>Discussion Group</strong><a> if you have any suggestion or bugs to discuss.
<p>
  
---------

<div align="center"> 
<h1><b>Screenshots</b></h1>
</div>

| ![](https://te.legra.ph/file/565b3f47e0886fc93e75c.jpg) | ![](https://te.legra.ph/file/e6e16e6f3a1d07524a23b.jpg)|
|--------------------------------------------------------|--------------------------------------------------------|
| ![](https://te.legra.ph/file/29f7e8163406f63bfb4f8.jpg) | ![](https://te.legra.ph/file/c26991c1eaae34920216c.jpg) |

_______

<div align="center"> 
<h1><b>Bot Deployment and Usage</b></h1>
<p><b>( VPS or Local hosting )</b></p>
</div>

( checkout no database branch if you don't want to use database in your bot. )
  
Upgrading, Updating and setting up required packages in Server.

```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install python3-pip -y
sudo pip3 install -U pip
```

Cloning Github Repository and Starting the Bot in Server.
 
```
git clone https://github.com/sanjit-sinha/Telegram-Bot-Boilerplate && cd Telegram-Bot-Boilerplate 
pip3 install -U -r requirements.txt
```


Now edit the config vars by typing `nano config.env` and save it by pressing <kbd>ctrl</kbd>+<kbd>o</kbd> and <kbd>ctrl</kbd>+<kbd>x</kbd>.
<br>
<br>
<details open="open">
<summary><strong> Setting up config variables files (config.env) </strong></summary>
<br>
<ul>
 <li>Get your API_ID and API_HASH from <a href="https://my.telegram.org/auth">Telegram.org</a>, BOT_TOKEN from <a href="https://t.me/botfather">Botfather.</a> You can get user ids for sudo users and owner from <a href="https://t.me/MissRose_bot">MissRoseBot</a> by just using /info command and copying ID value from result. </li>
  <li>To get guide for getting MONGO_URI click <a href="https://graph.org/How-to-create-mongodb-URI-01-01">here</a></li>
  </ul>
</details>
  
now you can start the bot by simply typing `bash start` or `python3 -m TelegramBot`

<img src="https://telegra.ph/file/03a650af46de1bcc27756.png" align="right" width="150">

The bot will stop working once you logout from the server. You can run the bot 24*7 in the server by using screen or tmux.
```
sudo apt install tmux -y
tmux && bash start
```
  
Now the bot will run 24*7 even if you logout from the server. [Click here to know about tmux and screen advance commands.](https://grizzled-cobalt-5da.notion.site/Terminal-Multiplexers-to-run-your-command-24-7-3b2f3fd15922411dbb9a46986bd0e116)


<details open="open">
<summary><strong>Basic Bot Commands and it's usage</strong></summary>
<ul>
<br>
	<li>
	<i><b>Users Commands</b></i><br><br>
	/start - To get the start message.<br>
	/help - Alias command for start. <br>
	/ping - Ping the telegram api server<br>
	/paste - Paste the text in katb.in
	</li>
<br>
	<li>
	<i><b>Sudo User Commands </b></i><br><br>
	/speedtest - Check the internet speed of bot server.<br>
	/serverstats - Get the stats of bot server.<br>
	/stats - Alias command for serverstats.<br>
	/dbstats - Get the stats of bot database. 
	</li>
<br>
	<li>
	<i><b>Developer Commands </b></i><br><br> 
	/shell - To run the terminal commands via bot.<br>
	/py - To run the python commands via bot. <br>
	/update - To update the bot to latest commit from repository. <br> 
	/restart - Restart the bot. <br>
	/log - To get the log file of bot. <br>
	/broadcast - broadcast the message to bot users and chat. 
</ul>
</details>
<br> 
	

-------
  
<div align="center">
<h1><img src="https://telegra.ph/file/c182d98c9d2bc0295bc86.png" width="45"><b>  
DirectoryLayout <b></h1>
</div>


```

├── Dockerfile                          
├── LICENSE
├── README.md
├── config.env                         ( For storing all the  environment variables)
├── requirements.txt                   ( For keeping all the library name wich project is using)
├── TelegramBot
│   │
│   ├── __init__.py                   ( Initializing the bot from here.)
│   ├── __main__.py                   ( Starting the bot from here.)
│   ├── config.py                     ( Importing and storing all envireonment variables from config.env)
│   ├── logging.py                    ( Help in logging and get log file)
│   │
│   ├── assets                        ( An assets folder to keep all type of assets like thumbnail, font, constants, etc.)
│   │   └── __init__.py
│   │   ├── font.ttf
│   │   └── template.png
│   │
│   ├── database                      (Sperate folder to manage database related stuff for bigger projects.)
│   │   ├── __init__.py
│   │   ├── database.py              (contain functions related to handle database operations all over the bor)
│   │   └── MongoDb.py               (Contain a MongoDB class to handle CRUD operations on MongoDB collection )
│   │  
│   ├── helpers                       ( Contain all the file wich is imported and  used all over the code. It act as backbone of code.)
│   │   ├── __init__.py
│   │   ├── filters.py 
│   │   ├── decorators.py            ( Contain all the python decorators)
│   │   ├── ratelimiter.py           (Contain RateLimiter class that handle ratelimiting part of the bot.)
│   │   └── functions.py             ( Contain all the functions wich is used all over the code. )
│   │
│   ├── plugins                       ( plugins folder contain all the plugins commands via wich user interact)  
│   │   ├── __init__.py 
│   │   ├── developer
│   │   │   ├── __init__.py
│   │   │   ├── terminal.py
│   │   │   └── updater.py
│   │   │
│   │   ├── sudo
│   │   │   ├── __init__.py
│   │   │   ├── speedtest.py
│   │   │   ├── dbstats.py
│   │   │   └── serverstats.py
│   │   │   
│   │   └── users
│   │       ├── __init__.py
│   │       ├── alive.py
│   │       └── start.py
│   │      
│   └── version.py         
└── start                             ( A start file containing bash script to start the bot using bash start)

```    
  
<details>
   <summary>Some important articles and Links wich will help you to understand the code better.</summary>
   <ul>
    <br>
    <li> <a href="https://stackoverflow.com/questions/448271/what-is-init-py-for#:~:text=The%20__init__.py%20file%20makes%20Python,directories%20containing%20it%20as%20modules">What is __init__.py</a>│ <a href="https://youtu.be/cONc0NcKE7s">( YouTube video )</a</li>         
    <li> <a href="https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/">What is __name__ = "__main__" in python?</a></li>
    <li><a href="https://realpython.com/python-logging/
">About python logging</a></li>
    <li><a href="https://www.educative.io/blog/python-concurrency-making-sense-of-asyncio">Python concurrecny and asyncio<a></li>
    <li><a href="https://developer.vonage.com/blog/21/10/01/python-environment-variables-a-primer">What is Environment Variables (.env files) ?<a></li>  
    <li><a href="https://www.programiz.com/python-programming/decorator
">About Python decorator</a></li>
    <li> <a href="https://stackoverflow.com/questions/4042905/what-is-main-py">What is __main__.py</a> </li> 
       <li><a href="https://learnpython.com/blog/python-requirements-file">What is requirements.txt and why should we use it?</a></li>
     <li> <a href="https://geekflare.com/dockerfile-tutorial/">What iS Dockerfile?</a> </li>
     <li> <a href="https://developerexperience.io/practices/license-in-repository">what is License in a repository?</a> │<a href="https://choosealicense.com/">choosealicense.</a></li> 
     <li><a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes">What is README.md?</a> │ <a href="https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">( writing format for Github readme ) </a>│ <a href="https://readme.so ">( website wich will help you in writing readme ) </a>│website to get png images wich  can be used in making readme:- <a href="https://shields.io/">shields.io│</a> <a href="https://www.flaticon.com/">flaticon.com</a></li>
     
   </ul>
</details>


-------
  
<div align="center">
<h1><b>Basic structure for building your own plugin.</b></h1>
</div>


```py
from TelegramBot.helpers.decorators import ratelimiter
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["hello", "hi"]))
@ratelimiter
async def hello(client: Client, message: Message):
    """
    simple plugin to demonstrate in readme.
    """   	
    return await message.reply_text("world")	    
```
	    
_____
  
<div align="center">
<h1><b>Credits and Contibution</b></h1>
</div>
  
<img src="https://telegra.ph/file/b26313d73e4d05de84a85.png" align="right" width="150">
<p>
Codes and structure of this bot is heavily inspired by open source projects like <a href="https://github.com/TeamYukki/YukkiMusicBot"><strong>YukkiMusicbot</strong></a> | <a href="https://github.com/UsergeTeam/Userge"><strong>Userge</strong></a> | <a href="https://github.com/EverythingSuckz/TG-FileStreamBot"><strong>TG-FileStreamBot etc.</strong></a>.
<br>
<br>
 Special Thanks to <br>
• <a href="https://github.com/delivrance"><strong>Dan</strong></a> for creating <a href="https://github.com/pyrogram/pyrogram"><strong>Pyrogram.</strong></a><br>
• <a href="https://github.com/starry69"> Starry</a> for guiding and acutebot repository. <br>
• <a href="https://github.com/annihilatorrrr">Annihilator</a> for helping me out with pyrogram stuff.

<br>
<br>
Any type of suggestions, pointing out bug or contribution is highly appreciated. :)
</p>
 
  
-------
  
<div align="center">
<h1><b>Copyright and License</b></h1>
</div>
<br>
<img src="https://telegra.ph/file/b5850b957f081cfe5f0a6.png" align="right" width="110">
  

* copyright (C) 2023 by [Sanjit sinha](https://github.com/sanjit-sinha)
* Licensed under the terms of the [The MIT License](https://github.com/sanjit-sinha/Telegram-Bot-Boilerplate/blob/main/LICENSE)

<div align="center">
<img src="https://img.shields.io/badge/License-MIT-green.svg" align="center">
</div>

-------
