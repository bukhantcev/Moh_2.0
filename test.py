import os

from django.test import TestCase

BOT_TOKEN = os.getenv("BOT_TOKEN")
print(BOT_TOKEN)