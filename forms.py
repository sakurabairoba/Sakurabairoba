## forms.py 
class QueryUserForm(ModelForm):
    class Meta:
        model = QueryUser
        fields = ['condition', 'queryContent', ]
        # 指定呈现样式字段、指定 CSS 样式
        widgets = {
            'condition': Select(attrs={'class':"form-control",
                                    'title':"query condition",
                                    'name':'condition',
                                    }),
            'queryContent':TextInput(attrs={'class': 'form-control is-invalid',
                                      'name': 'queryContent',
                                      'placeholder': '请输入需要要查询的内容...'
                                      })
        }

        localized = {
            'condition':('username', '用户名'),
            'queryContent':123
        }

        # 自定义错误信息
        error_messages = {
            'queryContent':{
                'required': '查询内容不能为空 !',
            }
        }
