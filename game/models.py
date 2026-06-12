from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_click = models.DateTimeField(null=True, blank=True)

    points = models.IntegerField(default=0)
    player_level = models.IntegerField(default=0)

    luck = models.IntegerField(default=0)
    upgrade_luck_cost = models.IntegerField(default=20)
    upgrade_luck_level = models.IntegerField(default=0)

    points_per_click = models.IntegerField(default=1)
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

    crit_chance = models.IntegerField(default=1)
    crit_chance_upgrade_cost = models.IntegerField(default=20)
    upgrade_crit_chance_level = models.IntegerField(default=0)

    crit_multiplier = models.IntegerField(default=2)
    crit_multiplier_upgrade_cost = models.IntegerField(default=20)
    upgrade_crit_multiplier_level = models.IntegerField(default=0)

    points_per_second = models.IntegerField(default=0)
    auto_upgrade_cost = models.IntegerField(default=20)
    upgrade_auto_level = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Boss(models.Model):
    boss_hp = models.IntegerField(default=1000)
    boss_level = models.IntegerField(default=1)
    boss_reward = models.IntegerField(default=500)
    boss_next_spawn = models.DateTimeField(null=True, blank=True)
    boss_active = models.BooleanField(default=False)
