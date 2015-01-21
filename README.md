###Description
Simple site is written on Django with caching views, js sliders, PSQL DB and WYSIWYG-redactor in admin for easily adding content.

###Tech Stack
* Django as framework on backend
* Redis for caching
* jQuery + skel for the frontend
* Standard nginx + uwsgi + django + postgresql stack used for production.

###Requirements
* Python 2.7.x
* Django>=1.7
* django-redis-cache==0.13.0
* django-wysiwyg-redactor==0.4.4.1
* Pillow==2.7.0
* psycopg2==2.5.4
* redis==2.10.3
* uWSGI==2.0.9

after you get the project up you can use pip to install this:
```sh
pip install -r requirements.txt
```

You can look this [site].

[site]:http://eventcreative.org
