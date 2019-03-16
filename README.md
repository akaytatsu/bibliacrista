#Passo a Passo

### Instando Apache

### Download apache windows

executar comando:

* httpd.exe -k install -n "Apache HTTP Server"

achar a versão em https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi
baixar e executar pip install "nome_arquivo.whl" 

executar:

set MOD_WSGI_APACHE_ROOTDIR = c:/chronun/Apache24
mod_wsgi-express module-config

copy content to httpd.cfg apache

httpd.cfg

LoadFile "c:/users/thiago/appdata/local/programs/python/python37/python37.dll"
LoadModule wsgi_module "c:/users/thiago/appdata/local/programs/python/python37/lib/site-packages/mod_wsgi/server/mod_wsgi.cp37-win_amd64.pyd"
WSGIPythonHome "c:/users/thiago/appdata/local/programs/python/python37"

Alias /media/ C:/chronun/vexmid/backend/media/
Alias /static/ C:/chronun/vexmid/backend/static_files/

<Directory C:/chronun/vexmid/backend/static_files>
Require all granted
</Directory>

<Directory C:/chronun/vexmid/backend/media>
Require all granted
</Directory>

WSGIScriptAlias / c:/chronun/vexmid/backend/conf/wsgi.py
WSGIPythonHome c:/chronun/vexmid_venv
WSGIPythonPath c:/chronun/vexmid/backend

<Directory c:/chronun/vexmid/backend>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
criar python path

PYTHONPATH = C:\Users\Thiago\AppData\Local\Programs\Python\Python37;C:\Users\Thiago\AppData\Local\Programs\Python\Python37\Lib;C:\Users\Thiago\AppData\Local\Programs\Python\Python37\Scripts;C:\Users\Thiago\AppData\Local\Programs\Python\Python37\DLLs

WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py
WSGIPythonHome /path/to/venv
WSGIPythonPath /path/to/mysite.com

<Directory /path/to/mysite.com/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

### Sincronização VTEX

Após instalar, executar os seguintes passos:

* python manage.py protheus_sync_all
* ativar uma tabela de preços
* python manage.py vtex_pull_all
* python manage.py protheus_sync_protheus_vexmid