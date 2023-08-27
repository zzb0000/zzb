import requests
from lxml import etree
import shuju
url = "https://101.qq.com/#/hero"
# headers = {
# 'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
# 'Cookie':
# 'pac_uid=0_6cf60b3cc4084; iip=0; pgv_pvid=8483537460; RK=d8ccgzhJRL; ptcz=4f5ee1fae81934ffe04124bf214b20c98044e905a2c398b04bc6e3db19035075; qq_domain_video_guid_verify=26ad4f1b41307558; eas_sid=41c6U9a2L903N3W5g7W0X3h5u7; pgv_info=ssid=s6872272680; lolqqcomrouteLine=index-tool_main; eas_entry=https%3A%2F%2Flol.qq.com%2F; isHostDate=19594; PTTuserFirstTime=1692921600000; isOsSysDate=19594; PTTosSysFirstTime=1692921600000; isOsDate=19594; PTTosFirstTime=1692921600000; ts_refer=lol.qq.com/; ts_uid=7376201596; weekloop=0-0-0-34; ts_last=101.qq.com/; 101qqcomrouteLine=main_main_main_main_main'
# }
r = shuju.r

html = etree.HTML(r)

urls = html.xpath('//li/div/p/text()')
#print(urls)
