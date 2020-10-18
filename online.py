#!/bin/python3
import requests
import bs4


def Check(_hash_):
    List_val = []
    url1 = [
            'https://md5decrypt.net/Api/api.php?hash='+_hash_+'&hash_type=md5&email=deanna_abshire@proxymail.eu&code=1152464b80a61728',
            'https://md5decrypt.net/Api/api.php?hash='+_hash_+'&hash_type=sha1&email=deanna_abshire@proxymail.eu&code=1152464b80a61728'
            ]

    url2 =[
            'https://md5.gromweb.com/?hash='+_hash_,
            'https://sha1.gromweb.com/?md5='+_hash_
            ]

    if len(_hash_) == 32:
        Index = 0
    elif len(_hash_) == 40:
        Index = 1
    else:
        Index = 2

    if Index != 2:
        try:
            req = requests.get(url1[Index])
            List_val.append(req.text)
            req.close()
            req = requests.get(url2[Index])
            soup = bs4.BeautifulSoup(req.text, 'lxml')
            List_val+=soup.text.strip().split("\n")
            req.close()
        except:
            pass
    return(List_val)

