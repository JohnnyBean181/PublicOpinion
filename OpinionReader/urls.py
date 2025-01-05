from django.urls import path

app_name = "OpinionReader"

# these urls come from the tutorial, they're not used anymore.
tutorial_url = [
    #path("main", views.index, name="index"),
    path("main/", t_views.IndexView.as_view(), name="index"),
]