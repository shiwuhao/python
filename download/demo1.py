# /usr/bin/env python3

import os
import requests

"""
下载M3U8文件里的所有片段
"""


def download(url):
    download_path = '/Users/shiwuhao/Downloads/aa'

    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    print(file_line)
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
        unknow = True  # 用来判断是否找到了下载的地址
        for index, line in enumerate(file_line):
            if "EXT-X-STREAM-INF" in line:
                unknow = False
                # 拼出ts片段的URL
                pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]
                res = requests.get(pd_url)
                # c_fule_name = str(file_line[index + 1])
                c_fule_name = 'index.m3u8'
                with open(download_path + "/" + c_fule_name, 'ab') as f:
                    f.write(res.content)
                    f.flush()
        if unknow:
            raise BaseException("未找到对应的下载链接")
        else:
            print(u"下载完成")


download("https://dadi-yun.com/20190305/1826_4d2ec220/index.m3u8")
