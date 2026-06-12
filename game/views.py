from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Player
import random
from django.utils import timezone

def click_view(request):
    player = Player.objects.first()

    if request.method == "POST":
        player.points += player.points_per_click
        player.save()
        return redirect('click')

    return render(request, 'game/click.html', {'player': player} )


from django.utils import timezone

def click_ajax(request):
    if request.method == "POST":
        player = Player.objects.first()

        now = timezone.now()
        if player.last_click:
            seconds = int((now - player.last_click).total_seconds())
            player.points += player.points_per_second * seconds
        player.last_click = now

        is_crit = random.randint(1, 100) <= player.crit_chance
        if is_crit:
            gained_points = player.points_per_click * player.crit_multiplier
        else:
            gained_points = player.points_per_click
        player.points += gained_points
        player.save()

        return JsonResponse({
            'points': player.points,
            'points_per_click': player.points_per_click,
            'gained_points': gained_points,
            'is_crit': is_crit,
            'crit_multiplier': player.crit_multiplier,
        })


def buy_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.upgrade_cost:
            player.player_level += 1
            player.points -= player.upgrade_cost
            player.upgrade_level += 1
            player.points_per_click += 1
            player.upgrade_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_level': player.upgrade_level,
            'points_per_click': player.points_per_click,
            'upgrade_cost': player.upgrade_cost
        })


def reset_game(request):
    if request.method == "POST":
        player = Player.objects.first()

        # base stats
        player.player_level = 0
        player.points = 0
        player.points_per_click = 1
        player.upgrade_cost = 10
        player.upgrade_level = 0
        player.luck = 0
        player.upgrade_luck_level = 0
        player.upgrade_luck_cost = 20

        # weapons
        player.wooden_sword_per_click = 3
        player.upgrade_wooden_sword_cost = 100
        player.upgrade_wooden_sword_level = 0

        player.short_sword_per_click = 5
        player.upgrade_short_sword_cost = 500
        player.upgrade_short_sword_level = 0

        player.long_sword_per_click = 10
        player.upgrade_long_sword_cost = 1000
        player.upgrade_long_sword_level = 0

        player.slingshot_per_click = 20
        player.upgrade_slingshot_cost = 2000
        player.upgrade_slingshot_level = 0

        player.bow_per_click = 50
        player.upgrade_bow_cost = 5000
        player.upgrade_bow_level = 0

        player.crossbow_per_click = 100
        player.upgrade_crossbow_cost = 10000
        player.upgrade_crossbow_level = 0

        # crit system
        player.crit_chance = 1
        player.crit_chance_upgrade_cost = 20
        player.upgrade_crit_chance_level = 0

        player.crit_multiplier = 2
        player.crit_multiplier_upgrade_cost = 20
        player.upgrade_crit_multiplier_level = 0

        # auto click
        player.points_per_second = 0
        player.auto_upgrade_cost = 20
        player.upgrade_auto_level = 0

        player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'points_per_click': player.points_per_click,
            'upgrade_cost': player.upgrade_cost,
            'upgrade_level': player.upgrade_level,

            'luck': player.luck,
            'upgrade_luck_level': player.upgrade_luck_level,
            'upgrade_luck_cost': player.upgrade_luck_cost,

            'wooden_sword_per_click': player.wooden_sword_per_click,
            'upgrade_wooden_sword_cost': player.upgrade_wooden_sword_cost,
            'upgrade_wooden_sword_level': player.upgrade_wooden_sword_level,

            'short_sword_per_click': player.short_sword_per_click,
            'upgrade_short_sword_cost': player.upgrade_short_sword_cost,
            'upgrade_short_sword_level': player.upgrade_short_sword_level,

            'long_sword_per_click': player.long_sword_per_click,
            'upgrade_long_sword_cost': player.upgrade_long_sword_cost,
            'upgrade_long_sword_level': player.upgrade_long_sword_level,

            'slingshot_per_click': player.slingshot_per_click,
            'upgrade_slingshot_cost': player.upgrade_slingshot_cost,
            'upgrade_slingshot_level': player.upgrade_slingshot_level,

            'bow_per_click': player.bow_per_click,
            'upgrade_bow_cost': player.upgrade_bow_cost,
            'upgrade_bow_level': player.upgrade_bow_level,

            'crossbow_per_click': player.crossbow_per_click,
            'upgrade_crossbow_cost': player.upgrade_crossbow_cost,
            'upgrade_crossbow_level': player.upgrade_crossbow_level,

            'crit_chance': player.crit_chance,
            'crit_chance_upgrade_cost': player.crit_chance_upgrade_cost,
            'upgrade_crit_chance_level': player.upgrade_crit_chance_level,

            'crit_multiplier': player.crit_multiplier,
            'crit_multiplier_upgrade_cost': player.crit_multiplier_upgrade_cost,
            'upgrade_crit_multiplier_level': player.upgrade_crit_multiplier_level,

            'points_per_second': player.points_per_second,
            'auto_upgrade_cost': player.auto_upgrade_cost,
            'upgrade_auto_level': player.upgrade_auto_level,
        })


def buy_auto_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        success = False

        if player.points >= player.auto_upgrade_cost:
            player.player_level += 1
            player.points -= player.auto_upgrade_cost
            player.upgrade_auto_level += 1
            player.points_per_second += 1
            player.auto_upgrade_cost *= 2
            player.save()
            success = True

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_auto_level': player.upgrade_auto_level,
            'points_per_second': player.points_per_second,
            'auto_upgrade_cost': player.auto_upgrade_cost,
            'success': success
        })

def buy_crit_chance_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.crit_chance_upgrade_cost:
            player.points -= player.crit_chance_upgrade_cost
            player.upgrade_crit_chance_level += 1
            player.crit_chance += 1  # +1%
            player.crit_chance_upgrade_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'upgrade_crit_chance_level': player.upgrade_crit_chance_level,
            'crit_chance': player.crit_chance,
            'crit_chance_upgrade_cost': player.crit_chance_upgrade_cost
        })


def buy_crit_multiplier_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.crit_multiplier_upgrade_cost:
            player.points -= player.crit_multiplier_upgrade_cost
            player.upgrade_crit_multiplier_level += 1
            player.crit_multiplier += 1
            player.crit_multiplier_upgrade_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'crit_multiplier': player.crit_multiplier,
            'upgrade_crit_multiplier_level': player.upgrade_crit_multiplier_level,
            'crit_multiplier_upgrade_cost': player.crit_multiplier_upgrade_cost
        })


def buy_wooden_sword_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 5:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_wooden_sword_cost:
            player.player_level += 1
            player.points -= player.upgrade_wooden_sword_cost
            player.upgrade_wooden_sword_level += 1
            player.points_per_click += 3
            player.upgrade_wooden_sword_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_wooden_sword_level': player.upgrade_wooden_sword_level,
            'points_per_click': player.points_per_click,
            'upgrade_wooden_sword_cost': player.upgrade_wooden_sword_cost
        })

def buy_short_sword_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 10:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_short_sword_cost:
            player.player_level += 1
            player.points -= player.upgrade_short_sword_cost
            player.upgrade_short_sword_level += 1
            player.points_per_click += 5
            player.upgrade_short_sword_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_short_sword_level': player.upgrade_short_sword_level,
            'points_per_click': player.points_per_click,
            'upgrade_short_sword_cost': player.upgrade_short_sword_cost
        })

def buy_long_sword_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 15:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_long_sword_cost:
            player.player_level += 1
            player.points -= player.upgrade_long_sword_cost
            player.upgrade_long_sword_level += 1
            player.points_per_click += 10
            player.upgrade_long_sword_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_long_sword_level': player.upgrade_long_sword_level,
            'points_per_click': player.points_per_click,
            'upgrade_long_sword_cost': player.upgrade_long_sword_cost
        })

def buy_slingshot_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 20:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_slingshot_cost:
            player.player_level += 1
            player.points -= player.upgrade_slingshot_cost
            player.upgrade_slingshot_level += 1
            player.points_per_click += 25
            player.upgrade_slingshot_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_slingshot_level': player.upgrade_slingshot_level,
            'points_per_click': player.points_per_click,
            'upgrade_slingshot_cost': player.upgrade_slingshot_cost
        })

def buy_bow_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 25:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_bow_cost:
            player.player_level += 1
            player.points -= player.upgrade_bow_cost
            player.upgrade_bow_level += 1
            player.points_per_click += 50
            player.upgrade_bow_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_bow_level': player.upgrade_bow_level,
            'points_per_click': player.points_per_click,
            'upgrade_bow_cost': player.upgrade_bow_cost
        })

def buy_crossbow_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 30:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_crossbow_cost:
            player.player_level += 1
            player.points -= player.upgrade_crossbow_cost
            player.upgrade_crossbow_level += 1
            player.points_per_click += 100
            player.upgrade_crossbow_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_crossbow_level': player.upgrade_crossbow_level,
            'points_per_click': player.points_per_click,
            'upgrade_crossbow_cost': player.upgrade_crossbow_cost
        })


def buy_luck_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.upgrade_luck_cost:
            player.points -= player.upgrade_luck_cost
            player.upgrade_luck_level += 1
            player.luck += 1
            player.upgrade_luck_cost *= 3
            player.save()

        return JsonResponse({
            'points': player.points,
            'luck': player.luck,
            'upgrade_luck_level': player.upgrade_luck_level,
            'upgrade_luck_cost': player.upgrade_luck_cost
        })