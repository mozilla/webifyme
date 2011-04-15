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

To install virtualenv (if you don't have it already):

    easy_install virtualenv

And pip (package manager):

    easy_install pip

You will also need RabbitMQ which is the backend for the message queue system:

    sudo [port|apt-get|yum] install rabbitmq-server

Start RabbitMQ:

    sudo rabbitmq-server

Set up a user and vhost:

    sudo rabbitmqctl add_user [USER] [PASS]
    sudo rabbitmqctl add_vhost [VHOST]
    sudo rabbitmqctl set_permissions -p [VHOST] [USER] "" ".*" ".*"

Start and activate the virtualenv:

    virtualenv --distribute --no-site-packages ./ffenv
    source ./ffenv/bin/activate

Prepare you development environment:

    pip install -r requirements/dev.txt -r requirements/compiled.txt

### Setup

Get a username and API key from http://bit.ly/ by signing up and and requesting an API key (http://bit.ly/a/your_api_key)

Now add the settings to settings_local.py (BITLY_USERNAME / BITLY_APIKEY)

Create a database and be sure to note the name then make a copy of settings_local.py.default called settings_local.py and update your database settings

Sync your db:

	python ff4/manage.py syncdb

Run the migrations

    python ff4/manage.py migrate

Then load the fixtures

    python ff4/manage.py loaddata ff4/things/fixtures/*.yaml

Fire up a celery worker:

    python ff4/manage.py celeryd --verbosity=2 --loglevel=DEBUG

Start your dev server:
    python ff4/manage.py runserver



-- tmp --

and spin up beanstalkd (and settings in settings_local_)

      ./beanstalkd -d -l 10.0.1.5 -p 11300

[beanstalkd]: http://kr.github.com/beanstalkd/

### Django
Put your database and beanstalkd settings and [bitly][bitly] api creds in `settings_local.py`

[bitly]: http://bit.ly/a/account

Static collage images are rendered by a (beanstalkd) background job, located at ff4/things/tasks/render.collage.py

This task should be monitored by a tool such as [God][God]. An example God config is included in the project root.

Load and start up God by

     sudo god -c /path/to/god.conf

[God]: https://github.com/mojombo/god

-- tmp


