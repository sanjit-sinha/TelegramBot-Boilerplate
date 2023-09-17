from sys import version_info
from pyrogram import __version__ as __pyro_version__

__major__ = 4
__minor__ = 0
__micro__ = 0


def get_version() -> str:
    return f"{__major__}.{__minor__}.{__micro__}"


__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
__version__ = get_version()
__license__ = ("[MIT](https://github.com/sanjit-sinha/TelegramBot-Boilerplate/blob/main/LICENSE)")
__pyrogram_version__ = __pyro_version__
