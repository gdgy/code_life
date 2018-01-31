# Redis #
## redis 事务 ##
    multi开始 exec结束
	在事务开始前watch的变量，如果在事务提交前改变，事务会取消执行 
	