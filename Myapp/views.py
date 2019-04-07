import data as data
from django.db import IntegrityError
from django.forms import models, ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from post import POST

import Myapp
from Myapp.forms import TeamModelForm, TeamForm, ScoreModelForm
from Myapp.models import Team, GameScore, Player


class HomePageView(View):
    def get(self, request):
        all_team = Team.objects.all()
        context = {'teams': all_team}
        return render(request, 'team_list.html', context)


class TeamsListView(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'


class ScoresListView(ListView):
    model = GameScore
    template_name = 'score_list.html'
    context_object_name = 'scores'

    def get_context_data(self, **kwargs):
        context = super(ScoresListView, self).get_context_data(**kwargs)
        context['form'] = ScoreModelForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ScoreModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/scores/')


class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'
    slug_field = 'name'


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player_detail.html'
    context_object_name = 'player'
    slug_field = 'name'


class PlayerListView(ListView):
    model = Player
    template_name = 'player_list.html'
    context_object_name = 'player'


class AddTeamView(View):
    def get(self, request):
        form = TeamModelForm()
        context = {'form': form}
        return render(request,'add_team.html', context)

    def post(self, request):
        form = TeamModelForm(request.POST)
        if form.is_valid():
            Myapp = Team()
            Myapp.save()
            return redirect('/')
        else:
            context ={'form': form}
            return render(request,'add_team.html', context)

