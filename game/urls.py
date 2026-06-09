from django.urls import path
from . import views

urlpatterns = [
    path('', views.click_view, name='click'),
    path('click/', views.click_ajax, name='click_ajax'),
    path('buy/', views.buy_upgrade, name='buy_upgrade'),
    path('reset/', views.reset_game, name='reset_game'),
    path('buy-auto/', views.buy_auto_upgrade, name='buy_auto_upgrade'),
    path('buy-crit-chance/', views.buy_crit_chance_upgrade, name='buy_crit_chance_upgrade'),
    path('buy-crit-multiplier/', views.buy_crit_multiplier_upgrade, name='buy_crit_multiplier_upgrade'),
]