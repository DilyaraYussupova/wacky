from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.WidgetCreate.as_view(), name='index'),
    path('delete/<int:pk>', views.widget_delete, name='widget_delete'),
]