#encoding=utf-8
import requests
import re
from selenium import webdriver
import sys
import time

headers={'Referer':'https://weibo.com/dayudie','Cookie':'login_sid_t=c3615f4809e66bb8b46c5cec518205e1; _s_tentry=passport.weibo.com; Apache=3626317308726.8496.1457352140971; SINAGLOBAL=3626317308726.8496.1457352140971; _ga=GA1.2.394366518.1465382033; TC-Page-G0=b1761408ab251c6e55d3a11f8415fc72; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; YF-Page-G0=5c7144e56a57a456abed1d1511ad79e8; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; ULV=1488611532494:1:1:1:3626317308726.8496.1457352140971:; TC-V5-G0=5fc1edb622413480f88ccd36a41ee587; appkey=; WBtopGlobal_register_version=a05309c5d15974a8; cross_origin_proto=SSL; SSOLoginState=1512960820; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWZO9H.LduBYm_oiiqo_l0f5JpX5KMhUgL.Fo2pShqc1Knce0e2dJLoIceLxKqL1hBL12qLxK-LBKBLBKMLxK-L1hnLBK.LxK-LBKqL1KeLxK-LBK-LBoeLxK-L1KnLBoBLxK.L1hML12eLxKML1-2L1hBLxK-L12qLBKeLxK.LBKqL1K.LxKMLBoeL1Kqt; ALF=1547277993; SCF=AvyQEsY7xmPB3WcIgm9Us9tUwI6D31-5nVq96uqjnxGnndr6-GD4rRDWVid_dioEJUd1ZPkJ8LJQ1rBzidTnUyY.; SUB=_2A253XBN8DeRhGedP71QX-SbKyD-IHXVUKAO0rDV8PUNbmtAKLXHRkW9NX_HOFF4CPXFF2JN-3pE4RWutE57Xlmn8; SUHB=0ElbaReBGmJPDh; wvr=6; UOR=,,login.sina.com.cn; wb_cusLike_1146698633=N','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
while 1==1:
    try:
        t=requests.get('https://weibo.com/dayudie',headers=headers,verify=False).text
        idx=re.findall('<a name=(.*?) ',t,re.S)
        for x in idx:
            print x
            datax={'mid':x}
            html=requests.post('https://weibo.com/aj/mblog/del?ajwvr=6',data=datax,headers=headers,verify=False).text
            print html
            # time.sleep(1) #请适当调整延迟！速度过快可能会导致10054错误！
    except Exception as err:
        print err
