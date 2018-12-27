import requests
import json
from models import session
import models
id = "449818741"
urlid = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + id
comment_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
music_name_url = "https://music.163.com/song?id="
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'Referer': 'http://music.163.com/',
          "Cookie":"_iuqxldmzr_=32; _ntes_nnid=fa970a3e6429f7a1128f6c59fc6dbce6,1545818838892; _ntes_nuid=fa970a3e6429f7a1128f6c59fc6dbce6; __utmc=94650624; WM_NI=AQ9phYuIqUvp85AXUQ%2FCvxu4ctr0ZcLY%2B2KdUmEF07k3mG1JOMC8Mywp8epPFb8ZorRoqwylJP%2BTMaxMLK9WMzSQxGbzmPR%2Fdpp%2F0IMuJMRNHUwc%2BIwFRj0VRKyGO0%2B%2BNkw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4d13caeecfdd8b76bf5ef8eb7d45f969e9aaeb76bedee9cccbc21aaa9988bbc2af0fea7c3b92a838ff791eb53b797bfb6f57cfceb8fb9d85bed9dba99f840a1acbed1d9699087e5d3ca7097b38ba7b33da9eda3a8b4428d938dd9d073b5b0f886f35c86bef8bbee7a92b1bf98fc688a90e5b5d06bbc9384acbc5d8fa69db2fb4da2a6a3b1d125a8b0c0d0b3438fab86aed1468c8bb984aa43b59a9e8bb35e9295b7a8ce3ce9f5828cf637e2a3; WM_TID=0NWFfPd%2BjlRBABEURAc8Lv2S64ui1Gz5; playerid=21689604; __utma=94650624.709259473.1545818839.1545818839.1545873192.2; __utmz=94650624.1545873192.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __remember_me=true; MUSIC_U=72f4c91e0ab8ecfda87a2b70901378d9e338b367896ff5d684ed54d73262c65007d1acd73dfe625fd1452e28c74353fb77749c2dda21047b; __csrf=fa90670026159953729812e679ccddbc; JSESSIONID-WYYY=vioHGttWfvG8UTqoXOrYDZKakoY%2F2YI0%2FHkKRJMFaqJ%5CiVKIpB1jvh%2FIsyODVE2c%2FVawRQ1cHVwJnb%5C7rMWnRMHCsyFMpTFSb8GQhixPbQxYKPvaq%2BHW1uin%5Cr6mI%2BkGvek20DtkzX8sGnW1R14geGPjmvMyfMorf6hej0UpXi588QS1%3A1545878473103",
          }
'''respon = requests.get(urlid,headers = header)
comment = respon.text
comment_sum = json.loads(comment)["total"]
print("评论数：",comment_sum)'''
def get_commnet_num(id):
    respon = requests.get(comment_url + id, headers=header)
    comment = respon.text
    comment_dict = json.loads(comment)
    print("评论数：", comment_dict["total"],comment_dict)
def get_music_name(id):
    respon = requests.get(music_name_url + id, headers=header)
    html = respon.content.decode("utf-8")
    start = '<script type="application/ld+json">'
    name = html[html.find(start) + len(start) :html.find('</script>')]
    print(dict(eval(name)))
get_music_name(id)