mytable = setmetatable({key1 = "value1"}, {
  __index = function(mytable, key)
    if key == "key2" then
      return "metatablevalue"
    else
      return mytable[key]
    end
  end
})
print(mytable.key1,mytable.key2)
test_table = {[1]=5, [2] =4}
test_table = {x = 5, y = 4}
for key, value in pairs(test_table) do
	print(key, value)
end
print("len: ", #test_table, type(test_table))
test_table2 = {4, 5, 6}
print("len: ", #test_table2, type(test_table2))
test_table3 = {4, 5, 6, y = 8}
print("len: ", #test_table2, type(test_table3))

test_arry = {}
test_arry[1] = 5
print (type(test_arry))