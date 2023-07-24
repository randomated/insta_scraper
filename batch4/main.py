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
        "link": "https://www.instagram.com/hatha_yoga_ayo/",
        "stores": [
          {
            "store_name": "AYO: Ashtanga Yoga Omotesando",
            "wls_id": "264"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/bobbibrownjapan/",
        "stores": [
          {
            "store_name": "BOBBI BROWN 新宿髙島屋",
            "wls_id": "342"
          },
          {
            "store_name": "BOBBI BROWN渋谷スクランブルスクエア",
            "wls_id": "341"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/cliniquejp/",
        "stores": [
          {
            "store_name": "クリニーク渋谷スクランブルスクエア",
            "wls_id": "346"
          },
          {
            "store_name": "クリニーク新宿高島屋",
            "wls_id": "345"
          },
          {
            "store_name": "クリニーク西武 渋谷店",
            "wls_id": "344"
          },
          {
            "store_name": "クリニーク渋谷ヒカリエShinQs",
            "wls_id": "343"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/today_sagarayoga_studio/?hl=ja",
        "stores": [
          {
            "store_name": "TODAY SAGARA YOGA STUDIO",
            "wls_id": "244"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/zenplace_official/",
        "stores": [
          {
            "store_name": "zen place pilates 恵比寿スタジオ",
            "wls_id": "247"
          },
          {
            "store_name": "zen place pilates 代官山スタジオ",
            "wls_id": "246"
          },
          {
            "store_name": "zen place pilates 渋谷スタジオ",
            "wls_id": "245"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/clubpilates_japan/",
        "stores": [
          {
            "store_name": "Club Pilates 恵比寿ガーデンプレイス",
            "wls_id": "248"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/bdcpilates/",
        "stores": [
          {
            "store_name": "BDC PILATES恵比寿",
            "wls_id": "251"
          },
          {
            "store_name": "BDC PILATES表参道 B Studio",
            "wls_id": "250"
          },
          {
            "store_name": "BDC PILATES表参道 A Studio",
            "wls_id": "249"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/pilates_thesilk_hiroo/",
        "stores": [
          {
            "store_name": "ピラティススタジオ the SILK 広尾・恵比寿",
            "wls_id": "252"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/igniteliving/",
        "stores": [
          {
            "store_name": "IGNITE yoga studio h",
            "wls_id": "253"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/studioes731/",
        "stores": [
          {
            "store_name": "ピラティススタジオ STUDIO es",
            "wls_id": "254"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/pilates.studiotou/",
        "stores": [
          {
            "store_name": "studio tou 東京原宿",
            "wls_id": "255"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/yoga_simple/",
        "stores": [
          {
            "store_name": "SiMPLE 渋谷本店",
            "wls_id": "257"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/pilateslab_daikanyama/",
        "stores": [
          {
            "store_name": "ピラティスラボ 代官山スタジオ",
            "wls_id": "259"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/studiobodydesign/",
        "stores": [
          {
            "store_name": "スタジオボディデザイン渋谷店",
            "wls_id": "260"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/arancia_masterstretch/",
        "stores": [
          {
            "store_name": "ピラティス・スタジオ・アランチャ　渋谷本店",
            "wls_id": "262"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/lavayoga_official/",
        "stores": [
          {
            "store_name": "ホットヨガスタジオLAVA渋谷店",
            "wls_id": "239"
          },
          {
            "store_name": "ホットヨガスタジオLAVA恵比寿東口店",
            "wls_id": "240"
          },
          {
            "store_name": "ホットヨガスタジオLAVA笹塚店",
            "wls_id": "241"
          },
          {
            "store_name": "ホットヨガ スタジオ カルド 渋谷",
            "wls_id": "242"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/airweave/",
        "stores": [
          {
            "store_name": "airweave 高島屋 新宿店",
            "wls_id": "398"
          },
          {
            "store_name": "airweave ハンズ新宿店",
            "wls_id": "397"
          },
          {
            "store_name": "airweave ハンズ渋谷店",
            "wls_id": "396"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/artekjapan/",
        "stores": [
          {
            "store_name": "Artek Tokyo",
            "wls_id": "399"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/boconcept_jp/",
        "stores": [
          {
            "store_name": "BOCONCEPT 代官山",
            "wls_id": "400"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/fritzhansen/",
        "stores": [
          {
            "store_name": "FRITZ HANSEN TOKYO",
            "wls_id": "403"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/saint_marc_cafe_official/",
        "stores": [
          {
            "store_name": "サンマルクカフェ 恵比寿東口店",
            "wls_id": "602"
          },
          {
            "store_name": "サンマルクカフェ 渋谷公園通り店",
            "wls_id": "601"
          },
          {
            "store_name": "サンマルクカフェ+R 恵比寿駅前店",
            "wls_id": "600"
          },
          {
            "store_name": "サンマルクカフェ 代々木上原店",
            "wls_id": "599"
          },
          {
            "store_name": "サンマルクカフェ 渋谷道玄坂店",
            "wls_id": "598"
          },
        ]
      },
      {
        "link": "https://www.instagram.com/excelsiorcaffe_official/",
        "stores": [
          {
            "store_name": "エクセルシオール カフェ 渋谷宮益坂店",
            "wls_id": "597"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/cafedecrie/",
        "stores": [
          {
            "store_name": "カフェ・ド・クリエ グラン 恵比寿ガーデンプレイス店",
            "wls_id": "607"
          },
          {
            "store_name": "カフェ・ド・クリエ グラン　渋谷桜丘スクエア店",
            "wls_id": "606"
          },
          {
            "store_name": "カフェ・ド・クリエ 代々木東口店",
            "wls_id": "605"
          },
          {
            "store_name": "カフェ・ド・クリエ 南新宿店",
            "wls_id": "604"
          },
          {
            "store_name": "カフェ・ド・クリエ 渋谷3丁目店",
            "wls_id": "603"
          },
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