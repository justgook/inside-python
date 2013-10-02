REST+subscribe
--------------
**create items**

	{post:
      [
        {
          chanel:wiki,
          items:[
            {id:"1234567",title:"hello",body: "world"},
            {id:"1234568",title:"hello2",body: "world2"},
          ]
        }
      ]
    }
    
**update items**

{
   "put":[
      {
         "chanel":"wiki",
         "tems":[
            {
               "id":"1234567",
               "title":"hello",
               "body":"world"
            },
            {
               "id":"1234568",
               "title":"hello2",
               "body":"world2"
            }
         ]
      }
   ]
}
    
**delete items**

	{delete:
      [
        {
          chanel:wiki,
          items:[
            {id:"1234567",title:"hello",body: "world"},
            {id:"1234568",title:"hello2",body: "world2"},
          ]
        }
      ]
    }
    
**get items**

	{get:
      [
        {
          chanel:wiki,
          props:["id","title","body"],
          limit:[10,30],
          order:["id","desc"],
          by:"id>10"
        }
      ]
    }
    
**subscribe chanel**

	{subscribe:
      [
        {
          chanel:wiki,
          props:["id","title"],
          limit:[10,30],
          order:["id","desc"],
          by:"id>10"
        }
      ]
    }

**unsubscribe chanel**

	{unsubscribe:
      [
        {
          chanel:wiki,
          props:["id","title"],
          limit:[10,30],
          order:["id","desc"],
          by:"id>10"
        }
      ]
    }