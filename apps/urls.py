from django.urls import path

from apps.views import CreateUser

urlpatterns = [
    path('user-create/',CreateUser.as_view(),name='user-create')
]
