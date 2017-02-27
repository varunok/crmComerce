
sites="dom6.neruhomist.volyn.ua dom6.gek.cv.ua dom6.gek.kr.ua dom6.bizflat.kiev.ua dom6.domgomel.by dom6.bizflat.kz dom6.batysdom.kz dom6.hata.km.ua dom6.dom-alexandria.kr.ua dom6.xata.dp.ua dom6.dom.zt.ua dom6.usatba-krm.dn.ua"

for site in sites
do
short_site=${site:4}
short_site=${short_name//./}
cd /hsphere/local/home/image2007/$site/$short_site
source ../data/bin/activate

python manage.py makemigrations arendator
python manage.py makemigrations backupbd_crm
python manage.py makemigrations buyer
python manage.py makemigrations extuser
python manage.py makemigrations facility
python manage.py makemigrations homes
python manage.py makemigrations learning
python manage.py makemigrations makler
python manage.py makemigrations meeting
python manage.py makemigrations notes
python manage.py makemigrations parsings
python manage.py makemigrations posting
python manage.py makemigrations searching
python manage.py makemigrations send_messege_user
python manage.py makemigrations sender_email
python manage.py makemigrations setting_globall
python manage.py makemigrations setting_street
python manage.py makemigrations setting_superadmin
python manage.py makemigrations setting_mail_delivery
python manage.py makemigrations single_arendator
python manage.py makemigrations single_buyer
python manage.py makemigrations single_object
python manage.py makemigrations tasking
python manage.py makemigrations trash_object
python manage.py makemigrations watermark
python manage.py makemigrations who_online


python manage.py migrate arendator --fake
python manage.py migrate backupbd_crm --fake
python manage.py migrate buyer --fake
python manage.py migrate extuser --fake
python manage.py migrate facility --fake
python manage.py migrate homes --fake
python manage.py migrate learning --fake
python manage.py migrate makler --fake
python manage.py migrate meeting --fake
python manage.py migrate notes --fake
python manage.py migrate parsings --fake
python manage.py migrate posting --fake
python manage.py migrate searching --fake
python manage.py migrate send_messege_user --fake
python manage.py migrate sender_email --fake
python manage.py migrate setting_globall --fake
python manage.py migrate setting_street --fake
python manage.py migrate setting_superadmin --fake
python manage.py migrate setting_mail_delivery --fake
python manage.py migrate single_arendator --fake
python manage.py migrate single_buyer --fake
python manage.py migrate single_object --fake
python manage.py migrate tasking --fake
python manage.py migrate trash_object --fake
python manage.py migrate watermark --fake
python manage.py migrate who_online --fake

done