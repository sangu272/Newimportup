# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
# Owner https://t.me/ll_BAD_MUNDA_ll

import logging
from logging.handlers import RotatingFileHandler
from Abg import patch
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pymongo import MongoClient
from pyrogram import Client
from pyrogram.enums import ParseMode

from config import LOG_FILE_NAME
import config
import time

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

# welcome..
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
boot = time.time()
mongodb = MongoCli(config.MONGO_DB_URI)
db = mongodb.Badmusic
mongo = MongoClient(config.MONGO_DB_URI)
OWNER = config.OWNER_ID


logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("ntgcalls").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
