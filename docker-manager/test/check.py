import requests
import re
import subprocess
import time
import os

#从环境变量中获取校验服务器地址
CHECK_SERVER = os.environ.get('CHECK_SERVER')
while True:
    
    # 使用Popen创建进程，并与进程进行复杂的交互
    proc = subprocess.Popen('who /var/log/wtmp',
                            stdin=None,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True) 
    outinfo, errinfo = proc.communicate() # 获取输出和错误信息
    m = outinfo.decode('utf-8')
    """
    admin    pts/4        2023-10-18 11:50 (::1)
    admin    pts/2        2023-10-18 14:58 (172.17.0.1)
    admin    pts/2        2023-10-19 02:20 (172.17.0.1)
    """
    pattern = r'\((.*?)\)' # 匹配括号内的内容
    matches = re.findall(pattern, m)
    for t in matches:
        if t != '::1' and t != '127.0.0.1':
            requests.post(f'{CHECK_SERVER}')
    time.sleep(5)