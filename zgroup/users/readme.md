# User模型

User继承了django内置的AbstractUser模型

AbstractUser包括了以下属性：
- username
- password
- email
- first_name
- last_name

# 注册
内置注册表单：django.contrib.auth.forms.UserCreationForm

在其内部类Meta中的model指定该表单关联的模型

```python
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email"]

```

fields指定表单提交的哪些字段，其中username,password是默认存在的

# 登陆
django内置登陆功能，以下是url规则

    path('login/')
    path('logout/'),
    path('password_change/'),
    path('password_change/done/'),
    path('password_reset/'),
    path('password_reset/done/'),
    path('reset/<uidb64>/<token>/),
    path('reset/done/'),