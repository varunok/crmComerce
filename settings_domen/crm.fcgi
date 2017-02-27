#!/hsphere/local/home/image2007/site/data/bin/python
import sys, os
 
# Add a custom Python path.
sys.path.insert(0, "/hsphere/local/home/image2007/site/crm")
#sys.path.append("/usr/lib/python2.7/site-packages")
#sys.path.append("/hsphere/local/home/image2007/dom6.dom.zt.ua/data/crm/lib/python2.7")
 
# Switch to the directory of your project. (Optional.)
# os.chdir("/hsphere/local/home/username/usersite.com/mysite")
 
# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "crm.settings"
 
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="prefork", daemonize="false", minspare=1, maxspare=1, maxchildren=1)
