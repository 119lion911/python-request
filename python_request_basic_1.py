
#coding=utf-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import requests as rq
from bs4 import BeautifulSoup
import time

# to prevent from being treated as DDOS, we need delay between operations
def delay(hr, min, sec):
    time.sleep(hr*3600 + min * 60 + sec)

start_time = time.time() # record time period of web crawling

techjob_url = "https://www.ptt.cc/bbs/Tech_Job/index.html"
techjob_html = rq.get(techjob_url)
#print(techjob_html.text)
techjob_parse = BeautifulSoup(techjob_html.text, "html.parser")
title_lists = techjob_parse.select("div.title a")
for title in title_lists:
    print(title.text, "https://www.ptt.cc" + title["href"])