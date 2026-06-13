from django.urls import path
from . import views

urlpatterns = [
    path('', views.click_view, name='click'),
    path('click/', views.click_ajax, name='click_ajax'),
    path('reset/', views.reset_game, name='reset_game'),

    # per click
    path('buy/', views.buy_upgrade, name='buy_upgrade'),
    path('buy-wooden-sword/', views.buy_wooden_sword_upgrade, name='buy_wooden_sword_upgrade'),
    path('buy-short-sword/', views.buy_short_sword_upgrade, name='buy_short_sword_upgrade'),
    path('buy-long-sword/', views.buy_long_sword_upgrade, name='buy_long_sword_upgrade'),
    path('buy-slingshot/', views.buy_slingshot_upgrade, name='buy_slingshot_upgrade'),
    path('buy-bow/', views.buy_bow_upgrade, name='buy_bow_upgrade'),
    path('buy-crossbow/', views.buy_crossbow_upgrade, name='buy_crossbow_upgrade'),
    path('buy-spear/', views.buy_spear_upgrade, name='buy_spear_upgrade'),
    path('buy-shield/', views.buy_shield_upgrade, name='buy_shield_upgrade'),
    path('buy-warhammer/', views.buy_warhammer_upgrade, name='buy_warhammer_upgrade'),

    # per second
    path('buy-auto/', views.buy_auto_upgrade, name='buy_auto_upgrade'),
    path('buy-drunk/', views.buy_drunk_upgrade, name='buy_drunk_upgrade'),
    path('buy-maid/', views.buy_maid_upgrade, name='buy_maid_upgrade'),
    path('buy-groom/', views.buy_groom_upgrade, name='buy_groom_upgrade'),
    path('buy-jester/', views.buy_jester_upgrade, name='buy_jester_upgrade'),
    path('buy-priest/', views.buy_priest_upgrade, name='buy_priest_upgrade'),
    path('buy-archer/', views.buy_archer_upgrade, name='buy_archer_upgrade'),
    path('buy-knight/', views.buy_knight_upgrade, name='buy_knight_upgrade'),
    path('buy-cavalry/', views.buy_cavalry_upgrade, name='buy_cavalry_upgrade'),
    path('buy-architect/', views.buy_architect_upgrade, name='buy_architect_upgrade'),
    path('buy-baron/', views.buy_baron_upgrade, name='buy_baron_upgrade'),
    path('buy-king/', views.buy_king_upgrade, name='buy_king_upgrade'),
    path('buy-pope/', views.buy_pope_upgrade, name='buy_pope_upgrade'),

    # upgrades 
    path('buy-crit-chance/', views.buy_crit_chance_upgrade, name='buy_crit_chance_upgrade'),
    path('buy-crit-multiplier/', views.buy_crit_multiplier_upgrade, name='buy_crit_multiplier_upgrade'),
    path('buy-luck/', views.buy_luck_upgrade, name='buy_luck_upgrade'),
    path('buy-time-offline/', views.buy_time_offline_upgrade, name='buy_time_offline_upgrade'),
    path('buy-shekel-multiplier/', views.buy_shekel_multiplier_upgrade, name='buy_shekel_multiplier_upgrade'),

    # path('boss-hit/', views.boss_hit, name='boss_hit'),
]