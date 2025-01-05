from django.urls import path
from .views import IndexView, DetailView

app_name = "OpinionReader"

# these urls come from the tutorial, they're not used anymore.
urlpatterns = [
    #path("main", views.index, name="index"),
    path("", IndexView.as_view(), name="index"),
    # ex: /OpinionViewer/5/
    path("<int:pk>/", DetailView.as_view(), name="detail"),
]