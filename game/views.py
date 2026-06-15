from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Player
import random
from django.db import transaction
from django.contrib import messages
from django.utils import timezone

def click_view(request):
    with transaction.atomic():
        player = Player.objects.select_for_update().first()
        now = timezone.now()
        earned = 0
        offline_minutes = 0
        if player.last_seen:
            offline_seconds = (now - player.last_seen).total_seconds()
            max_seconds = player.time_offline * 3600
            offline_seconds = min(offline_seconds, max_seconds)
            earned = offline_seconds * player.points_per_second
            earned *= player.shekel_multiplier
            earned = round(earned, 2)
            offline_minutes = int(offline_seconds // 60)
            player.points += earned
        player.last_seen = now
        player.last_click = now
        player.save()

    return render(request, 'game/click.html', {
        'player': player,
        'offline_earned': earned,
        'offline_minutes': offline_minutes,
    })

def click_ajax(request):
    if request.method == "POST":
        with transaction.atomic():
            player = Player.objects.select_for_update().first()
            now = timezone.now()
            if player.last_click:
                seconds = int((now - player.last_click).total_seconds())
                if player.time_offline > 0:
                    max_seconds = player.time_offline * 3600
                    seconds = min(seconds, max_seconds)
                else:
                    seconds = 0

                gained_afk = player.points_per_second * seconds
                gained_afk *= player.shekel_multiplier
                player.points += gained_afk

            player.last_click = now

            is_crit = random.randint(1, 100) <= player.crit_chance
            if is_crit:
                gained_points = player.points_per_click * player.crit_multiplier
                gained_points *= player.shekel_multiplier
                player.player_total_crits += 1
                player.player_total_crits_earned += gained_points
            else:
                gained_points = player.points_per_click
                gained_points *= player.shekel_multiplier
                player.player_total_clicks_earned += gained_points

            player.points += gained_points
            player.last_seen = timezone.now()

            player.player_total_clicks += 1
            player.player_total_both_earned += gained_points

            player.save()

        return JsonResponse({
            'points': player.points,
            'points_per_click': player.points_per_click,
            'gained_points': gained_points,
            'is_crit': is_crit,
            'crit_multiplier': player.crit_multiplier,
        })


def get_stats(request):
    player = Player.objects.first()
    return JsonResponse({
        'player_total_clicks': player.player_total_clicks,
        'player_total_clicks_earned': player.player_total_clicks_earned,
        'player_total_crits': player.player_total_crits,
        'player_total_crits_earned': player.player_total_crits_earned,
        'player_total_both_earned': player.player_total_both_earned,
    })


def buy_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.upgrade_cost:
            player.player_level += 1
            player.points -= player.upgrade_cost
            player.upgrade_level += 1
            player.points_per_click += player.upgrade_per_click
            player.upgrade_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_level': player.upgrade_level,
            'points_per_click': player.points_per_click,
            'upgrade_cost': player.upgrade_cost
        })

def buy_drunk_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 5:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_drunk_cost:
            player.player_level += 1
            player.points -= player.upgrade_drunk_cost
            player.upgrade_drunk_level += 1
            player.points_per_second += player.drunk_per_second
            player.upgrade_drunk_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_drunk_level': player.upgrade_drunk_level,
            'points_per_second': player.points_per_second,
            'upgrade_drunk_cost': player.upgrade_drunk_cost
        })

def buy_maid_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 10:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_maid_cost:
            player.player_level += 1
            player.points -= player.upgrade_maid_cost
            player.upgrade_maid_level += 1
            player.points_per_second += player.maid_per_second
            player.upgrade_maid_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_maid_level': player.upgrade_maid_level,
            'points_per_second': player.points_per_second,
            'upgrade_maid_cost': player.upgrade_maid_cost
        })


def buy_groom_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 15:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_groom_cost:
            player.player_level += 1
            player.points -= player.upgrade_groom_cost
            player.upgrade_groom_level += 1
            player.points_per_second += player.groom_per_second
            player.upgrade_groom_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_groom_level': player.upgrade_groom_level,
            'points_per_second': player.points_per_second,
            'upgrade_groom_cost': player.upgrade_groom_cost
        })

def buy_jester_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 20:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_jester_cost:
            player.player_level += 1
            player.points -= player.upgrade_jester_cost
            player.upgrade_jester_level += 1
            player.points_per_second += player.jester_per_second
            player.upgrade_jester_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_jester_level': player.upgrade_jester_level,
            'points_per_second': player.points_per_second,
            'upgrade_jester_cost': player.upgrade_jester_cost
        })

def buy_priest_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 30:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_priest_cost:
            player.player_level += 1
            player.points -= player.upgrade_priest_cost
            player.upgrade_priest_level += 1
            player.points_per_second += player.priest_per_second
            player.upgrade_priest_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_priest_level': player.upgrade_priest_level,
            'points_per_second': player.points_per_second,
            'upgrade_priest_cost': player.upgrade_priest_cost
        })

def buy_archer_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 40:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_archer_cost:
            player.player_level += 1
            player.points -= player.upgrade_archer_cost
            player.upgrade_archer_level += 1
            player.points_per_second += player.archer_per_second
            player.upgrade_archer_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_archer_level': player.upgrade_archer_level,
            'points_per_second': player.points_per_second,
            'upgrade_archer_cost': player.upgrade_archer_cost
        })


def buy_knight_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 50:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_knight_cost:
            player.player_level += 1
            player.points -= player.upgrade_knight_cost
            player.upgrade_knight_level += 1
            player.points_per_second += player.knight_per_second
            player.upgrade_knight_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_knight_level': player.upgrade_knight_level,
            'points_per_second': player.points_per_second,
            'upgrade_knight_cost': player.upgrade_knight_cost
        })

def buy_cavalry_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 60:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_cavalry_cost:
            player.player_level += 1
            player.points -= player.upgrade_cavalry_cost
            player.upgrade_cavalry_level += 1
            player.points_per_second += player.cavalry_per_second
            player.upgrade_cavalry_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_cavalry_level': player.upgrade_cavalry_level,
            'points_per_second': player.points_per_second,
            'upgrade_cavalry_cost': player.upgrade_cavalry_cost
        })

def buy_architect_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 70:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_architect_cost:
            player.player_level += 1
            player.points -= player.upgrade_architect_cost
            player.upgrade_architect_level += 1
            player.points_per_second += player.architect_per_second
            player.upgrade_architect_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_architect_level': player.upgrade_architect_level,
            'points_per_second': player.points_per_second,
            'upgrade_architect_cost': player.upgrade_architect_cost
        })


def buy_baron_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 80:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_baron_cost:
            player.player_level += 1
            player.points -= player.upgrade_baron_cost
            player.upgrade_baron_level += 1
            player.points_per_second += player.baron_per_second
            player.upgrade_baron_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_baron_level': player.upgrade_baron_level,
            'points_per_second': player.points_per_second,
            'upgrade_baron_cost': player.upgrade_baron_cost
        })

def buy_king_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 90:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_king_cost:
            player.player_level += 1
            player.points -= player.upgrade_king_cost
            player.upgrade_king_level += 1
            player.points_per_second += player.king_per_second
            player.upgrade_king_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_king_level': player.upgrade_king_level,
            'points_per_second': player.points_per_second,
            'upgrade_king_cost': player.upgrade_king_cost
        })

def buy_pope_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 100:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_pope_cost:
            player.player_level += 1
            player.points -= player.upgrade_pope_cost
            player.upgrade_pope_level += 1
            player.points_per_second += player.pope_per_second
            player.upgrade_pope_cost *= 2
            player.save()

        return JsonResponse({
            'player_level': player.player_level,
            'points': player.points,
            'upgrade_pope_level': player.upgrade_pope_level,
            'points_per_second': player.points_per_second,
            'upgrade_pope_cost': player.upgrade_pope_cost
        })

def reset_game(request):
    if request.method == "POST":
        player = Player.objects.first()

        # base stats
        player.player_level = 0
        player.points = 0.0
        player.points_per_click = 1.0
        player.upgrade_cost = 10.0
        player.upgrade_level = 0
        player.player_total_clicks = 0
        player.player_total_clicks_earned = 0.0
        player.player_total_crits = 0
        player.player_total_crits_earned = 0.0
        player.player_total_both_earned = 0.0
        player.rebirth = 0
        player.rebirth_cost = 1000000.0
        player.rebirth_gems = 0.0

        player.tax = 0.0
        player.upgrade_tax_cost = 1000.0
        player.upgrade_tax_level = 0

        player.anchor = 10000.0
        player.upgrade_anchor_cost = 3000.0
        player.upgrade_anchor_level = 0

        player.dragon_multiplier = 1.0
        player.upgrade_dragon_multiplier_cost = 10000.0
        player.upgrade_dragon_multiplier_level = 0

        player.luck = 0.0
        player.upgrade_luck_level = 0
        player.upgrade_luck_cost = 200.0

        player.time_offline = 0
        player.upgrade_time_offline_cost = 300.0
        player.upgrade_time_offline_level = 0

        player.shekel_multiplier = 1.0
        player.upgrade_shekel_multiplier_level = 0
        player.upgrade_shekel_multiplier_cost = 500.0

        # weapons
        player.upgrade_wooden_sword_cost = 100.0
        player.upgrade_wooden_sword_level = 0

        player.upgrade_short_sword_cost = 500.0
        player.upgrade_short_sword_level = 0

        player.upgrade_long_sword_cost = 1000.0
        player.upgrade_long_sword_level = 0

        player.upgrade_slingshot_cost = 2000.0
        player.upgrade_slingshot_level = 0

        player.upgrade_bow_cost = 5000.0
        player.upgrade_bow_level = 0

        player.upgrade_crossbow_cost = 10000.0
        player.upgrade_crossbow_level = 0

        player.upgrade_spear_cost = 30000.0
        player.upgrade_spear_level = 0

        player.upgrade_shield_cost = 50000.0
        player.upgrade_shield_level = 0

        player.upgrade_warhammer_cost = 100000.0
        player.upgrade_warhammer_level = 0

        # crit system
        player.crit_chance = 1.0
        player.crit_chance_upgrade_cost = 100.0
        player.upgrade_crit_chance_level = 0

        player.crit_multiplier = 2.0
        player.crit_multiplier_upgrade_cost = 150.0
        player.upgrade_crit_multiplier_level = 0

        # auto click
        player.points_per_second = 0.0

        player.auto_upgrade_cost = 20.0
        player.upgrade_auto_level = 0

        player.upgrade_drunk_cost = 100.0
        player.upgrade_drunk_level = 0

        player.upgrade_maid_cost = 500.0
        player.upgrade_maid_level = 0

        player.upgrade_groom_cost = 2000.0
        player.upgrade_groom_level = 0

        player.upgrade_jester_cost = 5000.0
        player.upgrade_jester_level = 0

        player.upgrade_priest_cost = 20000.0
        player.upgrade_priest_level = 0

        player.upgrade_archer_cost = 50000.0
        player.upgrade_archer_level = 0

        player.upgrade_knight_cost = 100000.0
        player.upgrade_knight_level = 0

        player.upgrade_cavalry_cost = 400000.0
        player.upgrade_cavalry_level = 0

        player.upgrade_architect_cost = 1000000.0
        player.upgrade_architect_level = 0

        player.upgrade_baron_cost = 10000000.0
        player.upgrade_baron_level = 0

        player.upgrade_king_cost = 30000000.0
        player.upgrade_king_level = 0

        player.upgrade_pope_cost = 100000000.0
        player.upgrade_pope_level = 0

        player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'points_per_click': player.points_per_click,
            'upgrade_cost': player.upgrade_cost,
            'upgrade_level': player.upgrade_level,

            'player_total_clicks': player.player_total_clicks,
            'player_total_clicks_earned': player.player_total_clicks_earned,
            'player_total_crits': player.player_total_crits,
            'player_total_both_earned': player.player_total_both_earned,
            'player_total_crits_earned': player.player_total_crits_earned,

            'rebirth': player.rebirth,
            'rebirth_cost': player.rebirth_cost,
            'rebirth_gems': player.rebirth_gems,

            'tax': player.tax,
            'upgrade_tax_cost': player.upgrade_tax_cost,
            'upgrade_tax_level': player.upgrade_tax_level,

            'anchor': player.anchor,
            'upgrade_anchor_cost': player.upgrade_anchor_cost,
            'upgrade_anchor_level': player.upgrade_anchor_level,

            'dragon_multiplier': player.dragon_multiplier,
            'upgrade_dragon_multiplier_cost': player.upgrade_dragon_multiplier_cost,
            'upgrade_dragon_multiplier_level': player.upgrade_dragon_multiplier_level,

            'luck': player.luck,
            'upgrade_luck_level': player.upgrade_luck_level,
            'upgrade_luck_cost': player.upgrade_luck_cost,

            'shekel_multiplier': player.shekel_multiplier,
            'upgrade_shekel_multiplier_cost': player.upgrade_shekel_multiplier_cost,
            'upgrade_shekel_multiplier_level': player.upgrade_shekel_multiplier_level,

            'time_offline': player.time_offline,
            'upgrade_time_offline_cost': player.upgrade_time_offline_cost,
            'upgrade_time_offline_level': player.upgrade_time_offline_level,

            'upgrade_wooden_sword_cost': player.upgrade_wooden_sword_cost,
            'upgrade_wooden_sword_level': player.upgrade_wooden_sword_level,

            'upgrade_short_sword_cost': player.upgrade_short_sword_cost,
            'upgrade_short_sword_level': player.upgrade_short_sword_level,

            'upgrade_long_sword_cost': player.upgrade_long_sword_cost,
            'upgrade_long_sword_level': player.upgrade_long_sword_level,

            'upgrade_slingshot_cost': player.upgrade_slingshot_cost,
            'upgrade_slingshot_level': player.upgrade_slingshot_level,

            'upgrade_bow_cost': player.upgrade_bow_cost,
            'upgrade_bow_level': player.upgrade_bow_level,

            'upgrade_crossbow_cost': player.upgrade_crossbow_cost,
            'upgrade_crossbow_level': player.upgrade_crossbow_level,

            'upgrade_spear_cost': player.upgrade_spear_cost,
            'upgrade_spear_level': player.upgrade_spear_level,

            'upgrade_shield_cost': player.upgrade_shield_cost,
            'upgrade_shield_level': player.upgrade_shield_level,

            'upgrade_warhammer_cost': player.upgrade_warhammer_cost,
            'upgrade_warhammer_level': player.upgrade_warhammer_level,

            'crit_chance': player.crit_chance,
            'crit_chance_upgrade_cost': player.crit_chance_upgrade_cost,
            'upgrade_crit_chance_level': player.upgrade_crit_chance_level,

            'crit_multiplier': player.crit_multiplier,
            'crit_multiplier_upgrade_cost': player.crit_multiplier_upgrade_cost,
            'upgrade_crit_multiplier_level': player.upgrade_crit_multiplier_level,

            'points_per_second': player.points_per_second,

            'auto_upgrade_cost': player.auto_upgrade_cost,
            'upgrade_auto_level': player.upgrade_auto_level,

            'upgrade_drunk_cost': player.upgrade_drunk_cost,
            'upgrade_drunk_level': player.upgrade_drunk_level,

            'upgrade_maid_cost': player.upgrade_maid_cost,
            'upgrade_maid_level': player.upgrade_maid_level,

            'upgrade_groom_cost': player.upgrade_groom_cost,
            'upgrade_groom_level': player.upgrade_groom_level,

            'upgrade_jester_cost': player.upgrade_jester_cost,
            'upgrade_jester_level': player.upgrade_jester_level,

            'upgrade_priest_cost': player.upgrade_priest_cost,
            'upgrade_priest_level': player.upgrade_priest_level,

            'upgrade_archer_cost': player.upgrade_archer_cost,
            'upgrade_archer_level': player.upgrade_archer_level,

            'upgrade_knight_cost': player.upgrade_knight_cost,
            'upgrade_knight_level': player.upgrade_knight_level,

            'upgrade_cavalry_cost': player.upgrade_cavalry_cost,
            'upgrade_cavalry_level': player.upgrade_cavalry_level,

            'upgrade_architect_cost': player.upgrade_architect_cost,
            'upgrade_architect_level': player.upgrade_architect_level,

            'upgrade_baron_cost': player.upgrade_baron_cost,
            'upgrade_baron_level': player.upgrade_baron_level,

            'upgrade_king_cost': player.upgrade_king_cost,
            'upgrade_king_level': player.upgrade_king_level,

            'upgrade_pope_cost': player.upgrade_pope_cost,
            'upgrade_pope_level': player.upgrade_pope_level,
        })


def buy_auto_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.auto_upgrade_cost:
            player.player_level += 1
            player.points -= player.auto_upgrade_cost
            player.upgrade_auto_level += 1
            player.points_per_second += player.auto_per_second
            player.auto_upgrade_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_auto_level': player.upgrade_auto_level,
            'points_per_second': player.points_per_second,
            'auto_upgrade_cost': player.auto_upgrade_cost,
        })

def buy_crit_chance_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.crit_chance_upgrade_cost:
            player.points -= player.crit_chance_upgrade_cost
            player.upgrade_crit_chance_level += 1
            player.crit_chance += 1 
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
            player.crit_multiplier_upgrade_cost *= 3
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
            player.points_per_click += player.wooden_sword_per_click
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

        if player.player_level < 15:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_short_sword_cost:
            player.player_level += 1
            player.points -= player.upgrade_short_sword_cost
            player.upgrade_short_sword_level += 1
            player.points_per_click += player.short_sword_per_click
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

        if player.player_level < 25:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_long_sword_cost:
            player.player_level += 1
            player.points -= player.upgrade_long_sword_cost
            player.upgrade_long_sword_level += 1
            player.points_per_click += player.long_sword_per_click
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

        if player.player_level < 30:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_slingshot_cost:
            player.player_level += 1
            player.points -= player.upgrade_slingshot_cost
            player.upgrade_slingshot_level += 1
            player.points_per_click += player.slingshot_per_click
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

        if player.player_level < 40:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_bow_cost:
            player.player_level += 1
            player.points -= player.upgrade_bow_cost
            player.upgrade_bow_level += 1
            player.points_per_click += player.bow_per_click
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

        if player.player_level < 50:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_crossbow_cost:
            player.player_level += 1
            player.points -= player.upgrade_crossbow_cost
            player.upgrade_crossbow_level += 1
            player.points_per_click += player.crossbow_per_click
            player.upgrade_crossbow_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_crossbow_level': player.upgrade_crossbow_level,
            'points_per_click': player.points_per_click,
            'upgrade_crossbow_cost': player.upgrade_crossbow_cost
        })

def buy_spear_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 70:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_spear_cost:
            player.player_level += 1
            player.points -= player.upgrade_spear_cost
            player.upgrade_spear_level += 1
            player.points_per_click += player.spear_per_click
            player.upgrade_spear_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_spear_level': player.upgrade_spear_level,
            'points_per_click': player.points_per_click,
            'upgrade_spear_cost': player.upgrade_spear_cost
        })

def buy_shield_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 90:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_shield_cost:
            player.player_level += 1
            player.points -= player.upgrade_shield_cost
            player.upgrade_shield_level += 1
            player.points_per_click += player.shield_per_click
            player.upgrade_shield_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_shield_level': player.upgrade_shield_level,
            'points_per_click': player.points_per_click,
            'upgrade_shield_cost': player.upgrade_shield_cost
        })

def buy_warhammer_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.player_level < 110:
            return JsonResponse({"error": "Locked"}, status=403)

        if player.points >= player.upgrade_warhammer_cost:
            player.player_level += 1
            player.points -= player.upgrade_warhammer_cost
            player.upgrade_warhammer_level += 1
            player.points_per_click += player.warhammer_per_click
            player.upgrade_warhammer_cost *= 2
            player.save()

        return JsonResponse({
            'points': player.points,
            'player_level': player.player_level,
            'upgrade_warhammer_level': player.upgrade_warhammer_level,
            'points_per_click': player.points_per_click,
            'upgrade_warhammer_cost': player.upgrade_warhammer_cost
        })


def buy_luck_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.upgrade_luck_cost:
            player.points -= player.upgrade_luck_cost
            player.upgrade_luck_level += 1
            player.luck += 1.0
            player.upgrade_luck_cost *= 3
            player.save()

        return JsonResponse({
            'points': player.points,
            'luck': player.luck,
            'upgrade_luck_level': player.upgrade_luck_level,
            'upgrade_luck_cost': player.upgrade_luck_cost
        })


def buy_time_offline_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.upgrade_time_offline_cost:
            player.points -= player.upgrade_time_offline_cost
            player.upgrade_time_offline_level += 1
            player.time_offline += 1
            player.upgrade_time_offline_cost *= 3
            player.save()

        return JsonResponse({
            'points': player.points,
            'time_offline': player.time_offline,
            'upgrade_time_offline_level': player.upgrade_time_offline_level,
            'upgrade_time_offline_cost': player.upgrade_time_offline_cost
        })


def buy_shekel_multiplier_upgrade(request):
    if request.method == "POST":
        player = Player.objects.first()

        if player.points >= player.upgrade_shekel_multiplier_cost:
            player.points -= player.upgrade_shekel_multiplier_cost
            player.upgrade_shekel_multiplier_level += 1
            player.shekel_multiplier += 0.1
            player.upgrade_shekel_multiplier_cost *= 3
            player.save()

        return JsonResponse({
            'points': player.points,
            'shekel_multiplier': player.shekel_multiplier,
            'upgrade_shekel_multiplier_level': player.upgrade_shekel_multiplier_level,
            'upgrade_shekel_multiplier_cost': player.upgrade_shekel_multiplier_cost
        })