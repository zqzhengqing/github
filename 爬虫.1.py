import requests
import re
'''
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, timeout = 30, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("出错了")


def getIMAGE(html):
    try:
        plt = re.findall(r'data-original="(,*?)"',html)
        tlt = re.findall(r'alt="(,*?)"',html)
        for a,b in tlt,plt:
            image = requests.get(b).content
            with open('./image/%s'%a,'wb') as file:
                file.write(image)


def main():
    depth = 1
    url = 'https://www.doutula.com/photo/list/?page=1'
    html = getHTMLText(url)
    getIMAGE()


main()




# 正则 data-original="(,*?)"
# alt="(,*?)"
'''
for i in range(16, 17):
    url = 'https://www.doutula.com/photo/list/?page=' + str(i)
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, timeout = 30, headers = kv)
    html = r.text
    plt = re.findall('data-backup="(.*?)"*?!', html)
    tlt = re.findall('alt="(.*?)"', html)
    ilt = []
    print(tlt)
    for i in range(len(plt)):
        p = plt[i]
        t = tlt[i]
        ilt.append([t, p])

        for [a, b] in ilt:
            aca = requests.get(b).content
            c = b[-4:]
            with open('./image/' + a + c, 'wb') as file:
                file.write(aca)
