import os

API_ID = API_ID = 26033579

API_HASH = os.environ.get("API_HASH", "33a934bc26568850ed0eb2c829817090")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6847591791:AAHBJeZ_4jDvDHDwllDxs5v0sS2Q5IDiAyw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1739695986))

LOG = -1002089257258

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


