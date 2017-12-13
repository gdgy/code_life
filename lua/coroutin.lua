local function test_corotuine()
	print ("Hello, lua coroutine")
end
	
local co = coroutine.create(test_corotuine)


print (coroutine.status(co), co)

--用了resume函数，将协同程序co由suspended改为running状态
coroutine.resume(co)
print(coroutine.status(co))

--[[local function test_corotuine2(a, b)
	a = a*a
	b = b*b*b
	coroutine.yield(a, b)
end]]--

local co_test2 = coroutine.create(function (a, b)
									 a = a*a
									b  = b*b*b
									coroutine.yield(a, b)
									end)
print(coroutine.resume(co_test2, 2, 3))
print(coroutine.resume(co_test2))