from django.urls import path

from .views import JutyuListView, add_jutyu

urlpatterns = [
    path('', JutyuListView.as_view(), name='jutyu_list'),
    path('add/', add_jutyu, name='add_jutyu'),
]
