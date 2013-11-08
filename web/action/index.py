# -*- coding:utf-8 -*- 
"""
    author comger@gmail.com
    migrant 前端展示公共页面
"""
from kpages import url
from kpages.context import get_context
from utility import BaseHandler


@url(r'/?')
class Index(BaseHandler):
    def get(self):
        self.render('action/index.html')


@url(r'/login?')
class Login(BaseHandler):
    def get(self):
        self.render('action/login.html')


@url(r'/logout?')
class Logout(BaseHandler):
    def get(self):
        self.clear_cookie('uid')
        self.clear_cookie('city')
        self.redirect('/')


@url(r'/profile?')
class Profile(BaseHandler):
    def get(self):
        self.render('action/profile.html')


@url(r'/setpwd?')
class SetPwd(BaseHandler):
    def get(self):
        self.render('action/setpwd.html')


@url(r'/forgot_password?')
@url(r'/forgot_password/(.*)')
class SetPwd(BaseHandler):
    def get(self, key=None):
        if not key:
            self.render('action/forget_password.html')
        else:
            with get_context() as context:
                redis = context.get_redis()
                username = redis.get(key)
                if username:
                    self.render('action/xxxx.html', username=username)
                else:
                    self.render('action/xxxx.html', username=username)