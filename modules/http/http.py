#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
提供基础的三个函数，可自行扩展requests库函数
'''
import requests
import random

def post(url, data = None, header = None):
    url = set_url_protocol(url)
    if header == None:
        header = {
            'Content-Type':'application/x-www-form-urlencoded',
            'User-agent': random_ua()
        }
    try:
        response = requests.post(url, data = data, headers = header)
        response.encoding = 'utf-8'
    except Exception as e:
        print("request http exception:"+str(e))
        return False
    response.close()

    return response

def get(url, header = None, timeout = None):
    url = set_url_protocol(url)
    try:
        response = requests.get(url, headers = header, timeout = timeout)
        response.encoding = 'utf-8'
    except Exception as e:
        print("request http exception:"+str(e))
        return False
    response.close()

    return response

def upload(url, data, header = None):
    '''
    文件上传
    data = {'filed': open('/tmp/xx.txt', 'rb')}
    :param url: 
    :param data: 
    :param header: 
    :return: 
    '''
    url = set_url_protocol(url)
    try:
        response = requests.post(url, files = data, headers = header)
        response.encoding = 'utf-8'
    except Exception as e:
        print("request http exception:" + str(e))
        return False
    response.close()

    return response

def set_url_protocol(url):
    if 'http' not in url:
        url = 'http://' + url
    return url

def random_ua():
    '''
    随机User-agent
    :return: 
    '''
    ua_list = [
        'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
        'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
        'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'
    ]
    ua = random.choice(ua_list)
    return ua