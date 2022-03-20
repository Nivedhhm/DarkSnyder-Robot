import re
from os import environ
from translation import DarkSnyder
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "off"]:
        return False
    else:
        return default

# ==================================
API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
B_KEYS = environ["BOT_TOKEN"]
START_MSG = environ.get("START_MSG", DarkSnyder.DEFAULT_MSG)
BOT_PICS = (environ.get('PICS', 'https://telegra.ph/file/8d4e4693a8a907cb51797.jpg')).split()
SUPPORT = environ.get("SUPPORT", "t.me/")
SPELL_MODE = is_enabled((environ.get('SPELL_MODE', "on")), True)
SET_SPEL_M = environ.get("SPELL_MODE_TEXT", DarkSnyder.SPELL_CHECK)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", None))
DATABASE_URI = environ.get("DATABASE_URI", None)
FORCE = environ.get('FORCES_SUB')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", DarkSnyder.FILE_CAPTIONS)

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]


# ==================================
# Others

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))

SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')

P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)

IMDB = is_enabled((environ.get('IMDB', "True")), True)

SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)

BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)

SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)

MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)

PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)

PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)


# ==================================
# About Bot 🤖
class bot_info(object):
    BOT_NAME = None
    BOT_USERNAME = None
    BOT_ID = None
