import requests
import lxml.html

r = requests.get('https://race.netkeiba.com/?pid=race&id=p201906040601&mode=top')
r.encoding = r.apparent_encoding # HTTPヘッダからエンコーディングを取得出来ない為、推定されるエンコーディングを取得

# fromstring()関数で文字列（str型・bytes型）をパースする。r.contentはbytes型。
root = lxml.html.fromstring(r.content)
table = root.xpath("//div[@class='race_result fc']/table[@class='race_table_01 nk_tb_common']")
tr = table[0].xpath("//tr")
for td in tr:
    str = ""
    for v in td:
        str += v.text_content()
        str += ","
    print(str)

lxml.html.tostring(table[0])
