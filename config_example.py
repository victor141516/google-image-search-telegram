import os

BOT_NAME = os.environ.get("BOT_NAME", "")
CSE_KEY = os.environ.get("CSE_KEY", "")
CSE_CX = os.environ.get("CSE_CX", "")
API_TOKEN = os.environ.get("API_TOKEN", "")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")
NGINX_SUBPATH = os.environ.get("NGINX_SUBPATH", "")
BATCH = int(os.environ.get("BATCH", 10))
POLLING = bool(os.environ.get("POLLING", False))
