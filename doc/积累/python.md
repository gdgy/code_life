## 日志格式设置 ##
    logging.basicConfig(level=logging.DEBUG,
          format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
          datefmt='%m-%d %H:%M',
          filename='myapp.log',
          filemode='w')
	# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
	console = logging.StreamHandler()
	console.setFormatter(formatter)
	# 将定义好的console日志handler添加到root logger
	logging.getLogger('').addHandler(console)

### mysql事物操作 ###
>  对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。（在上一个笔记上面写了mysql语句在python中的使用）
    db = MySQLdb.connect("ip地址，本机为localhost"，"用户名","密码","表名")

	#打开数据库的连接 
	
	cursor = db.cursor()
	
	#使用cursor()方法获得操作游标
	
	try:
	   # 执行sql语句
	   cursor.execute("update account set money=money-600 where name='zhangsan'")
	   cursor.execute("update account set money=money+600 where name='lisi'")
	   # 提交到数据库执行
	   db.commit()
	except:
	   # 发生错误时回滚    回滚到获取游标的位置开始重新执行  看代码上面的文字有说明
	   db.rollback()
	
	db.close()

### list排序 ###
	list list排序
    sorted(L, key=lambda x: x[1], reverse=True)
	sorted(L, key=lambda x: x[1])
	list dict排序
	sorted(L, key=lamdba x: x['key'])

### gevent monkey ###
    Monkey-patching not on the main thread; threading.main_thread().join() w
	python3 -m gevent.monkey app.py
### 静态方法类方法 ###
	class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")

	foo = Foo()
	foo.instance_method()
	foo.static_method()
	foo.class_method()
	print('----------------')
	Foo.static_method()
	Foo.class_method()

	实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。
	实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
	静态方法，参数没有要求。
	类方法，第一个参数必须要默认传类，一般习惯用cls。

### 父类构造函数 ###
	以下两种方法
	 Parent.__init__(self)
     super(Parent, self).__init__()
