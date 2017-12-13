local account = require("lua_class")
print(account)
local a = account.new()
a:deposit(100)


local my_talbe = {a = 5}
print (my_talbe.a, my_talbe['a'])
my_talbe.b = 10
print(my_talbe.b)