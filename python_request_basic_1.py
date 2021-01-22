#coding=utf-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import requests as rq
from bs4 import BeautifulSoup
import time
import re
import os

cwd = os.getcwd()
record_file = "ppt_title_list.txt"
# to prevent from being treated as DDOS, we need delay between operations
def delay(hr, min, sec):
    time.sleep(hr*3600 + min * 60 + sec)

start_time = time.time() # record time period of web crawling

ppt_url = "https://www.ptt.cc"
techjob_url = "https://www.ptt.cc/bbs/Tech_Job/index.html"
techjob_html = rq.get(techjob_url)
#print(techjob_html.text)
techjob_parse = BeautifulSoup(techjob_html.text, "html.parser")
title_lists = techjob_parse.select("div.title a") # parse tag "a" of div.title
with open(os.path.join(cwd, record_file), "w+", encoding="utf-8") as txt_file:
    txt_file.writelines("PPT Title Crawl\npage the last:\n")
    for title in title_lists:
        txt_file.write("%s %s\n" % (title.text, ppt_url + title["href"]))
        #print(title.text, ppt_url + title["href"])



page_parse = techjob_parse
for page in range(10): # parse 10 previous pages
    delay(0,0,2)
    prev_page = page_parse.select("div.btn-group.btn-group-paging a")
    prev_url = ppt_url + prev_page[1]["href"]
    index = re.search("index[0-9]*", prev_url)
    page_html = rq.get(prev_url)
    page_parse = BeautifulSoup(page_html.text, "html.parser")
    title_lists = page_parse.select("div.title a")
    with open(os.path.join(cwd, record_file), "a+", encoding="utf-8") as txt_file:
        txt_file.write("page index " + index.group(0)[5:9] + ":\n")
        #print("page index", index.group(0)[5:9], ":")
        for title in title_lists:
            txt_file.write("%s %s\n" % (title.text, ppt_url + title["href"]))
            #print(title.text, ppt_url + title["href"])

crawl_period = time.time() - start_time
with open(os.path.join(cwd, record_file), "a+", encoding="utf-8") as txt_file:
    txt_file.write("Crawl Duration: " + str(round(crawl_period, 2)) + "sec")