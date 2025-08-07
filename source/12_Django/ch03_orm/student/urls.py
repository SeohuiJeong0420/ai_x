from django.urls import path, register_converter
from . import views
from .converters import IdConverter
app_name="student"
register_converter(IdConverter, 'dddd')
urlpatterns = [
    path("", views.list, name="list"),
    path("get/<dddd:id>", views.get, name="get"),
    path("del/<int:id>", views.delete, name="del")
]