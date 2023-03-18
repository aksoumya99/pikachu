from django.urls import re_path
from rest_framework import routers
from .views import GeneralTaskView, PokemonViewSet, SpecificTaskView, TaskForEmployeeView, ProductivityView


router = routers.DefaultRouter()
router.register(r'^pokemon', PokemonViewSet)

urlpatterns = [
    re_path(r'^task/$', GeneralTaskView.as_view()),
    re_path(r'^task/([0-9]*)/$', SpecificTaskView.as_view()),
    re_path(r'^task_for_employee/([0-9]*)/$', TaskForEmployeeView.as_view()),
    re_path(r'^get_productivity/$', ProductivityView.as_view())
] + router.urls
