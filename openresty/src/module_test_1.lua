local _M = {}
_M.VERSION = '1.0'

local mt = {__index = _M}

function _M.new(self, width, heith)
    return setmetatable({width=width, heith=heith}, mt)
end

function _M.square(self)
    return self.width * self.heith
end