from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_click = models.DateTimeField(null=True, blank=True)

    points = models.FloatField(default=0.0)

    rebirth = models.IntegerField(default=0)
    rebirth_cost = models.FloatField(default=1000000.0)
    rebirth_gems = models.FloatField(default=0.0)
    
    player_level = models.IntegerField(default=0)
    player_total_clicks = models.IntegerField(default=0)
    player_total_clicks_earned = models.FloatField(default=0.0)
    player_total_crits = models.IntegerField(default=0)
    player_total_crits_earned = models.FloatField(default=0.0)
    player_total_both_earned = models.FloatField(default=0.0)

    luck = models.FloatField(default=0.0)
    upgrade_luck_cost = models.FloatField(default=200.0)
    upgrade_luck_level = models.IntegerField(default=0)

    last_seen = models.DateTimeField(default=timezone.now)
    time_offline = models.IntegerField(default=0)
    upgrade_time_offline_cost = models.FloatField(default=300.0)
    upgrade_time_offline_level = models.IntegerField(default=0)

    shekel_multiplier = models.FloatField(default=1.0)
    upgrade_shekel_multiplier_cost = models.FloatField(default=500.0)
    upgrade_shekel_multiplier_level = models.IntegerField(default=0)

    crit_chance = models.FloatField(default=0.0)
    crit_chance_upgrade_cost = models.FloatField(default=100.0)
    upgrade_crit_chance_level = models.IntegerField(default=0)

    crit_multiplier = models.FloatField(default=2.0)
    crit_multiplier_upgrade_cost = models.FloatField(default=150.0)
    upgrade_crit_multiplier_level = models.IntegerField(default=0)

    tax = models.FloatField(default=0.0)
    upgrade_tax_cost = models.FloatField(default=1000.0)
    upgrade_tax_level = models.IntegerField(default=0)

    anchor = models.FloatField(default=1000.0)
    anchor_click = models.IntegerField(default=100)
    upgrade_anchor_cost = models.FloatField(default=3000.0)
    upgrade_anchor_level = models.IntegerField(default=0)

    dragon_multiplier = models.FloatField(default=1.0)
    upgrade_dragon_multiplier_cost = models.FloatField(default=10000.0)
    upgrade_dragon_multiplier_level = models.IntegerField(default=0)

    # per click
    points_per_click = models.FloatField(default=1.0)

    upgrade_per_click = models.FloatField(default=1.0)
    upgrade_cost = models.FloatField(default=10.0)
    upgrade_level = models.IntegerField(default=0)

    wooden_sword_per_click = models.FloatField(default=3.0)
    upgrade_wooden_sword_cost = models.FloatField(default=100.0)
    upgrade_wooden_sword_level = models.IntegerField(default=0)

    short_sword_per_click = models.FloatField(default=5.0)
    upgrade_short_sword_cost = models.FloatField(default=500.0)
    upgrade_short_sword_level = models.IntegerField(default=0)

    long_sword_per_click = models.FloatField(default=10.0)
    upgrade_long_sword_cost = models.FloatField(default=1000.0)
    upgrade_long_sword_level = models.IntegerField(default=0)

    slingshot_per_click = models.FloatField(default=20.0)
    upgrade_slingshot_cost = models.FloatField(default=2000.0)
    upgrade_slingshot_level = models.IntegerField(default=0)

    bow_per_click = models.FloatField(default=50.0)
    upgrade_bow_cost = models.FloatField(default=5000.0)
    upgrade_bow_level = models.IntegerField(default=0)

    crossbow_per_click = models.FloatField(default=100.0)
    upgrade_crossbow_cost = models.FloatField(default=10000.0)
    upgrade_crossbow_level = models.IntegerField(default=0)

    spear_per_click = models.FloatField(default=200.0)
    upgrade_spear_cost = models.FloatField(default=30000.0)
    upgrade_spear_level = models.IntegerField(default=0)

    shield_per_click = models.FloatField(default=500.0)
    upgrade_shield_cost = models.FloatField(default=50000.0)
    upgrade_shield_level = models.IntegerField(default=0)

    warhammer_per_click = models.FloatField(default=1000.0)
    upgrade_warhammer_cost = models.FloatField(default=100000.0)
    upgrade_warhammer_level = models.IntegerField(default=0)


    # per second 
    points_per_second = models.FloatField(default=0.0)

    auto_per_second = models.FloatField(default=1.0)
    auto_upgrade_cost = models.FloatField(default=20.0)
    upgrade_auto_level = models.IntegerField(default=0)

    drunk_per_second = models.FloatField(default=3.0)
    upgrade_drunk_cost = models.FloatField(default=100.0)
    upgrade_drunk_level = models.IntegerField(default=0)

    maid_per_second = models.FloatField(default=5.0)
    upgrade_maid_cost = models.FloatField(default=500.0)
    upgrade_maid_level = models.IntegerField(default=0)

    groom_per_second = models.FloatField(default=10.0)
    upgrade_groom_cost = models.FloatField(default=2000.0)
    upgrade_groom_level = models.IntegerField(default=0)

    jester_per_second = models.FloatField(default=20.0)
    upgrade_jester_cost = models.FloatField(default=5000.0)
    upgrade_jester_level = models.IntegerField(default=0)

    priest_per_second = models.FloatField(default=40.0)
    upgrade_priest_cost = models.FloatField(default=20000.0)
    upgrade_priest_level = models.IntegerField(default=0)

    archer_per_second = models.FloatField(default=70.0)
    upgrade_archer_cost = models.FloatField(default=50000.0)
    upgrade_archer_level = models.IntegerField(default=0)

    knight_per_second = models.FloatField(default=100.0)
    upgrade_knight_cost = models.FloatField(default=100000.0)
    upgrade_knight_level = models.IntegerField(default=0)

    cavalry_per_second = models.FloatField(default=200.0)
    upgrade_cavalry_cost = models.FloatField(default=400000.0)
    upgrade_cavalry_level = models.IntegerField(default=0)

    architect_per_second = models.FloatField(default=400.0)
    upgrade_architect_cost = models.FloatField(default=1000000.0)
    upgrade_architect_level = models.IntegerField(default=0)

    baron_per_second = models.FloatField(default=700.0)
    upgrade_baron_cost = models.FloatField(default=10000000.0)
    upgrade_baron_level = models.IntegerField(default=0)

    king_per_second = models.FloatField(default=1000.0)
    upgrade_king_cost = models.FloatField(default=30000000.0)
    upgrade_king_level = models.IntegerField(default=0)

    pope_per_second = models.FloatField(default=1500.0)
    upgrade_pope_cost = models.FloatField(default=100000000.0)
    upgrade_pope_level = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Boss(models.Model):
    boss_name = models.CharField(max_length=50, default="Boss")
    boss_max_hp = models.FloatField(default=1000.0)
    boss_hp = models.FloatField(default=1000.0)
    boss_level = models.IntegerField(default=1)
    boss_reward = models.FloatField(default=500.0)
    boss_next_spawn = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("inactive", "Inactive"),
            ("active", "Active"),
            ("dead", "Dead"),
        ],
        default="inactive"
    )
    spawned_at = models.DateTimeField(null=True, blank=True)
    killed_at = models.DateTimeField(null=True, blank=True)


class Monster(models.Model):
    monster_max_hp = models.FloatField(default=50.0)
    monster_hp = models.FloatField(default=50.0)
    monster_name = models.CharField(max_length=50, default="Monster")
    monster_reward = models.FloatField(default=10.0)
    monster_is_alive = models.BooleanField(default=True)
    monster_level = models.IntegerField(default=1)
