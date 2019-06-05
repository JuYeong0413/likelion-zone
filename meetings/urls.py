from django.urls import path
from . import views

app_name="meetings"
urlpatterns = [
    path('list/', views.list, name="list"),
    path('<int:id>/', views.read, name="read"),
    path('create/', views.create, name="create"),
    path('verification/', views.verification, name="verification"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    # path('search_result/', views.search_result, name="search_result"),
    path('', views.search, name ="search"),
    path('join_page/<int:id>/', views.join_page, name="join_page"),
    path('join/<int:id>/', views.join, name="join"),
    path('participants/<int:id>/', views.participants, name="participants"),
    path('joined_meetings/', views.joined_meetings, name="joined_meetings"),
    path('fail/', views.fail, name ="fail"),
    path('check_pwd/', views.check_pwd, name="check_pwd"),
    path('delete/<int:id>/', views.delete, name="delete"),
    # path('show/', views.show, name ="show"),
    path('board/', views.board, name ="board"),
]