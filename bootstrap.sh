#/bin/bash
virtualenv --distribute --no-site-packages ./ffenv
source ./ffenv/bin/activate
pip install django==1.2.3
pip install Jinja2
pip install south==0.7.2
pip install django-easymode
pip install PIL
pip install pyyaml
pip install beanstalkc
easy_install http://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.3.tar.gz
easy_install django-dbgettext
