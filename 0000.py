import re
import requests
import csv
import time

f = open("score_all.csv", mode='w+', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["姓名",
                     "学号",
                     "附加分"])
lis = list()
for i in lis:

    url = ""

    payload = 'stuId=' + str(i) + '&password=' + str(i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/51.0.2704.103 Safari/537.36",
               'Content-Type': 'application/x-www-form-urlencoded',
               }
    response = requests.request("POST", url, headers=headers, data=payload)
    if re.findall("登录失败：用户名或密码错误", response.text):
        print("错误！" + str(i) + "号学生写入失败！")
        time.sleep(0.05)
    else:
        res1 = re.findall("<label>(.*?)</label>", response.text)
        res2 = re.findall("青(.*?)</label>", response.text)
        name = re.findall("(.*?)同学", res1[0])
        aggregation = re.findall("总积分为：(.*?)分", res1[0])
        stuId = [str(i)]
        subunit = re.findall("平台:(.*?)分", res2[0])
        csv_writer.writerow(name + stuId + aggregation + subunit)
        print(str(i) + "号学生数据写入完成")

f.close()
