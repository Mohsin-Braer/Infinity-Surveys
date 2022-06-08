from django.urls import path 
from . import views
from teamcreation import views as v1


urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"), 
    path("view/", views.view, name="view"), 
    path("PAresponse/", views.PAresponse, name = "test")
    #path("dashboard/", views.all_teams, name = "team_list"),
]

