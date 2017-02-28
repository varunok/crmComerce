#!/usr/bin/env bash

sites="work6.bizofis.kiev.ua work6.gek.od.ua work6.ofis.dp.ua"

for site in $sites
do
short_name=${site:5}
short_name=${short_name//-/}
short_site=${short_name//./}
echo $site
echo $short_site
cd /hsphere/local/home/image2007/$site/$short_site
source ../data/bin/activate
#pip install django-watson


python manage.py migrate

#python manage.py buildwatson

#ln -s /hsphere/local/home/image2007/crm_rieltor/crm/add_settings.py

deactivate
echo $site' done'

done