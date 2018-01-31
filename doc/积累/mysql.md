## mysql insert ##
	IF NOT EXISTS (SELECT * FROM `table` WHERE username = 'foo') THEN
	  INSERT INTO `table` (username) VALUES ('foo');
	END IF;

## mysql id跳跃 insert插入失败 ##
	
> "In all lock modes (0, 1, and 2), if a transaction that generated auto-increment values rolls back, those auto-increment values are “lost.” Once a value is generated for an auto-increment column, it cannot be rolled back, whether or not the “INSERT-like” statement is completed, and whether or not the containing transaction is rolled back. Such lost values are not reused. Thus, there may be gaps in the values stored in an AUTO_INCREMENT column of a table."

### acid ###
> 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
>
>原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
>
>一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。

>持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。

### mysql  ###
> 列设置为自增是缓存在内存字典中的,分配方式是先预留,然后再插入的.所以插入失败不会回滚内存字典.

### update ###
    UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;
### delete ###
	DELETE FROM runoob_tbl WHERE runoob_id=3;
### insert ###
	INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       		( value1, value2,...valueN );	
### like ###
	SELECT * from runoob_tbl  WHERE runoob_author LIKE '%COM';

### 跳过前多少条 ###
    语句1：select * from student limit 9,4
	语句2：slect * from student limit 4 offset 9
	// 语句1和2均返回表student的第10、11、12、13行  
	//语句2中的4表示返回4行，9表示从表的第十行开始
	例2，通过limit和offset 或只通过limit可以实现分页功能。
	假设 numberperpage 表示每页要显示的条数，pagenumber表示页码，那么 返回第pagenumber页，每页条数为numberperpage的sql语句：