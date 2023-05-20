from main_2 import main_2_parse
from main import main_parse
from aiogram.types import InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types, executor
from config import *
import logging

api = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot)