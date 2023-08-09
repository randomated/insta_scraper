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
        "link": "https://www.instagram.com/fratelliparadisojapan/",
        "stores": [
          {
            "store_name": "フラテリパラディソ | 表参道ヒルズ - Omotesando Hills",
            "wls_id": "497"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/celaravird/",
        "stores": [
          {
            "store_name": "セララバアド",
            "wls_id": "501"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/restaurant_julia/",
        "stores": [
          {
            "store_name": "JULIA",
            "wls_id": "505"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/pss_harajuku/?r=nametag",
        "stores": [
          {
            "store_name": "protein supply stand｜pss 原宿",
            "wls_id": "479"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/yasai_to_kudamono_to_tanpaku/",
        "stores": [
          {
            "store_name": "野菜と果物とたんぱく",
            "wls_id": "480"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/kinnikushokudo/",
        "stores": [
          {
            "store_name": "筋肉食堂 渋谷MIYASHITA PARK店",
            "wls_id": "482"
          },
          {
            "store_name": "筋肉食堂 渋谷店",
            "wls_id": "481"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/the_theatre_table/?hl=ja",
        "stores": [
          {
            "store_name": "THE THEATRE TABLE",
            "wls_id": "487"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/longraintokyo/",
        "stores": [
          {
            "store_name": "Longrain",
            "wls_id": "493"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/mercer_brunch/",
        "stores": [
          {
            "store_name": "MERCER BRUNCH EBISU HILLSIDE",
            "wls_id": "494"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/gloriouschaincafe/",
        "stores": [
          {
            "store_name": "GLORIOUS CHAIN CAFÉ SHIBUYA",
            "wls_id": "500"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/hare_tokyo.jp/",
        "stores": [
          {
            "store_name": "ハレ ガストロノミア",
            "wls_id": "504"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/restaurant_florilege/",
        "stores": [
          {
            "store_name": "Restaurant Florilège｜フロリレージュ",
            "wls_id": "506"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/sabon_japan/",
        "stores": [
          {
            "store_name": "SABON 渋谷マークシティ店",
            "wls_id": "286"
          },
          {
            "store_name": "SABON 渋谷ヒカリエShinQs店",
            "wls_id": "285"
          },
          {
            "store_name": "SABON 表参道本店",
            "wls_id": "284"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/cledepeaubeaute/",
        "stores": [
          {
            "store_name": "クレ・ド・ポー ボーテ西武渋谷店Ａ館　１階化粧品　資生堂ショップＷブランド",
            "wls_id": "301"
          },
          {
            "store_name": "新宿髙島屋１階化粧品売場　クレ・ド・ポーボーテ　ショップ",
            "wls_id": "300"
          },
          {
            "store_name": "渋谷・東急本店　１階化粧品売場　クレ・ド・ポー　ボーテ　ショップ",
            "wls_id": "299"
          },
          {
            "store_name": "クレ・ド・ポー　ボーテ渋谷スクランブルスクエア　＋Ｑ（プラスク）ビューティー",
            "wls_id": "298"
          },
          {
            "store_name": "クレ・ド・ポーボーテ渋谷ヒカリエ　ＳｈｉｎＱｓＢ１",
            "wls_id": "297"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/suqqu_official/",
        "stores": [
          {
            "store_name": "SUQQU 渋谷スクランブルスクエア",
            "wls_id": "310"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/jillstuartbeauty/",
        "stores": [
          {
            "store_name": "JILL STUART 高島屋新宿店",
            "wls_id": "314"
          },
          {
            "store_name": "JILL STUART 西武百貨店渋谷店",
            "wls_id": "313"
          },
          {
            "store_name": "JILL STUART 渋谷スクランブルスクエア店",
            "wls_id": "312"
          },
          {
            "store_name": "JILL STUART Beauty & PARTY 東急プラザ表参道原宿店",
            "wls_id": "311"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/addictionbeauty_official/",
        "stores": [
          {
            "store_name": "ADDICTION 渋谷スクランブルスクエア店",
            "wls_id": "318"
          },
          {
            "store_name": "ADDICTION 西武渋谷店",
            "wls_id": "317"
          },
          {
            "store_name": "ADDICTION 新宿タカシマヤ",
            "wls_id": "316"
          },
          {
            "store_name": "ADDICTION STUDIO",
            "wls_id": "315"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/shuuemura/",
        "stores": [
          {
            "store_name": "shuuuemura 新宿高島屋タイムズスクエア",
            "wls_id": "328"
          },
          {
            "store_name": "shuuemura 渋谷スクランブルスクエア",
            "wls_id": "327"
          },
          {
            "store_name": "シュウ トウキョウ メイクアップ ボックス",
            "wls_id": "326"
          },
          {
            "store_name": "shuuemura 西武渋谷店",
            "wls_id": "325"
          },
          {
            "store_name": "shuuemura 渋谷パルコ",
            "wls_id": "324"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/paulandjoe_beaute/",
        "stores": [
          {
            "store_name": "PAUL&JOE高島屋 新宿店",
            "wls_id": "335"
          },
          {
            "store_name": "PAUL&JOE西武百貨店 渋谷店",
            "wls_id": "334"
          },
          {
            "store_name": "渋谷スクランブルスクエア ショップ＆レストラン 6階 ポール ＆ ジョー ＋Qビューティー店",
            "wls_id": "333"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/annasuicosmetics/",
        "stores": [
          {
            "store_name": "ANNASUI ラフォーレ原宿ストア",
            "wls_id": "336"
          }
        ]
      },
      {
        "link": "https://www.instagram.com/ipsa_jp/",
        "stores": [
          {
            "store_name": "IPSAウィズ原宿 ビューティ・スクエア店",
            "wls_id": "296"
          },
          {
            "store_name": "IPSA渋谷PARCO店",
            "wls_id": "295"
          },
          {
            "store_name": "IPSA渋谷スクランブルスクエア店",
            "wls_id": "294"
          },
          {
            "store_name": "IPSA西武渋谷店",
            "wls_id": "293"
          },
          {
            "store_name": "IPSA 新宿タカシマヤ",
            "wls_id": "292"
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
