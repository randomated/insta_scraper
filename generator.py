import json

text = """
NANGA SHOP HARAJUKU	198	https://www.instagram.com/nanga_official/
Reebok原宿店（クラシックストア）	176	https://www.instagram.com/reebokjp/
Reebok渋谷店（フィットハブ＆クラシックストア） 	175	https://www.instagram.com/reebokjp/
HUMAN MADE Cafe by Blue Bottle Coffee	627	https://www.instagram.com/bluebottlejapan/?hl=ja
ブルーボトルコーヒー渋谷カフェ	626	https://www.instagram.com/bluebottlejapan/?hl=ja
ブルーボトルコーヒー広尾カフェ	625	https://www.instagram.com/bluebottlejapan/?hl=ja
ブルーボトルコーヒー恵比寿カフェ 	624	https://www.instagram.com/bluebottlejapan/?hl=ja
lululemon Tokyo SIX HARAJUKU TERRACE 	158	https://www.instagram.com/lululemonjp/
ベネクスショップ髙島屋新宿店	200	https://www.instagram.com/venex_jp/
Urth Caffe 渋谷スクランブルスクエア店	362	https://www.instagram.com/urthcaffe_japan/?hl=ja
Urth Caffe 代官山店	361	https://www.instagram.com/urthcaffe_japan/?hl=ja
Brown Rice by Neal's Yard Remedies	363	https://www.instagram.com/brownrice_tokyo/
BiOcafe	364	https://www.instagram.com/biocafe_shibuya_official/
rinato kitchen 代官山本店	367	https://www.instagram.com/rinatokitchen/
KO-SO CAFE BIORISE	370	https://www.instagram.com/ko.so.cafe/
キッチン わたりがらす	371	https://www.instagram.com/kitchen_watarigarasu/
神宮前 らかん・果	374	https://www.instagram.com/jingumaelakanka/
ＭＯＭＩＮＯＫＩ ＨＯＵＳＥ	375	https://www.instagram.com/mominokihouse_official/
no.501	376	https://www.instagram.com/no.501.bottletokyo/
お粥 ワイン 蒸し料理 Fabudine. ファビュダイン	377	https://www.instagram.com/fabudine/
ハッピーアワー	378	https://www.instagram.com/happy_hour2020/
アビオファームズマーケット	385	https://www.instagram.com/abio_farms_market/
フィコ&ポムム ジュース 青山店	386	https://www.instagram.com/ficoandpomum/?ref=badge
Terra Burger & Bowl	387	https://www.instagram.com/terraburgerandbowl/
GREEN BROTHERS 恵比寿店	388	https://www.instagram.com/greenbrothers025/
"""

scrape_list = { "scrape_list": [] }

lines = text.strip().split('\n')
for line in lines:
    data = line.split('\t')

    index = next((index for index, item in enumerate(scrape_list["scrape_list"]) if item["link"] == data[2]), -1)

    if index != -1:
    	scrape_list["scrape_list"][index]["stores"].append({ "store_name": data[0], "wls_id": data[1] })
    else:
    	scrape_list["scrape_list"].append({ "link": data[2], "stores": [ { "store_name": data[0], "wls_id": data[1] } ] })

print(json.dumps(scrape_list, indent=2, ensure_ascii=False))