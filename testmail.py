#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from flask import Flask 
from flask_mail import Mail, Message 

app = Flask(__name__) 
app.config['MAIL_SERVER'] = 'smtp.qq.com' 
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USE_SSL'] = True 
app.config['MAIL_USERNAME'] = '1306116821' 
app.config['MAIL_PASSWORD'] = 'mbbjwtowowstgbej' 

mail = Mail(app) 
msg = Message('test subject', sender='1306116821@qq.com',recipients=['1306116827@qq.com']) 
msg.body = 'tesadas'
with app.app_context(): 
	mail.send(msg)
