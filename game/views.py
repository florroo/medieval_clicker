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
            player.points -= player.upgrade_cost
            player.points_per_click += 1
            player.upgrade_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'points_per_click': player.points_per_click,
            'upgrade_cost': player.upgrade_cost
        })


def reset_game(request):
    if request.method == "POST":
        player = Player.objects.first()

        player.points  = 0
        player.points_per_click = 1
        player.upgrade_cost = 10
        player.points_per_second = 0
        player.auto_upgrade_cost = 20
        player.crit_chance = 1
        player.crit_chance_upgrade_cost = 20
        player.crit_multiplier = 2
        player.crit_multiplier_upgrade_cost = 20
        player.save()

        return JsonResponse({
            'points': player.points,
            'points_per_click': player.points_per_click,
            'upgrade_cost': player.upgrade_cost,
            'auto_upgrade_cost': player.auto_upgrade_cost,
            'points_per_second': player.points_per_second,
            'crit_chance': player.crit_chance,
            'crit_chance_upgrade_cost': player.crit_chance_upgrade_cost,
            'crit_multiplier': player.crit_multiplier,
            'crit_multiplier_upgrade_cost': player.crit_multiplier_upgrade_cost,
        })


def buy_auto_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        success = False

        if player.points >= player.auto_upgrade_cost:
            player.points -= player.auto_upgrade_cost
            player.points_per_second += 1
            player.auto_upgrade_cost *= 2
            player.save()
            success = True

        return JsonResponse({
            'points': player.points,
            'points_per_second': player.points_per_second,
            'auto_upgrade_cost': player.auto_upgrade_cost,
            'success': success
        })

def buy_crit_chance_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.crit_chance_upgrade_cost:
            player.points -= player.crit_chance_upgrade_cost

            player.crit_chance += 1  # +1%

            player.crit_chance_upgrade_cost *= 2

            player.save()

        return JsonResponse({
            'points': player.points,
            'crit_chance': player.crit_chance,
            'crit_chance_upgrade_cost': player.crit_chance_upgrade_cost
        })


def buy_crit_multiplier_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.crit_multiplier_upgrade_cost:
            player.points -= player.crit_multiplier_upgrade_cost

            player.crit_multiplier += 1

            player.crit_multiplier_upgrade_cost *= 2

            player.save()

        return JsonResponse({
            'points': player.points,
            'crit_multiplier': player.crit_multiplier,
            'crit_multiplier_upgrade_cost': player.crit_multiplier_upgrade_cost
        })