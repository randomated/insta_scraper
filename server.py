import json
from datetime import datetime, timedelta
from flask import Flask, Response
from saver import Saver
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, str):
      return obj.encode('utf-8').decode('unicode-escape')
    return super().default(obj)

def get_data(batch):
  today = datetime.now()
  yesterday = today - timedelta(days=1)
  path = os.path.join(current_directory, batch, "datas", yesterday.strftime('%Y-%m-%d'))
  saver = Saver(path)
  data = saver.fetch_datas()
  saver.close_db()
  return data

@app.route('/insta/api/v1/batchone')
def batchone():
  data = get_data("batch1")
  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  return response

@app.route('/insta/api/v1/batchtwo')
def batchtwo():
  data = get_data("batch2")
  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  return response

@app.route('/insta/api/v1/batchthree')
def batchthree():
  data = get_data("batch3")
  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  return response

@app.route('/insta/api/v1/batchfour')
def batchfour():
  data = get_data("batch4")
  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  return response

@app.route('/insta/api/v1/batchfive')
def batchfive():
  data = get_data("batch5")
  json_data = json.dumps(data, ensure_ascii=False, cls=CustomJSONEncoder)
  response = Response(json_data, content_type='application/json; charset=utf-8')
  return response

if __name__ == '__main__':
  app.json_provider_class = CustomJSONEncoder
  app.run(host='0.0.0.0', port=3001)
