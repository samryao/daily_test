import re
import os
import time
import json
import random
import requests
from utils import *
from DecryptLogin import login

'''QQ个人专属报告类'''
class QQReports():
    def __init__(self, dirpath='qqdata', **kwargs):
        lg = login.Login()
        # QQ空间
        infos_return, self.session_zone = lg.QQZone('mobile')
        self.username = infos_return.get('username')
        self.session_zone_all_cookies = requests.utils.dict_from_cookiejar(self.session_zone.cookies)
        # QQ安全中心
        _, self.session_id = lg.QQId('mobile')
        self.session_id_all_cookies = requests.utils.dict_from_cookiejar(self.session_id.cookies)
        # QQ群
        _, self.session_qun = lg.QQQun('mobile')
        self.session_qun_all_cookies = requests.utils.dict_from_cookiejar(self.session_qun.cookies)
        # 数据保存的文件夹(方便后续的可视化操作)
        self.dirpath = dirpath
    '''获取登录账户的个人资料'''
    def getPersonalInfo(self, filename='personal_info.pkl'):
        personal_info = dict()
        summary_url = 'https://id.qq.com/cgi-bin/summary?'
        userinfo_url = 'https://id.qq.com/cgi-bin/userinfo?'
        bkn = self.__skey2bkn(self.session_id_all_cookies['skey'])
        params = {
            'r': str(random.random()),
            'ldw': str(bkn)
                }
        headers = {
        'referer': 'https://id.qq.com/myself/myself.html?ver=10049&',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            }
        res = self.session_id.get(summary_url, headers=headers, params=params, verify=False)
        res.encoding = 'utf-8'
        personal_info.update(res.json())
        params = {
            'r':str(random.random()),
            'ldw': str(bkn)
            }
        headers = {
            'referer': 'https://id.qq.com/myself/myself.html?ver=10045&',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        while True:
            res = self.session_id.get(userinfo_url, headers=headers, params=params, verify=False)
            res.encoding = 'utf-8'
            if res.text:
                break
        personal_info.update(res.json())
        personal_info_parsed = {
            '昵称': personal_info['nick'],
            '出生日期': '-'.join([str(personal_info['bir_y']), str(personal_info['bir_m']).zfill(2), str(personal_info['bir_d']).zfill(2)]),
            '年龄': personal_info['age'],
            'Q龄': personal_info['qq_age'],
            '账号等级': personal_info['level'],
            '等级排名': personal_info['level_rank'],
            '好友数量': personal_info['friend_count'],
            '单向好友数量': personal_info['odd_count'],
            '已备注好友数量': personal_info['remark_count'],
            '好友分组数量': personal_info['group_count'],
            '最近联系人数量': personal_info['chat_count'],
            '工作': personal_info['work'],
            '个性签名': personal_info['ln']
            }
        saveData2Pkl(personal_info_parsed, os.path.join(self.dirpath, filename))
        return personal_info_parsed 
