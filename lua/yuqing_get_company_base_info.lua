--require("user_util3")
local args = ngx.req.get_uri_args()
local company_name = args.company_name
local query_type = args.type

ngx.log(ngx.INFO, "company_name:", company_name, "query_type:",query_type)
if nil == company_name or nil == query_type then
	ngx.log(ngx.ERR, "input parameters formater error company_name:" ,  company_name, "query_type:", query_type)
	--ngx.header["X-IS-Error-Code"] = user_errcode.TS_ERR_PARAMETER
	--user_util3.http_return(406)
	ngx.exit(ngx.HTTP_OK)
end

query_type = string.lower(query_type)
query_types = {'product_info', 'list_delist_info', 'employee_status', 'achievement_award', 'other_info', 'all_types'}
ngx.say(company_name, query_type)
ngx.exit(ngx.HTTP_OK)




