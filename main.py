from scrapers.logger import Logger
from scrapers.insta import InstagramScraper
from database.saver import Saver
import os
from datetime import datetime

if __name__ == '__main__':
  links = {
    "scrape_list": [
      {
        "link": "https://www.instagram.com/nanga_official/",
        "stores": [
          {
            "store_name": "NANGA SHOP HARAJUKU",
            "wls_id": "198"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/reebokjp/",
        "stores": [
          {
            "store_name": "Reebok原宿店（クラシックストア）",
            "wls_id": "176"
          },
          {
            "store_name": "Reebok渋谷店（フィットハブ＆クラシックストア） ",
            "wls_id": "175"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/bluebottlejapan/?hl=ja",
        "stores": [
          {
            "store_name": "HUMAN MADE Cafe by Blue Bottle Coffee",
            "wls_id": "627"
          },
          {
            "store_name": "ブルーボトルコーヒー渋谷カフェ",
            "wls_id": "626"
          },
          {
            "store_name": "ブルーボトルコーヒー広尾カフェ",
            "wls_id": "625"
          },
          {
            "store_name": "ブルーボトルコーヒー恵比寿カフェ ",
            "wls_id": "624"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/lululemonjp/",
        "stores": [
          {
            "store_name": "lululemon Tokyo SIX HARAJUKU TERRACE ",
            "wls_id": "158"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/venex_jp/",
        "stores": [
          {
            "store_name": "ベネクスショップ髙島屋新宿店",
            "wls_id": "200"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/urthcaffe_japan/?hl=ja",
        "stores": [
          {
            "store_name": "Urth Caffe 渋谷スクランブルスクエア店",
            "wls_id": "362"
          },
          {
            "store_name": "Urth Caffe 代官山店",
            "wls_id": "361"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/brownrice_tokyo/",
        "stores": [
          {
            "store_name": "Brown Rice by Neal's Yard Remedies",
            "wls_id": "363"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/biocafe_shibuya_official/",
        "stores": [
          {
            "store_name": "BiOcafe",
            "wls_id": "364"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/rinatokitchen/",
        "stores": [
          {
            "store_name": "rinato kitchen 代官山本店",
            "wls_id": "367"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/ko.so.cafe/",
        "stores": [
          {
            "store_name": "KO-SO CAFE BIORISE",
            "wls_id": "370"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/kitchen_watarigarasu/",
        "stores": [
          {
            "store_name": "キッチン わたりがらす",
            "wls_id": "371"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/jingumaelakanka/",
        "stores": [
          {
            "store_name": "神宮前 らかん・果",
            "wls_id": "374"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/mominokihouse_official/",
        "stores": [
          {
            "store_name": "ＭＯＭＩＮＯＫＩ ＨＯＵＳＥ",
            "wls_id": "375"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/no.501.bottletokyo/",
        "stores": [
          {
            "store_name": "no.501",
            "wls_id": "376"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/fabudine/",
        "stores": [
          {
            "store_name": "お粥 ワイン 蒸し料理 Fabudine. ファビュダイン",
            "wls_id": "377"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/happy_hour2020/",
        "stores": [
          {
            "store_name": "ハッピーアワー",
            "wls_id": "378"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/abio_farms_market/",
        "stores": [
          {
            "store_name": "アビオファームズマーケット",
            "wls_id": "385"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/ficoandpomum/?ref=badge",
        "stores": [
          {
            "store_name": "フィコ&ポムム ジュース 青山店",
            "wls_id": "386"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/terraburgerandbowl/",
        "stores": [
          {
            "store_name": "Terra Burger & Bowl",
            "wls_id": "387"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/greenbrothers025/",
        "stores": [
          {
            "store_name": "GREEN BROTHERS 恵比寿店",
            "wls_id": "388"
          }
        ]
      }
    ]
  }
  
  current_directory = os.path.dirname(os.path.realpath(__file__))
  info_logger = Logger('info', current_directory)
  saver = Saver(current_directory)

  scraper = InstagramScraper(False, info_logger, saver)
  scraper.start(links)

  scraper.close()