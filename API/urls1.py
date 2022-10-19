from django.urls import path

from API import views

urlpatterns = [
    
    #127.0.0.1:8000/API/
    path('',views.index),

    #127.0.0.1:8000/API/5/
    path('<int:question_id>/',views.detail),

    #127.0.0.1:8000/API/5/results/
    path("<int:question_id>/results/", views.results),

    #127.0.0.1:8000/API/5/vote/
    path("<int:question_id>/vote/",views.vote),


]