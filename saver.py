import os
import sqlite3
from datetime import datetime
import re

class Saver:
  __conn = None
  __db_file = None

  def __init__(self, current_directory):
    self.__db_file = f"{current_directory}/scraped.sqlite"

    if not os.path.exists(current_directory):
      os.makedirs(current_directory)

    if not os.path.exists(self.__db_file):
      self.__conn = sqlite3.connect(self.__db_file)
      self.__conn.execute('''CREATE TABLE scraped_datas
        (id INTEGER PRIMARY KEY,
        body TEXT,
        link TEXT)''')

      self.__conn.execute('''CREATE TABLE image_links
        (id INTEGER PRIMARY KEY,
        scraped_data_id INTEGER,
        image_link TEXT, 
        FOREIGN KEY (scraped_data_id) REFERENCES scraped_datas(id))''')

      self.__conn.execute('''CREATE TABLE stores
        (id INTEGER PRIMARY KEY,
        scraped_data_id INTEGER,
        store_name TEXT, 
        wls_id INTEGER, 
        FOREIGN KEY (scraped_data_id) REFERENCES scraped_datas(id))''')
    else:
      self.__conn = sqlite3.connect(self.__db_file)

  def add_scraped_data(self, body, link, image_links):
    cursor = self.__conn.cursor()
    cursor.execute('INSERT INTO scraped_datas (body, link) VALUES (?, ?)', (body, link))
    inserted_id = cursor.lastrowid

    cursor.executemany('INSERT INTO image_links (scraped_data_id, image_link) VALUES (?, ?)', [(inserted_id, link) for link in image_links])

    self.__conn.commit()
    cursor.close()
    return inserted_id

  def add_store(self, scraped_data_id, store_name, wls_id):
    cursor = self.__conn.cursor()
    cursor.execute('INSERT INTO stores (scraped_data_id, store_name, wls_id) VALUES (?, ?, ?)', (scraped_data_id, store_name, wls_id))

    self.__conn.commit()
    cursor.close()

  def fetch_datas(self):
    result = []

    scraped_data_cursor = self.__conn.cursor()
    scraped_data_cursor.execute('SELECT * FROM scraped_datas;')
    scraped_datas = scraped_data_cursor.fetchall()

    for index, scraped_data in enumerate(scraped_datas):
      image_link_cursor = self.__conn.cursor()
      image_link_cursor.execute('SELECT * FROM image_links WHERE scraped_data_id = ?;', (scraped_data[0],))
      image_links = image_link_cursor.fetchall()

      store_cursor = self.__conn.cursor()
      store_cursor.execute('SELECT * FROM stores WHERE scraped_data_id = ?', (scraped_data[0],))
      stores = store_cursor.fetchall()

      target_store_names = [
        [
        "サンマルクカフェ 恵比寿東口店",
        "サンマルクカフェ+R 恵比寿駅前店",
        "サンマルクカフェ 代々木上原店",
        "サンマルクカフェ 渋谷道玄坂店",
        "サンマルクカフェ 渋谷公園通り店"
        ],
        [
          "BiOcafe"
        ],
      ]

      fetched_store_names = [store[2] for store in stores]

      all_exist = all(any(target_store in sublist for sublist in target_store_names) for target_store in fetched_store_names)

      if all_exist:
        result.append({ "title": "", "body": scraped_data[1], "link": scraped_data[2], "complete_body": scraped_data[1], "images": [], "stores": [] })
      else:
        first_stanzas = scraped_data[1].replace(".\n", "").split("\n")[0]
        remaining_lines = "".join(scraped_data[1].replace(".\n", "").split("\n")[1:])
        result.append({ "title": first_stanzas, "body": remaining_lines, "link": scraped_data[2], "complete_body": scraped_data[1], "images": [], "stores": [] })

      for image_link in image_links:
        result[index]["images"].append(image_link[2])

      for store in stores:
        result[index]["stores"].append({ "store_name": store[2], "wls_id": store[3] })

      image_link_cursor.close()
      store_cursor.close()

    scraped_data_cursor.close()

    return result

  def __limit_text(self, text, max_length=105):
    if len(text) > max_length:
      return text[:max_length] + "..."
    return text

  def close_db(self):
    self.__conn.close()