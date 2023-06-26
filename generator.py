import os
import shutil


def generate_text_code(port):
  text = f"""import json
from flask import Flask, Response
from database.saver import Saver
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, str):
      return obj.encode('utf-8').decode('unicode-escape')
    return super().default(obj)

@app.route('/')
def index():
  saver = Saver(current_directory)
  data = saver.fetch_datas()

  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  
  saver.close_db()
  return response

if __name__ == '__main__':
  app.json_provider_class = CustomJSONEncoder
  app.run(host='0.0.0.0', port={port})"""

  return text

destination_folder = "./toserver"
if os.path.exists(destination_folder):
  shutil.rmtree(destination_folder)

os.makedirs(destination_folder, exist_ok=True)

batches = [ 
  { 
    "fname": "batch1", 
    "port": 3001 
  }, 
  { 
    "fname": "batch2", 
    "port": 3002 
  }, 
  { 
    "fname": "batch3", 
    "port": 3003 
  }, 
  { 
    "fname": "batch4", 
    "port": 3004 
  }, 
  { 
    "fname": "batch5", 
    "port": 3005 
  } 
]

for batch in batches:
  shutil.copytree(f"./{batch['fname']}/database", f"{destination_folder}/{batch['fname']}/database")
  shutil.copytree(f"./{batch['fname']}/datas", f"{destination_folder}/{batch['fname']}/datas")
  shutil.copy2(f"./{batch['fname']}/server.py", f"{destination_folder}/{batch['fname']}")

  with open(f"{destination_folder}/{batch['fname']}/server.py", "w") as file:
    file.write(generate_text_code(3000))


