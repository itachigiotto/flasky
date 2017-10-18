#工程中关于用户权限的分析
##本次问题主要出在关于默认用户的Post权限和command权限

##全部信息在/app/models.py中
```python

/app
    /models.py
        class Permission
        class Role 角色类
            #def insert_roles()#插入角色
        class User
            #def __init__(self, **kwargs)#初始化用户并判断权限
            #def can(self, permissions)#对某一用户判断权限
            #def is_administrator(self)#判断某一用户是否为管理员
        class AnonymousUser(AnonymousUserMixin)
            #def can(self, permissions)#对匿名角色判断权限
            #def is_administrator(self)#对匿名角色判断是否为管理员
        login_manager.anonymous_user = AnonymousUser#
    /decorators.py
        

```
