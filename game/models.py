from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_click = models.DateTimeField(null=True, blank=True)

    points = models.IntegerField(default=0)
    player_rebirth = models.IntegerField(default=0)
    player_rebirth_cost = models.IntegerField(default=1000000)
    player_level = models.IntegerField(default=0)

    luck = models.IntegerField(default=0)
    upgrade_luck_cost = models.IntegerField(default=200)
    upgrade_luck_level = models.IntegerField(default=0)

    last_seen = models.DateTimeField(default=timezone.now)
    time_offline = models.IntegerField(default=0)
    upgrade_time_offline_cost = models.IntegerField(default=300)
    upgrade_time_offline_level = models.IntegerField(default=0)

    shekel_multiplier = models.FloatField(default=1.0)
    upgrade_shekel_multiplier_cost = models.IntegerField(default=500)
    upgrade_shekel_multiplier_level = models.IntegerField(default=0)

    crit_chance = models.IntegerField(default=1)
    crit_chance_upgrade_cost = models.IntegerField(default=100)
    upgrade_crit_chance_level = models.IntegerField(default=0)

    crit_multiplier = models.IntegerField(default=2)
    crit_multiplier_upgrade_cost = models.IntegerField(default=150)
    upgrade_crit_multiplier_level = models.IntegerField(default=0)


    # per click
    points_per_click = models.IntegerField(default=1)

    upgrade_per_click = models.IntegerField(default=1)
    upgrade_cost = models.IntegerField(default=10)
    upgrade_level = models.IntegerField(default=0)

    wooden_sword_per_click = models.IntegerField(default=3)
    upgrade_wooden_sword_cost = models.IntegerField(default=100)
    upgrade_wooden_sword_level = models.IntegerField(default=0)

    short_sword_per_click = models.IntegerField(default=5)
    upgrade_short_sword_cost = models.IntegerField(default=500)
    upgrade_short_sword_level = models.IntegerField(default=0)

    long_sword_per_click = models.IntegerField(default=10)
    upgrade_long_sword_cost = models.IntegerField(default=1000)
    upgrade_long_sword_level = models.IntegerField(default=0)

    slingshot_per_click = models.IntegerField(default=20)
    upgrade_slingshot_cost = models.IntegerField(default=2000)
    upgrade_slingshot_level = models.IntegerField(default=0)

    bow_per_click = models.IntegerField(default=50)
    upgrade_bow_cost = models.IntegerField(default=5000)
    upgrade_bow_level = models.IntegerField(default=0)

    crossbow_per_click = models.IntegerField(default=100)
    upgrade_crossbow_cost = models.IntegerField(default=10000)
    upgrade_crossbow_level = models.IntegerField(default=0)

    spear_per_click = models.IntegerField(default=200)
    upgrade_spear_cost = models.IntegerField(default=30000)
    upgrade_spear_level = models.IntegerField(default=0)

    shield_per_click = models.IntegerField(default=500)
    upgrade_shield_cost = models.IntegerField(default=50000)
    upgrade_shield_level = models.IntegerField(default=0)

    warhammer_per_click = models.IntegerField(default=1000)
    upgrade_warhammer_cost = models.IntegerField(default=100000)
    upgrade_warhammer_level = models.IntegerField(default=0)


    # per second 
    points_per_second = models.IntegerField(default=0)

    auto_per_second = models.IntegerField(default=1)
    auto_upgrade_cost = models.IntegerField(default=20)
    upgrade_auto_level = models.IntegerField(default=0)

    drunk_per_second = models.IntegerField(default=3)
    upgrade_drunk_cost = models.IntegerField(default=100)
    upgrade_drunk_level = models.IntegerField(default=0)

    maid_per_second = models.IntegerField(default=3)
    upgrade_maid_cost = models.IntegerField(default=100)
    upgrade_maid_level = models.IntegerField(default=0)

    groom_per_second = models.IntegerField(default=3)
    upgrade_groom_cost = models.IntegerField(default=100)
    upgrade_groom_level = models.IntegerField(default=0)

    jester_per_second = models.IntegerField(default=3)
    upgrade_jester_cost = models.IntegerField(default=100)
    upgrade_jester_level = models.IntegerField(default=0)

    priest_per_second = models.IntegerField(default=3)
    upgrade_priest_cost = models.IntegerField(default=100)
    upgrade_priest_level = models.IntegerField(default=0)

    archer_per_second = models.IntegerField(default=3)
    upgrade_archer_cost = models.IntegerField(default=100)
    upgrade_archer_level = models.IntegerField(default=0)

    knight_per_second = models.IntegerField(default=3)
    upgrade_knight_cost = models.IntegerField(default=100)
    upgrade_knight_level = models.IntegerField(default=0)

    cavalry_per_second = models.IntegerField(default=3)
    upgrade_cavalry_cost = models.IntegerField(default=100)
    upgrade_cavalry_level = models.IntegerField(default=0)

    architect_per_second = models.IntegerField(default=3)
    upgrade_architect_cost = models.IntegerField(default=100)
    upgrade_architect_level = models.IntegerField(default=0)

    baron_per_second = models.IntegerField(default=3)
    upgrade_baron_cost = models.IntegerField(default=100)
    upgrade_baron_level = models.IntegerField(default=0)

    king_per_second = models.IntegerField(default=3)
    upgrade_king_cost = models.IntegerField(default=100)
    upgrade_king_level = models.IntegerField(default=0)

    pope_per_second = models.IntegerField(default=3)
    upgrade_pope_cost = models.IntegerField(default=100)
    upgrade_pope_level = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Boss(models.Model):
    boss_name = models.CharField(max_length=50, default="Boss")
    boss_max_hp = models.IntegerField(default=1000)
    boss_hp = models.IntegerField(default=1000)
    boss_level = models.IntegerField(default=1)
    boss_reward = models.IntegerField(default=500)
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
    monster_max_hp = models.IntegerField(default=50)
    monster_hp = models.IntegerField(default=50)
    monster_name = models.CharField(max_length=50, default="Monster")
    monster_reward = models.IntegerField(default=10)
    monster_is_alive = models.BooleanField(default=True)
    monster_level = models.IntegerField(default=1)
