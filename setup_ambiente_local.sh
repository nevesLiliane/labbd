#!/bin/sh

#./erase_and_first_config_monet_db.sh;

sudo apt-get install python3-pip python3-dev python-virtualenv redis-server;

virtualenv --system-site-packages -p python3 $env;

./$env/bin/easy_install -U pip;

sudo -H ./$env/bin/pip3 install -r $requirements.txt;
