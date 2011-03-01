Firefox 4 Internet Things

Setting up a dev environment:

1) Install virtualenv as a system python package however you so choose: http://pypi.python.org/pypi/virtualenv
2) Run bootstrap.sh - This create a virtual environment and installs any requirements, if you write any code that adds additional requirements be sure to update this script
3) Activate the virtualenv like this:
$ source ffenv/bin/activate

4) Create a database
5) Make a copy of settings_local.py.default called settings_local.py and update your database settings
7) Sync your db:
$ python manage.py syncdb
8) Run the migrations
$ python manage.py migrate
9) Load fixtures
$ python manage.py loaddata things/fixtures/*.yaml
10) Run the image-sizing script - this checks the static/object dirs and updates the images tables with the correct image dimensions.
$ python manage.py set_image_sizes
11) Start your dev server:
(ffenv)$ python ff4/manage.py runserver


NOTE: collages are rendered into flat images by ff4/things/tasks/render_collage.py - which needs to be run as a daemonized process, using some kind of process management tool like God (working example God config in the app root)

