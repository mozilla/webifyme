Internet Things
===

Firefox Internet Things is a [Django][Django]-based web application...
[Django]: http://www.djangoproject.com/

Getting Started
---
### Python
You need Python 2.6. Also, you probably want to run this application in a
[virtualenv][virtualenv] environment

[virtualenv]: http://pypi.python.org/pypi/virtualenv

### Dependencies
install [beanstalkd][beanstalkd]

Then, run

      easy_install pip

followed by

      ./bootsrap.sh

and spin up beanstalkd

      ./beanstalkd -d -l 10.0.1.5 -p 11300

[beanstalkd]: http://kr.github.com/beanstalkd/

### Django
Put your database and beanstalkd settings and [bitly][bitly] api creds in `settings_local.py`

[bitly]: http://bit.ly/a/account

South is used for migrations, so to sync the db, run

      manage.py syncdb

and to run the migs

      manage.py migrate

then load the fixtures

      manage.py loaddata things/fixtures/*.yaml

then run the image-sizing script - this checks the static/object dirs and updates the images tables with the correct image dimensions

      manage.py set_image_sizes

### Background Tasks
Static collage images are rendered by a (beanstalkd) background job, located at ff4/things/tasks/render.collage.py

This task should be monitored by a tool such as [God][God]. An example God config is included in the project root.

Load and start up God by

     sudo god -c /path/to/god.conf

[God]: https://github.com/mojombo/god



Internationalization
---