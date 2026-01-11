# imports/urls.py
from django.urls import path
from .views import ExcelImportView

urlpatterns = [
    path('excel/', ExcelImportView.as_view()),
]
