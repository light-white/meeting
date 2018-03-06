# meeting
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()
[![Travis](https://img.shields.io/badge/python-3-blue.svg)]()
[![Travis](https://img.shields.io/badge/django-1.10-blue.svg)]()
[![Hex.pm](https://img.shields.io/hexpm/l/plug.svg)]()

# Quickstart



clone 项目到本地  
执行 ```pip install -r requirements.txt```  
根据自己目录配置 ```meeting_uwsgi.ini meeting_uwsgi.conf```  
修改```meeting/settings.py``` 中 DATABASES 中账号密码  
可以参考[Django+uWSGI+Nginx部署Django](http://light-white.me/2017/04/07/Django+uWSGI+nginx/)  

执行```python3 manage.py makemigrations```初始化数据库  
执行```python3 manage.py createsuperuser```创建超级管理员

接下来就可以访问[后台系统](http://localhost/admin)了  
