1.
    git clone

	vim localrc
	
	#Passwords
	MYSQL_PASSWORD=stack
	ADMIN_PASSWORD=stack
	SERVICE_PASSWORD=stack
	RABBIT_PASSWORD=stack
	SERVICE_TOKEN_PASSWORD=stack
	
	#enable_service ceilometer
	enable_service ceilometer-acompute
	enable_service ceilometer-acentral
	enable_service ceilometer-collector
	enable_service ceilometer-api

	FORCE=yes ./stack.sh
	
