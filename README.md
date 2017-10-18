# flasky

. ./exp.sh
. ./sqlmig.sh

changes in config.py:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = '1306116821' #os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = 'mbbjwtowowstgbej'#os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <1306116821@qq.com>'
	FLASKY_ADMIN = '1306116821@qq.com'#os.environ.get('FLASKY_ADMIN')

for fake articles and users:U
	(venv) $ python manage.py shell
	>>> User.generate_fake(100)
	>>> Post.generate_fake(100)

do it :
	python manage.py runserver --host 0.0.0.0
