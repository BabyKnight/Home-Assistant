#!/bin/bash

# Assistant Web Service's command-line utility for service control
# Features:
# 	- default mode for production and development
#	- Service start/stop/restart/status



show_usage() {
    echo "Usage: $0 [-dev|--d] / start/stop/status"
    exit 1
}


change_and_set_path() {
	cd "$(dirname $0)"

	source path_env
}


# dev mode, using runserver directly
start_dev_server() {
	source "$PROJECT_ROOT_PATH/activate"
	python3 "$DJANGO_PROJECT_PATH/manage.py"  runserver 0:8080
}


# production mode, using gunicorn to manage django website


if (( ! "$#" ));then
	show_usage
else
	change_and_set_path
    case "$1" in
        -dev|--d)
            start_dev_server
            ;;
        -help|--h)
            show_usage
            ;;
		-start)
			;;
		-stop)
			;;
		-status)
			;;
        *)
            show_usage
            ;;
    esac
fi
