from django.urls import path
from . import views

urlpatterns = [
    path('', views.click_view, name='click'),
    path('click/', views.click_ajax, name='click_ajax'),
    path('buy/', views.buy_upgrade, name='buy_upgrade'),
    path('reset/', views.reset_game, name='reset_game'),
    path('buy-wooden-sword/', views.buy_wooden_sword_upgrade, name='buy_wooden_sword_upgrade'),
    path('buy-short-sword/', views.buy_short_sword_upgrade, name='buy_short_sword_upgrade'),
    path('buy-long-sword/', views.buy_long_sword_upgrade, name='buy_long_sword_upgrade'),
    path('buy-slingshot/', views.buy_slingshot_upgrade, name='buy_slingshot_upgrade'),
    path('buy-bow/', views.buy_bow_upgrade, name='buy_bow_upgrade'),
    path('buy-crossbow/', views.buy_crossbow_upgrade, name='buy_crossbow_upgrade'),
    path('buy-auto/', views.buy_auto_upgrade, name='buy_auto_upgrade'),
    path('buy-crit-chance/', views.buy_crit_chance_upgrade, name='buy_crit_chance_upgrade'),
    path('buy-crit-multiplier/', views.buy_crit_multiplier_upgrade, name='buy_crit_multiplier_upgrade'),
    path('buy-luck/', views.buy_luck_upgrade, name='buy_luck_upgrade'),
    
    # path('boss-hit/', views.boss_hit, name='boss_hit'),
]