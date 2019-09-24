import requests
import lxml.html
import pandas as pd

r = requests.get('https://race.netkeiba.com/?pid=race&id=p201906040601&mode=top')
r.encoding = r.apparent_encoding # HTTPヘッダからエンコーディングを取得出来ない為、推定されるエンコーディングを取得

# fromstring()関数で文字列（str型・bytes型）をパースする。r.contentはbytes型。
root = lxml.html.fromstring(r.content)



tr = root.xpath("//div[@class='race_result fc']/table[@class='race_table_01 nk_tb_common']/tr")

#print(tr[0].text_content())
#lxml.html.tostring(table[0])
print("1. 着順")
with open('test2.txt', 'w') as f:
    for td in tr[1:-1]:
        str = ""
        for v in td:
            str += v.text_content().replace('\n','').replace('\r','')
            str += ","
        f.write(str + "\r\n")

tr = root.xpath("//table[@class='pay_table_01']/tr")

print("2. 払い戻し")
for td in tr:
    str = ""
    for v in td:
        str += v.text_content()
        str += ","
    print(str)
