#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from tornado import websocket, web, ioloop
from tornado.escape import json_encode, json_decode

from CodernityDB.database import Database, DatabasePathException, HashIndex

class ChanelIndex(HashIndex):

    def __init__(self, *args, **kwargs):
        kwargs['key_format'] = 'I'
        super(ChanelIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("channel")
        if a_val is not None:
            return md5(a_val).digest(), None
        return None

    def make_key(self, key):
        return md5(key).digest()


# http://stackoverflow.com/questions/2266646/how-to-i-disable-and-re-enable-console-logging-in-python
import logging
logging.basicConfig(level=logging.DEBUG)



with open('config.json') as data_file:
  config = json.load(data_file)

cl = []

class IndexHandler(web.RequestHandler):
  def get(self):
    self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):

  def open(self):
    if self not in cl:
      cl.append(self)
  def on_message(self, message):
    try:
      data = json_decode(message)
    except ValueError:
      self.write_message(u'{"error": {"status": 400, "description": "Parsing error"}')
      return
    # create item(s)
    if data["type"] == "create":
      for item in data.pop("items", None):
        if "info-property" in data and data["info-property"] in item:
          infoProp = item.pop(data["info-property"], None)
        item["channel"] = data["channel"]
        item.update(db.insert(item))
        item.pop("channel", None)
        if "info-property" in data:
          item.update({data["info-property"]:infoProp})
        data["items"] = [item];
        self.write_message(data)
    elif data["type"] == "read":
      responseItems = []
      if "items" in data:
        for item in data["items"]:
          responseItems.insert(0, db.get("id", item["_id"], with_doc=True, with_storage=True))
      data["items"] = responseItems
      self.write_message(data)


  def on_close(self):
    if self in cl:
      cl.remove(self)

class ApiHandler(web.RequestHandler):

  @web.asynchronous
  def get(self, *args):
    self.finish()
    id = self.get_argument("id")
    value = self.get_argument("value")
    data = {"id": id, "value" : value}
    data = json.dumps(data)
    for c in cl:
      c.write_message(data)

  @web.asynchronous
  def post(self):
    pass

app = web.Application([
  (r'/', IndexHandler),
  (r'/ws', SocketHandler),
  (r'/api', ApiHandler),
  (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
])

db = Database(config["storage"]["directory"])

if __name__ == '__main__':
  app.listen(config['port'])
  try:
    db.open()
    logging.info("Open database in: %s", config["storage"]["directory"])
  except DatabasePathException:
    db.create()
    logging.info("Database does not exist in %s (creating new)", config["storage"]["directory"])
    db.add_index(ChanelIndex(db.path, 'channel'))
  try:
    logging.info("Server starts on port: %s", config['port'])
    ioloop.IOLoop.instance().start()
  except KeyboardInterrupt:
    logging.info("Server closing..")
    ioloop.IOLoop.instance().stop()