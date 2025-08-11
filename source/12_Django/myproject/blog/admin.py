from django.contrib import admin
from blog.models import Post

# Register your models here.
admin.site.register(Post) #admin페이지에서 Post테이블 엑세스 가능