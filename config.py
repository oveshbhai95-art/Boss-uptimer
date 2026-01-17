import os

class Config:
    API_ID = int(os.environ.get("API_ID", "23903140"))
    API_HASH = os.environ.get("API_HASH", "579f1bcf3eac1660d81ef34b09906012")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8592003697:AAEYGaFeYVLofUXegjE5tUwqbstMDM0ACZM")
    MONGO_URL = os.environ.get("MONGO_URL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003166629808"))
