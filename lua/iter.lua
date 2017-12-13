function values(tb)
	local i = 0
	return function() 
				i = i + 1
				return tb[i]
			end
end

local testTb = {10, 20 , 30}
print (values(testTb))
for value in values(testTb) do
	print (value)
end
assert (true, "test assert")

test_table1 = {"a", "b", "c"}
test_table2 = {a="aa", b="b", c="c"}
-- ipairs只能用于数字索引
for key, value in ipairs(test_table1) do
	print (key, value)
end

for key, value in pairs(test_table1) do
	print (key, value)
end
print (test_table1[4])
print (test_table2['a'])

for key, value in pairs(test_table2) do
	print(key, value)
end
