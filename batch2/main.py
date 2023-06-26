from scrapers.logger import Logger
# from scrapers.insta import InstagramScraper
from scrapers.new_insta import InstagramScraper
from database.saver import Saver
import os
from datetime import datetime
import time


if __name__ == '__main__':
  links = {
    "scrape_list": [
      {
        "link": "https://www.instagram.com/cityshop_food/",
        "stores": [
          {
            "store_name": "CITYSHOP 渋谷キャスト店",
            "wls_id": "440"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/soba.tamawarai/",
        "stores": [
          {
            "store_name": "半笑 HANWARAI",
            "wls_id": "477"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/suranje_com/",
        "stores": [
          {
            "store_name": "韓国料理スランジェ 新宿店",
            "wls_id": "472"
          },
          {
            "store_name": "韓国料理スランジェ 渋谷ヒカリエ店",
            "wls_id": "471"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/indian_restaurant_nataraj/",
        "stores": [
          {
            "store_name": "ミラン・ナタラジ渋谷店",
            "wls_id": "418"
          },
          {
            "store_name": "ナタラジ原宿表参道店",
            "wls_id": "417"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/vegan_izakaya_masaka/",
        "stores": [
          {
            "store_name": "ヴィーガン 居酒屋 真さか",
            "wls_id": "420"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/vegeater_official/",
        "stores": [
          {
            "store_name": "Vegeater ",
            "wls_id": "423"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/skyhighjuice/",
        "stores": [
          {
            "store_name": "Sky High DAIKANYAMA",
            "wls_id": "425"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/official.wearethefarm/",
        "stores": [
          {
            "store_name": "WE ARE THE FARM EBISU",
            "wls_id": "429"
          },
          {
            "store_name": "WE ARE THE FARM SHIBUYA",
            "wls_id": "430"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/pain_au_sourire/",
        "stores": [
          {
            "store_name": "Pain au Sourireパン・オ・スリール",
            "wls_id": "432"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/alohatable_daikanyama/",
        "stores": [
          {
            "store_name": "ALOHA TABLE 代官山",
            "wls_id": "433"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/heavenly_jp/",
        "stores": [
          {
            "store_name": "HEAVENLY Island Lifestyle 代官山",
            "wls_id": "434"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/yasaiyamei_/",
        "stores": [
          {
            "store_name": "やさい家めい 渋谷ヒカリエ店",
            "wls_id": "445"
          },
          {
            "store_name": "やさい家めい 表参道ヒルズ本家",
            "wls_id": "444"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/kyoto.hyoto.shibuya/",
        "stores": [
          {
            "store_name": "京都 瓢斗 渋谷店",
            "wls_id": "447"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/davidottojuice/",
        "stores": [
          {
            "store_name": "デービッド オットー ジュース東京店",
            "wls_id": "448"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/sunshinejuicetokyo/",
        "stores": [
          {
            "store_name": "SUNSHINE JUICE TOKYO",
            "wls_id": "450"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/cleansingcafe/",
        "stores": [
          {
            "store_name": "CLEANSING CAFE Daikanyama",
            "wls_id": "451"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/shoryuhinabe/?hl=ja",
        "stores": [
          {
            "store_name": "火鍋酒家 笑龍 | 恵比寿 | 一軒家",
            "wls_id": "473"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/yakuzen_soup/?hl=ja",
        "stores": [
          {
            "store_name": "薬膳湯研究所 薬膳スープらぼ",
            "wls_id": "474"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/n9y_okushibu/",
        "stores": [
          {
            "store_name": "N9Y 奥渋店 羊とチーズとワイン酒場",
            "wls_id": "475"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/teracafe_daikanyama/",
        "stores": [
          {
            "store_name": "寺カフェ代官山",
            "wls_id": "476"
          }
        ]
      },
    ]
  }
  
  current_directory = os.path.dirname(os.path.realpath(__file__))
  info_logger = Logger('info', current_directory)
  saver = Saver(current_directory)

  scraper = InstagramScraper(False, info_logger, saver)
  scraper.start(links)

  scraper.close()
