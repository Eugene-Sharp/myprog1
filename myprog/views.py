﻿from django.views.generic import View
from django.shortcuts import render 

class Index(View):
    def get(self, request): 
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
		
class Profile(View):
    """User Profile page reachable from /user/<username> URL""" 
    def get(self, request, username):
        params = dict()
        user = User.objects.get (username=usemame) 
        tweets = Tweet.objects.filter(user=user) 
        params["tweets"] = tweets 
        params["user"] = user
        return render(request, 'profile.html', params)
