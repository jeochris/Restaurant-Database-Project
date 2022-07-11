from django.urls import path, include
from dsl_app import views

app_name = 'dsl_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('register/', views.register)
]