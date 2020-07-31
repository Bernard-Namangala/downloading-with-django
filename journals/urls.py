from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('download/<int:journal_id>/', views.download_journal)
]
