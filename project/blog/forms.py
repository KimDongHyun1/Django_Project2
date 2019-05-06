from django import forms
from .models import Blog

# 이거를 만드는 이유는 Blog라는 class를 활용하기 위해 new.html같은 것을 만드는 작업을 덜어주기 위함이다. (반복 / 재사용 가능할 수 있게 하기위해)

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']