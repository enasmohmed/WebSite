"""MyWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Myapp.views import HomePageView, TeamsListView, ScoresListView, PlayerDetailView, TeamDetailView, PlayerListView, \
    AddTeamView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home-page'),
    path('teams/', TeamsListView.as_view(), name='teams-list-view'),
    path('scores/', ScoresListView.as_view(), name='scores-list-view'),
    path('player/<slug>/', PlayerDetailView.as_view(), name='player-detail-view'),
    path('team/<slug>/', TeamDetailView.as_view(), name='team-detail-vie'),
    path('player/', PlayerListView.as_view(), name='player-list-view'),
    path('add_team/', AddTeamView.as_view(), name='add-team-view'),

]
