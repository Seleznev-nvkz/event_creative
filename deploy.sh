#!/bin/bash
branch=${$1:-master}
git pull origin $1
if ! [ -e '/etc/uwsgi/apps-enabled/event_creative.ini' ]; then
	cp -f conf/event_creative.ini /etc/uwsgi/apps-available/
	ln -sf /etc/uwsgi/apps-available/event_creative.ini /etc/uwsgi/apps-enabled/event_creative.ini
fi
uwsgi --ini /etc/uwsgi/apps-enabled/event_creative.ini
# service nginx restart
redis-cli flushall
