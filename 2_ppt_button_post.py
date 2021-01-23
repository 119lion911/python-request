#coding=utf-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import requests as rq

##########################################
### stimulate the button click by POST ###
##########################################

Gossip_url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# this page needs cookie, so if no cookie installed, another page shows
gossip_html = rq.get(Gossip_url)
#print(gossip_html.text)

# check if parw is temporary moved(302)
# use Session module store the cookie which we post before
if len(gossip_html.history) == 1 and gossip_html.history[0].status_code == 302:
    rq_s = rq.Session()
    para = {
        "from": "/bbs/Gossiping/index.html",
        "yes": "yes"
    }
    post_request = rq_s.post(gossip_html.url, para)
    gossip_html = rq_s.get(Gossip_url)
    print(gossip_html.text)
