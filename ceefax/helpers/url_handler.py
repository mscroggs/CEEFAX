import json


def load_json(url):
    feed = load(url)
    return json.loads(feed)


def load_csv(url):
    feed = load(url)
    return [i.split(",") for i in feed.split("\n")]


def load(url):
    import urllib.request
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/50.0.2661.102 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    out = response.read()
    try:
        return out.decode(response.info().get_content_charset('utf-8'))
    except:
        return out
