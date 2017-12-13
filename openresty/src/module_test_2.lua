
_M = {}
mt = {__index=_M}

function _M.new(self)
    return setmetatable({a=5}, mt)
end

function _M.test(self)
    local a = rawget(self, "a")
    return a
end

_M.test2 = function()
    return 'Hello world'
end

return _M