Websocket comunication
----------------------
###Create item(s)
**request:**

	{
	   "channel": "wiki",
	   "type": "create",
	   "info-property": "cid",
	   "properties":[],
	   "items": [
	      {
	         "cid":"r3457",
	         "title":"hello",
	         "body":"world"
	      },
	      {
	         "cid":"r3458",
	         "title":"hello2",
	         "body":"world2"
	      }
	   ]
	}
 * **channel** - module / index name
 * **type** - request type `create`, `read`, `update`, `delete`, `subscribe`, `unsubscribe`
 * **info-property** (*optimal*) - property in `items` that will not be wrote in database, but used just for response detection (will back in response)
 * **properties** (*optimal*) - list of properties to return, if not set then will return all, if empty will return only `_id` and proporties setted in `info-property`
 * **items** - array of documents

**response:**

	{
	   "channel": "wiki",
	   "type": "create",
	   "items": [
	      {
	         "cid":"r3457",
	         "_rev": "00014dc9",
	         "_id": "4a1bbd33b494414f9d8dacbf7b19441a"
	      },
	      {
	        "cid":"r3458",
	        "_rev": "000198e1",
	        "_id": "beab46b910ca4b549e33c85fc4f23a16"
	      }
	   ]
	}

###Read item(s)
**request one item:**

	{
	   "channel": "wiki",
	   "type": "read",
	   "info-property": "cid",
	   "properties":["title","body"],
	   "items": [
	      {
	         "cid":"r345",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a"
	      }
	   ]
	}
 * **channel** - module / index name
 * **type** - request type `create`, `read`, `update`, `delete`, `subscribe`, `unsubscribe`
 * **info-property** (*optimal*) - property in `items` that will not be wrote in database, but used just for response detection (will back in response)
 * **properties** (*optimal*) - list of properties to return, if not set then will return all, if empty will return only `_id` and proporties setted in `info-property`
 * **items** - array of documents

**request item list:**

	{
	   "channel": "wiki",
	   "type": "read",
	   "limit":[10,30],
	   "properties":["title","body"],
	   "order":["title","desc"]
	}

 * **channel** - module / index name
 * **type** - request type `create`, `read`, `update`, `delete`, `subscribe`, `unsubscribe`
 * **limit** (*optimal*) - [from, count], if not set will return all (or maximum allowed in config)
 * **properties** (*optimal*) - list of properties to return, if not set then will return all, if empty will return only `_id`
 * **order** (*optimal* works if set limit) - array[0] - sort by, array[1] - order direction

**response one item:**

	{
	   "channel": "wiki",
	   "type": "read",
	   "info-property": "cid",
	   "properties":["title","body"],
	   "items": [
	      {
	         "title": "some title",
	         "body":"some body",
	         "cid":"r345",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a"
	      }
	   ]
	}
**response items list:**

	{
	   "channel": "wiki",
	   "type": "read",
	   "limit":[10,30],
	   "properties":["title","body"],
	   "order":["title","desc"],
	   "items": [
	      {
	         "title": "some title",
	         "body":"some body",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a"
	      },
	      {
	         "title": "some title1",
	         "body":"some body2",
	         "_id":"beab46b910ca4b549e33c85fc4f23a16"
	      }
	   ]
	}


###Update item(s)

**request one item:**

	{
	   "channel": "wiki",
	   "type": "update",
	   "info-property": "cid",
	   "properties":["title","body"],
	   "items": [
	      {
	         "cid":"r3457",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a"
	         "title":"set other title",
	         "body":"world"
	      },
	      {
	         "cid":"r3458",
	         "_id":"beab46b910ca4b549e33c85fc4f23a16",
	         "title":"set other title 2",
	         "body":"or set other body"
	      }
	   ]
	}
 * **channel** - module / index name
 * **type** - request type `create`, `read`, `update`, `delete`, `subscribe`, `unsubscribe`
 * **info-property** (*optimal*) - property in `items` that will not be wrote in database, but used just for response detection (will back in response)
 * **properties** (*optimal*) - list of properties to return, if not set then will return all, if empty will return only `_id` and proporties setted in `info-property`
 * **items** (for each item must be set `_id`) - array of documents

####(TODO request item list)

**response one item:**


	{
	   "channel": "wiki",
	   "type": "update",
	   "items": [
	      {
	         "cid":"r3457",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a",
	         "title":"set other title",
	         "body":"world"
	      },
	      {
	         "cid":"r3458",
	         "_id":"beab46b910ca4b549e33c85fc4f23a16",
	         "title":"set other title 2",
	         "body":"or set other body"
	      }
	   ]
	}

####(TODO response item list)

###delete item(s)
**request:**

	{
	   "channel": "wiki",
	   "type": "delete",
	   "info-property": "cid",
	   "items": [
	      {
	         "cid":"r3457",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a"
	      },
	      {
	         "cid":"r3458",
	         "_id":"beab46b910ca4b549e33c85fc4f23a16"
	      }
	   ]
	}

**response:**

	{
	   "channel": "wiki",
	   "type": "delete",
	   "info-property": "cid",
	   "items": [
	      {
	         "cid":"r3457",
	      },
	      {
	         "cid":"r3458",
	      }
	   ]
	}

#Draft

-----------------

###Subscribe chanel

**request one item:**

	{
	   "channel": "wiki",
	   "type": "subscribe",
	   "info-property": "cid",
	   "properties": ["title", "body"],
	   "items": [
	      {
	         "cid":"r345",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a"
	      }
	   ]
	}
 * **channel** - module / index name
 * **type** - request type `create`, `read`, `update`, `delete`, `subscribe`, `unsubscribe`
 * **info-property** (*optimal*) - property in `items` that will not be wrote in database, but used just for response detection (will back in response)
 * **properties** (*optimal*) - list of properties to return, if not set then will return all, if empty will return only `_id` and proporties setted in `info-property`
 * **items** - array of documents

**request item list:**

	{
	   "channel": "wiki",
	   "type": "subscribe",
	   "limit":[10,30],
	   "properties":["title","body"],
	   "order":["title","desc"]
	}

 * **channel** - module / index name
 * **type** - request type `create`, `read`, `update`, `delete`, `subscribe`, `unsubscribe`
 * **limit** (*optimal*) - [from, count], if not set will return all (or maximum allowed in config)
 * **properties** (*optimal*) - list of properties to return, if not set then will return all, if empty will return only `_id`
 * **order** (*optimal* works if set limit) - array[0] - sort by, array[1] - order direction

**response one item:**

automatically on `create` / `update` / `delete`

#####todo think about status-success for subscribe

	{
	   "channel": "wiki",
	   "type": "subscribe",
	   "info-property": "cid",
	   "properties": ["title", "body"],
	   "items": [
	      {
	         "cid":"r345",
	         "_id":"4a1bbd33b494414f9d8dacbf7b19441a",
	         "status": "success"
	      }
	   ]
	}

**response items list:**
#####todo think about status-success for subscribe
	{
	   "channel": "wiki",
	   "type": "subscribe",
	   "limit":[10,30],
	   "properties":["title","body"],
	   "order":["title","desc"],
	   "status": "success"
	}

###Unsubscribe chanel
**request:**

	{
	   "channel": "wiki",
	   "type": "unsubscribe"
	}

**response**

	{
	   "channel": "wiki",
	   "type": "unsubscribe",
	   "status": "success"
	}