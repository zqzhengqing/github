import requests
import re


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("出错了")


def getNAME(ilt, html):
    try:
        plt = re.findall('data-original="(.*?)"*?!', html)
        tlt = re.findall('alt="(.*?)"', html)
        for i in range(len(plt)):
            p = plt[i]
            t = tlt[i]
            ilt.append([t, p])
    except:
        print("出错了1")


def getIMAGE(ilt):
    for [a, b] in ilt:
        try:
            aca = requests.get(b).content
            c = b[-4:]
            with open('./image/' + a + c, 'wb') as file:
                file.write(aca)
        except:
            continue
            print("出错了2")


def main():
    # depth = 20
    INFO = []
    start_url = 'https://www.doutula.com/photo/list/?page='
    for i in range(16, 17):
        try:
            url = start_url + str(i)
            html = getHTMLText(url)
            getNAME(INFO, html)
        except:
            print("出错了3")
    getIMAGE(INFO)


main()

# 正则 data-original="(,*?)"
# alt="(,*?)"
