##
# Build SASS
##
sass:
	sass --style compressed --update static/css/

##
# For dokku - build sass and run gunicorn
##
dokku-start: sass run-gunicorn

##
# Run the gunicorn app
##
run-gunicorn:
	gunicorn webapp.wsgi
