from django.urls import path
from .views import calorie_calculator_index

app_name = 'calorie_calculator'

urlpatterns = [
    path('', calorie_calculator_index, name='index'),
]
