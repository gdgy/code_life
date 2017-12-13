local test_square = require "module_test_1"
local test_square2 = require "module_test_2"
ngx.say('Hello, world!')
local regex = [[\w+, \w+]]

-- ���� "j" ���� JIT ���룬���� "o" �ǿ�����������
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

--���ַ����滻
local b = string.gsub(s, 'hello', 'HELLO')
ngx.say(b)

--ģ�麯������
ngx.say(test_square)
test_new = test_square2:new()
ngx.say(test_new:test())
ngx.say(test_new.test2())

