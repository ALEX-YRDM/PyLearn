"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 下午5:31
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : repos.py
"""
import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept': 'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
response_dict=r.json()
print(response_dict.keys())
