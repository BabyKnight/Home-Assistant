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
production_server() {
	source "$PROJECT_ROOT_PATH/activate"
	gunicorn  assistant.wsgi:application --chdir "$DJANGO_PROJECT_PATH" --bind 0.0.0.0:8080
}


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
		-start|-stop|-status)
			production_server
			;;
        *)
			echo "Invalid arguments"
            show_usage
            ;;
    esac
fi
