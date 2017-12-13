Window = {}  

Window.mt = {}  
function Window.new(o)  
    setmetatable(o ,Window.mt)  
    return o  
end  

Window.mt.__index = function (t ,key)  
    return 1000  
end
  
Window.mt.__newindex = function (table ,key ,value)  
    if key == "wangbin" then
		print ("set wangbing")
        rawset(table ,"wangbin" ,"yes,i am")  
    end  
end  
w = Window.new{x = 10 ,y = 20}
w.wangbin = 50
print(w.x)
print(w.wangbin)
print(rawget(w ,w.wangbin))  

--------
print(string.format("%d %04d", 1, 2))

mytable = setmetatable({key1 = "value1"}, 
{__index = function(self, key)
			return "not has key"
			end})
			
print(mytable.key1, mytable.key2)