import sys
import warnings
import discord
import os
from random import SystemRandom
import asyncio
import csv
import urllib.request
import urllib.parse
from urllib.request import Request
import re
from datetime import datetime
import time as t
from PIL import Image
import requests
import urllib
from math import *
import aiohttp
import socket
from lxml import etree
import logging
import youtube_dl
EMBEDCOLOR=0x36393E
logging.getLogger().setLevel(logging.INFO)
try:
	from Token import TOKEN
except:
	print("TOKEN FILE NOT FOUND")
	try:
		TOKEN=os.environ['TOKEN']
	except:
		print("TOKEN NOT FOUND IN ENVIRONMENT")