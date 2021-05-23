#encoding: utf-8
import requests
from bs4 import BeautifulSoup

def get_web_value(value):
    r = requests.get(value)
    if r.status_code == 200:
        return r.text
    else:
        return None


def get_zsh_web():
    url = "https://ohmyz.sh/"
    ret = get_web_value(url)
    if ret is None:
        print ("get zsh web failed")
    else:
        return ret

def save_db (result):
    # do some thing
    pass

def save_result_to_db(results):
    for result in results:
        save_db(result)


zsh_text = get_zsh_web()
soup = BeautifulSoup(zsh_text, "html.parser")
mydivs = soup.find_all("div", {"class": "row justify-content-center no-gutters"})

element_cnt = 0
elements = []
if isinstance(mydivs, list) and len(mydivs) > 0:
    target_div = mydivs[0]
    for each_div in target_div:
        if isinstance(each_div, str):
            continue
        else:
            element_cnt += 1
            elements.append("%s\t%s\n" % (each_div.img['alt'], each_div.a['href']))
    print ("Total elements num is %s" % element_cnt)

else:
    print ("error, instance")

with open ("zsh sponsor list.txt", "w") as f:
    for el in elements:
        f.write(el)

save_result_to_db(elements)