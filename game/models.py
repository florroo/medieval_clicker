from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_click = models.DateTimeField(null=True, blank=True)

    points = models.IntegerField(default=0)

    points_per_click = models.IntegerField(default=1)
    upgrade_cost = models.IntegerField(default=10)

    crit_chance = models.IntegerField(default=1)
    crit_chance_upgrade_cost = models.IntegerField(default=20)

    crit_multiplier = models.IntegerField(default=2)
    crit_multiplier_upgrade_cost = models.IntegerField(default=20)

    points_per_second = models.IntegerField(default=0)
    auto_upgrade_cost = models.IntegerField(default=20)
    
    def __str__(self):
        return self.user.username

