from django import forms
from user.models import User


class UserForm(forms.ModelForm):
    code = forms.CharField(required=True, max_length=4, min_length=4,
                           error_messages={
                                'required': '验证码不能为空',
                                'min_length': '验证码必须是4位',
                                'max_length': '验证码必须是4位'
                           })
    class Meta:
        model = User
        fields = ['code', 'phonenum', 'nickname']
        error_messages = {
            'phonenum': {
                'required': '手机号码不能为空'
            },
            'nickname':{
                'required': '昵称不能为空'
            }
        }




