local test_square = require "module_test_1"
local test_square2 = require "module_test_2"
ngx.say('Hello, world!')
local regex = [[\w+, \w+]]

-- 参数 "j" 启用 JIT 编译，参数 "o" 是开启缓存必须的
local m = ngx.re.match("hello, 1234", regex, "jo")
if m then
    ngx.say(m[0])
else
    ngx.say("not matched!")
end

local s = 'Hello, World!'
local i, j = string.find(s, 'Hello')
ngx.say(i..' '..j)

local s = 'hello world from lua'
for world in string.gmatch(s, '%a+') do
    ngx.say(world)
end

--子字符串替换
local b = string.gsub(s, 'hello', 'HELLO')
ngx.say(b)

--模块函数测试
ngx.say(test_square)
test_new = test_square2:new()
ngx.say(test_new:test())
ngx.say(test_new.test2())

