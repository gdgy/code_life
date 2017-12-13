local user_util3 = require(user_util3)
local args = ngx.req.get_uri_args()
local company_name = args.company_name
local query_type = args.type

if nil == company_name or nil == query_type then
	ngx.log(ngx.ERR, "input parameters formater error company_name:" ,  company_name, "query_type:", query_type)
	ngx.header["X-IS-Error-Code"] = user_errcode.TS_ERR_PARAMETER
	user_util3.http_return(406)
end
ngx.log(ngx.INFO, "company_name:", company_name, "query_type:"query_type)
query_type = string.lower(query_type)
query_types = {product_info=1, list_delist_info=2, employee_status=3, achievement_award=4, other_info=5, all_types=6}

--验证输入参数
if query_types.query_type == nil then
	ngx.log(ngx.ERR, "input parameters formater error company_name:" ,  company_name, "query_type:", query_type)
	ngx.header["X-IS-Error-Code"] = user_errcode.TS_ERR_PARAMETER
	user_util3.http_return(406)
end



--判断输入参数
ngx.say(company_name, query_type)




