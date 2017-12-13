--测试redis的使用
local function close_redis(red)
	if not red then
		return
	end
	local ok, err = red:close()
	if not ok then
		ngx.say("close redis error:", err)
	end
end

    ngx.say('hello redis')
	local redis = require("resty.redis")

	--创建实例
	local red = redis:new()

	red:set_timeout(1000)

	local ip = "127.0.0.1"
	local port = "6379"
	
	local ret, err = red:connect(ip, port)
	if not ret then
		ngx.say("connect to redis error: ", err)
		return close_redis(red)
	end
	
	ret, err = red:set("msg", "hello redis!")
	if not ret then
		ngx.say("set msg error: ", err)
		return close_redis(red)
	end
	
	local resp, err = red:get("msg")  
	if not resp then  
		ngx.say("get msg error : ", err)  
		return close_reedis(red)  
	end  
	--得到的数据为空处理  
	if resp == ngx.null then  
		resp = ''  --比如默认值  
	end  
	ngx.say("msg : ", resp)  

	close_redis(red)