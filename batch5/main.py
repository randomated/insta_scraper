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
        "link": "https://www.instagram.com/hario_lwf/",
        "stores": [
          {
            "store_name": "HARIO Lampwork Factory 渋谷店",
            "wls_id": "404"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/lloydsantiques/",
        "stores": [
          {
            "store_name": "ロイズ・アンティークス 青山",
            "wls_id": "408"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/magis_japan/",
        "stores": [
          {
            "store_name": "MAGIS TOIKYO ショールーム",
            "wls_id": "409"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/tomdixonjapan/?hl=ja",
        "stores": [
          {
            "store_name": "TOM DIXON SHOP",
            "wls_id": "411"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/uchinorelax/",
        "stores": [
          {
            "store_name": "UCHINO Relax 渋谷スクランブルスクエア店",
            "wls_id": "412"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/goldsgym.sasazukatokyo/?hl=ja",
        "stores": [
          {
            "store_name": "GOLD'S GYM笹塚東京",
            "wls_id": "641"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/goldsgym.shibuyatokyo/?hl=ja",
        "stores": [
          {
            "store_name": "GOLD'S GYM渋谷東京",
            "wls_id": "640"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/goldsgym.omotesando/?hl=ja",
        "stores": [
          {
            "store_name": "GOLD'S GYM表参道東京",
            "wls_id": "639"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/goldsgym.harajukuannex/",
        "stores": [
          {
            "store_name": "GOLD'S GYM原宿ANNEX",
            "wls_id": "638"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/goldsgym.harajukutokyo/?hl=ja",
        "stores": [
          {
            "store_name": "GOLD'S GYM原宿東京",
            "wls_id": "637"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/sacs_shibuya/",
        "stores": [
          {
            "store_name": "SACS",
            "wls_id": "647"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/withharajukuhall/?hl=ja",
        "stores": [
          {
            "store_name": "WITH HARAJUKU",
            "wls_id": "655"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/daiso_official/",
        "stores": [
          {
            "store_name": "DAISO 渋谷センター街店",
            "wls_id": "234"
          },
          {
            "store_name": "DAISO ピーコックストア恵比寿店",
            "wls_id": "233"
          },
          {
            "store_name": "DAISO 京王クラウン街笹塚店",
            "wls_id": "232"
          },
          {
            "store_name": "DAISO 原宿店",
            "wls_id": "231"
          },
          {
            "store_name": "DAISO アコルデ代々木上原店",
            "wls_id": "230"
          },
          {
            "store_name": "DAISO ローソンストア100渋谷店",
            "wls_id": "229"
          },
          {
            "store_name": "Standard Products 渋谷マークシティ店",
            "wls_id": "228"
          },
          {
            "store_name": "DAISO 渋谷マークシティ店",
            "wls_id": "227"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/3COINS_official/",
        "stores": [
          {
            "store_name": "3COINS 原宿本店",
            "wls_id": "222"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/lifewithidee/",
        "stores": [
          {
            "store_name": "イデーショップヴァリエテ渋谷店",
            "wls_id": "214"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/plazastyle/",
        "stores": [
          {
            "store_name": "PLAZA アトレ恵比寿店",
            "wls_id": "202"
          },
          {
            "store_name": "PLAZA 渋谷109店",
            "wls_id": "201"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/nergyjapan/",
        "stores": [
          {
            "store_name": "nergy ATRE EBISU",
            "wls_id": "165"
          },
          {
            "store_name": "nergy SHIBUYA SCRAMBLE SQUARE",
            "wls_id": "164"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/emmi.jp/",
        "stores": [
          {
            "store_name": "SNEAKERS by emmi新宿高島屋店",
            "wls_id": "163"
          },
          {
            "store_name": "emmi アトレ恵比寿 西館店",
            "wls_id": "162"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/royalgardencafe/",
        "stores": [
          {
            "store_name": "ロイヤルガーデンカフェ渋谷",
            "wls_id": "439"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/loccitane_jp/",
        "stores": [
          {
            "store_name": "ロクシタン 新宿髙島屋店", 
            "wls_id":  "291"
          },
          {
            "store_name": "ロクシタン アトレ恵比寿店", 
            "wls_id": "290"
          },
          {
            "store_name": "ロクシタン 渋谷ヒカリエシンクス店", 
            "wls_id": "289"
          },
          {
            "store_name": "ロクシタン 渋谷店 ブーケ・ド・プロヴァンス", 
            "wls_id":  "288"
          },
          {
            "store_name": "ロクシタン 表参道店 ヴォヤージュ センソリアル ", 
            "wls_id": "287" 
          }
        ]
      },
      {
        "link": "https://www.instagram.com/yamano_hitsuzi/?hl=ja",
        "stores": [
          {
            "store_name": "薬膳＆米粉カフェ やまの　ひつじ",
            "wls_id": "470"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/chinese_bed/",
        "stores": [
          {
            "store_name": "中華寝台",
            "wls_id": "503"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/cosine_from_asahikawa/?hl=ja",
        "stores": [
          {
            "store_name": "コサイン青山",
            "wls_id": "402"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/narscosmeticsjapan/",
        "stores": [
          {
            "store_name": "NARS 西武渋谷店",
            "wls_id": "304"
          },
          {
            "store_name": "渋谷スクランブルスクエア ショップ＆レストラン 6階 ＋Ｑ（プラスク）ビューティー内 NARS",
            "wls_id": "303"
          },
          {
            "store_name": "NARS ビューティー・スクエア",
            "wls_id": "302"
          },
        ]
      },
      {
        "link": "https://www.instagram.com/awesomestore_jp/?hl=ja",
        "stores": [
          {
            "store_name": "AWESOME STORE TOKYO",
            "wls_id": "220"
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