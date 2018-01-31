### mongo pretty输出 ###
    db.monitorchangeitems.find({type:"Person"}).pretty()
### exists ###
    db.coll.find.{field:{$exists:true}}
### insert ###
    db.col.insert({title: 'MongoDB 教程', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
	})

### 查询 ###
    #### 查询list ####
	db.docs.find({'recentDownload':'coco'})
	同时包含
	db.food.find({“fruit”:{“$all”:["apple","banana"]}})
	包含其中一个
	db.food.find({“fruit”:{“$in”:["apple","banana"]}})
	查询指定长度
	db.food.find({“fruit”:{$size:3}})
	查询dict
	 {'author':{
	    'name':'coco',
	    'sex':'f'
	}}
	db.testDoc.find({'author.name':'coco'})
	时间
	db.docs.find({'uploadtime':{
        '$lte':time.strftime('%F %X',time.localtime(time.time())),
        '$gt':time.strftime('%F %X',time.localtime(time.time())),
        }
    })

### 删除 ###
    db.collection.remove(
   	<query>,
	   {
	     justOne: <boolean>,
	     writeConcern: <document>
	   }
	)

### 范围 ###
	db.testDoc.find({'x':{'$gt':6,'$lt':24}})
### 创建数据库账号 ###
	db.createUser(
	  {
	    user: "test",
	    pwd: "passwd",
	    roles:
	    [
	      {
	        role: "readWrite",
	        db: "dbname"
	      }
	    ]
	  }
	)