from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/c2f247db74e0f00579fc8.mp4")
START_IMG = getenv("START_IMG", "https://graph.org/file/c94cd0c1ddd9f030547e1.mp4")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Mr_nobi_1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+GZVYjz-zrZthNTQ1")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6713421664").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
