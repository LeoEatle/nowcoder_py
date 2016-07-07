#this file use encoding: utf-8
from flask_script import Manager
from c2 import app

#将系统和脚本分开来
manager = Manager(app)

@manager.option('--n', '--name', dest= 'name', default = "LeoEatle")
def hello(name):
    print 'hello', name


@manager.command
def initiallize_database():
    'initialize database'


