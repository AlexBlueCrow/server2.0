from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'getItem/$', views.get_item),
    url(r'getUserInfo', views.get_userInfo),
    url(r'pay_feedback', views.pay_feedback),
    url(r'payOrder/$', views.payOrder),
    url(r'getComments/', views.get_comments),
    url(r'postComment/', views.post_comment),
    url(r'weChatPay/', views.weChatPay),
    url(r'getFarmInfo/', views.get_farmInfo),
    url(r'getOrderInfo/', views.get_orderInfo),
    url(r'updateUser/', views.updateUser),
    url(r'allorder/', views.allorder),
    url(r'getCaptains/', views.getCaptains),
    url(r'cap_apply/', views.cap_apply),
    url(r'is_captain/', views.is_captain),
]
