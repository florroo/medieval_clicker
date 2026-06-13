
function updateTitle(points) {
    document.title = "Medieval Clicker - " + points;
}

function playClickSound() {
    const sound = new Audio("/static/game/click.mp3");
    sound.volume = 0.1;
    sound.playbackRate = 0.95 + Math.random() * 0.1;
    sound.play();
}

function openStats() {
    document.getElementById('stats-modal').style.display = 'flex';
    fetchStats();
    statsInterval = setInterval(fetchStats, 2000);
}

function closeStats() {
    document.getElementById('stats-modal').style.display = 'none';
    clearInterval(statsInterval);
    statsInterval = null;
}

function fetchStats() {
    fetch('/stats/')
        .then(res => res.json())
        .then(data => {
            document.getElementById('stat_total_clicks').innerText = data.player_total_clicks;
            document.getElementById('stat_clicks_earned').innerText = data.player_total_clicks_earned;
            document.getElementById('stat_total_crits').innerText = data.player_total_crits;
            document.getElementById('stat_crits_earned').innerText = data.player_total_crits_earned;
            document.getElementById('stat_both_earned').innerText = data.player_total_both_earned;
        });
}

function closeOfflineModal() {
  document.getElementById('offline-modal').style.display = 'none';
  sessionStorage.setItem('offlineModalShown', 'true');
}

window.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('offline-modal');
  if (modal && sessionStorage.getItem('offlineModalShown') === 'true') {
    modal.style.display = 'none';
  }
});

function sendClick(event) {
    fetch('/click/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        updateTitle(data.points);

        if (data.is_crit) {
            const critSound = document.getElementById("crit_sound");
            critSound.currentTime = 0;
            critSound.play().catch(err => console.log(err));
        } else {
            playClickSound();
        }

        createFloatingText(
            event.pageX,
            event.pageY,
            data.gained_points,
            data.is_crit
        );
    });
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = cookie.substring(name.length + 1);
                break;
            }
        }
    }
    return cookieValue;
}

function buyUpgrade() {
    fetch('/buy/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_level').innerHTML = data.upgrade_level;
        document.getElementById('cost').innerText = data.upgrade_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points)

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyWoodenSwordUpgrade() {
    fetch('/buy-wooden-sword/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_wooden_sword_level').innerHTML = data.upgrade_wooden_sword_level;
        document.getElementById('upgrade_wooden_sword_cost').innerText = data.upgrade_wooden_sword_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyShortSwordUpgrade() {
    fetch('/buy-short-sword/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_short_sword_level').innerHTML = data.upgrade_short_sword_level;
        document.getElementById('upgrade_short_sword_cost').innerText = data.upgrade_short_sword_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyLongSwordUpgrade() {
    fetch('/buy-long-sword/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_long_sword_level').innerHTML = data.upgrade_long_sword_level;
        document.getElementById('upgrade_long_sword_cost').innerText = data.upgrade_long_sword_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buySlingshotUpgrade() {
    fetch('/buy-slingshot/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_slingshot_level').innerHTML = data.upgrade_slingshot_level;
        document.getElementById('upgrade_slingshot_cost').innerText = data.upgrade_slingshot_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyBowUpgrade() {
    fetch('/buy-bow/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_bow_level').innerHTML = data.upgrade_bow_level;
        document.getElementById('upgrade_bow_cost').innerText = data.upgrade_bow_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyCrossbowUpgrade() {
    fetch('/buy-crossbow/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_crossbow_level').innerHTML = data.upgrade_crossbow_level;
        document.getElementById('upgrade_crossbow_cost').innerText = data.upgrade_crossbow_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buySpearUpgrade() {
    fetch('/buy-spear/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_spear_level').innerHTML = data.upgrade_spear_level;
        document.getElementById('upgrade_spear_cost').innerText = data.upgrade_spear_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyShieldUpgrade() {
    fetch('/buy-shield/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_shield_level').innerHTML = data.upgrade_shield_level;
        document.getElementById('upgrade_shield_cost').innerText = data.upgrade_shield_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyWarhammerUpgrade() {
    fetch('/buy-warhammer/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('upgrade_warhammer_level').innerHTML = data.upgrade_warhammer_level;
        document.getElementById('upgrade_warhammer_cost').innerText = data.upgrade_warhammer_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function resetGame() {
    if (!confirm("Na pewno chcesz zresetować progres?")) return;

    fetch('/reset/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {

        // base stats
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;

        document.getElementById('player_level').innerHTML = data.player_level;

        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('crit_multiplier').innerText = data.crit_multiplier;
        document.getElementById('crit_chance').innerText = data.crit_chance;
        document.getElementById('luck').innerText = data.luck;
        document.getElementById('time_offline').innerText = data.time_offline;
        document.getElementById('shekel_multiplier').innerText = data.shekel_multiplier;

        document.getElementById('upgrade_time_offline_cost').innerText = data.upgrade_time_offline_cost;
        document.getElementById('upgrade_time_offline_level').innerText = data.upgrade_time_offline_level;

        document.getElementById('upgrade_shekel_multiplier_cost').innerText = data.upgrade_shekel_multiplier_cost;
        document.getElementById('upgrade_shekel_multiplier_level').innerText = data.upgrade_shekel_multiplier_level;

        document.getElementById('upgrade_luck_cost').innerText = data.upgrade_luck_cost;
        document.getElementById('upgrade_luck_level').innerText = data.upgrade_luck_level;

        // crit system 
        document.getElementById('crit_chance_upgrade_cost').innerText = data.crit_chance_upgrade_cost;
        document.getElementById('upgrade_crit_chance_level').innerText = data.upgrade_crit_chance_level;

        document.getElementById('crit_multiplier_upgrade_cost').innerText = data.crit_multiplier_upgrade_cost;
        document.getElementById('upgrade_crit_multiplier_level').innerText = data.upgrade_crit_multiplier_level;

        // click income
        document.getElementById('cost').innerText = data.upgrade_cost;
        document.getElementById('upgrade_level').innerText = data.upgrade_level;

        document.getElementById('upgrade_wooden_sword_cost').innerText = data.upgrade_wooden_sword_cost;
        document.getElementById('upgrade_wooden_sword_level').innerText = data.upgrade_wooden_sword_level;

        document.getElementById('upgrade_short_sword_cost').innerText = data.upgrade_short_sword_cost;
        document.getElementById('upgrade_short_sword_level').innerText = data.upgrade_short_sword_level;

        document.getElementById('upgrade_long_sword_cost').innerText = data.upgrade_long_sword_cost;
        document.getElementById('upgrade_long_sword_level').innerText = data.upgrade_long_sword_level;

        document.getElementById('upgrade_slingshot_cost').innerText = data.upgrade_slingshot_cost;
        document.getElementById('upgrade_slingshot_level').innerText = data.upgrade_slingshot_level;

        document.getElementById('upgrade_bow_cost').innerText = data.upgrade_bow_cost;
        document.getElementById('upgrade_bow_level').innerText = data.upgrade_bow_level;

        document.getElementById('upgrade_wooden_sword_cost').innerText = data.upgrade_wooden_sword_cost;
        document.getElementById('upgrade_crossbow_level').innerText = data.upgrade_crossbow_level;

        document.getElementById('upgrade_spear_cost').innerText = data.upgrade_spear_cost;
        document.getElementById('upgrade_spear_level').innerText = data.upgrade_spear_level;

        document.getElementById('upgrade_shield_cost').innerText = data.upgrade_shield_cost;
        document.getElementById('upgrade_shield_level').innerText = data.upgrade_shield_level;

        document.getElementById('upgrade_warhammer_cost').innerText = data.upgrade_warhammer_cost;
        document.getElementById('upgrade_warhammer_level').innerText = data.upgrade_warhammer_level;

        // auto income 
        document.getElementById('auto_upgrade_cost').innerText = data.auto_upgrade_cost;
        document.getElementById('upgrade_auto_level').innerText = data.upgrade_auto_level;

        document.getElementById('upgrade_drunk_cost').innerText = data.upgrade_drunk_cost;
        document.getElementById('upgrade_drunk_level').innerText = data.upgrade_drunk_level;

        document.getElementById('upgrade_maid_cost').innerText = data.upgrade_maid_cost;
        document.getElementById('upgrade_maid_level').innerText = data.upgrade_maid_level;

        document.getElementById('upgrade_groom_cost').innerText = data.upgrade_groom_cost;
        document.getElementById('upgrade_groom_level').innerText = data.upgrade_groom_level;

        document.getElementById('upgrade_jester_cost').innerText = data.upgrade_jester_cost;
        document.getElementById('upgrade_jester_level').innerText = data.upgrade_jester_level;

        document.getElementById('upgrade_priest_cost').innerText = data.upgrade_priest_cost;
        document.getElementById('upgrade_priest_level').innerText = data.upgrade_priest_level;

        document.getElementById('upgrade_archer_cost').innerText = data.upgrade_archer_cost;
        document.getElementById('upgrade_archer_level').innerText = data.upgrade_archer_level;

        document.getElementById('upgrade_knight_cost').innerText = data.upgrade_knight_cost;
        document.getElementById('upgrade_knight_level').innerText = data.upgrade_knight_level;

        document.getElementById('upgrade_cavalry_cost').innerText = data.upgrade_cavalry_cost;
        document.getElementById('upgrade_cavalry_level').innerText = data.upgrade_cavalry_level;

        document.getElementById('upgrade_architect_cost').innerText = data.upgrade_architect_cost;
        document.getElementById('upgrade_architect_level').innerText = data.upgrade_architect_level;

        document.getElementById('upgrade_baron_cost').innerText = data.upgrade_baron_cost;
        document.getElementById('upgrade_baron_level').innerText = data.upgrade_baron_level;

        document.getElementById('upgrade_king_cost').innerText = data.upgrade_king_cost;
        document.getElementById('upgrade_king_level').innerText = data.upgrade_king_level;

        document.getElementById('upgrade_pope_cost').innerText = data.upgrade_pope_cost;
        document.getElementById('upgrade_pope_level').innerText = data.upgrade_pope_level;

        updateUpgradeLocks();
        updateTitle(data.points);
    });
}



const music = document.getElementById("bg_music");
const musicBtn = document.getElementById("music_btn");

function updateButton() {
    musicBtn.innerText = music.paused
        ? "Włącz muzykę"
        : "Wyłącz muzykę";
}

function toggleMusic() {
    if (music.paused) {
        music.play().catch(err => console.log(err));
    } else {
        music.pause();
    }

    updateButton();
}

function toggleFont() {
    document.body.classList.toggle("font_default");

    const btn = document.getElementById("font_btn");

    if (document.body.classList.contains("font_default")) {
        btn.innerText = "Medieval font";
    } else {
        btn.innerText = "Default font";
    }
}


function toggleMode() {
    document.body.classList.toggle("dark");

    const isDark = document.body.classList.contains("dark");
    const btn = document.getElementById("mode_btn");

    btn.innerText = isDark ? "Light mode" : "Dark mode";

    localStorage.setItem("darkMode", isDark);
}

window.onload = function () {
    const isDark = localStorage.getItem("darkMode") === "true";
    const isDefault = localStorage.getItem("fontMode") === "true";

    if (isDefault) {
        document.body.classList.add("font_default");
        document.getElementById("font_btn").innerText = "Medieval font";
    }

    if (isDark) {
        document.body.classList.add("dark");
        document.getElementById("mode_btn").innerText = "Light mode";
    }

    updateUpgradeLocks();
};


function buyAutoUpgrade() {
    fetch('/buy-auto/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_auto_level').innerText = data.upgrade_auto_level;
        document.getElementById('auto_upgrade_cost').innerText = data.auto_upgrade_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyDrunkUpgrade() {
    fetch('/buy-drunk/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_drunk_level').innerText = data.upgrade_drunk_level;
        document.getElementById('upgrade_drunk_cost').innerText = data.upgrade_drunk_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyMaidUpgrade() {
    fetch('/buy-maid/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_maid_level').innerText = data.upgrade_maid_level;
        document.getElementById('upgrade_maid_cost').innerText = data.upgrade_maid_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyGroomUpgrade() {
    fetch('/buy-groom/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_groom_level').innerText = data.upgrade_groom_level;
        document.getElementById('upgrade_groom_cost').innerText = data.upgrade_groom_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyJesterUpgrade() {
    fetch('/buy-jester/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_jester_level').innerText = data.upgrade_jester_level;
        document.getElementById('upgrade_jester_cost').innerText = data.upgrade_jester_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyPriestUpgrade() {
    fetch('/buy-priest/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_priest_level').innerText = data.upgrade_priest_level;
        document.getElementById('upgrade_priest_cost').innerText = data.upgrade_priest_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyArcherUpgrade() {
    fetch('/buy-archer/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_archer_level').innerText = data.upgrade_archer_level;
        document.getElementById('upgrade_archer_cost').innerText = data.upgrade_archer_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyKnightUpgrade() {
    fetch('/buy-knight/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_knight_level').innerText = data.upgrade_knight_level;
        document.getElementById('upgrade_knight_cost').innerText = data.upgrade_knight_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyCavalryUpgrade() {
    fetch('/buy-cavalry/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_cavalry_level').innerText = data.upgrade_cavalry_level;
        document.getElementById('upgrade_cavalry_cost').innerText = data.upgrade_cavalry_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyArchitectUpgrade() {
    fetch('/buy-architect/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_architect_level').innerText = data.upgrade_architect_level;
        document.getElementById('upgrade_architect_cost').innerText = data.upgrade_architect_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyBaronUpgrade() {
    fetch('/buy-baron/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_baron_level').innerText = data.upgrade_baron_level;
        document.getElementById('upgrade_baron_cost').innerText = data.upgrade_baron_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyKingUpgrade() {
    fetch('/buy-king/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_king_level').innerText = data.upgrade_king_level;
        document.getElementById('upgrade_king_cost').innerText = data.upgrade_king_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyPopeUpgrade() {
    fetch('/buy-pope/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('upgrade_pope_level').innerText = data.upgrade_pope_level;
        document.getElementById('upgrade_pope_cost').innerText = data.upgrade_pope_cost;
        document.getElementById('player_level').innerText = data.player_level;

        updateUpgradeLocks();
        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

function buyCritUpgrade() {
    fetch('/buy-crit-chance/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('crit_chance').innerText = data.crit_chance;
        document.getElementById('crit_chance_upgrade_cost').innerText = data.crit_chance_upgrade_cost;
        document.getElementById('upgrade_crit_chance_level').innerText = data.upgrade_crit_chance_level;

        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyMultiplierUpgrade() {
    fetch('/buy-crit-multiplier/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('crit_multiplier').innerText = data.crit_multiplier;
        document.getElementById('crit_multiplier_upgrade_cost').innerText = data.crit_multiplier_upgrade_cost;
        document.getElementById('upgrade_crit_multiplier_level').innerText = data.upgrade_crit_multiplier_level;

        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyLuckUpgrade() {
    fetch('/buy-luck/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('luck').innerText = data.luck;
        document.getElementById('upgrade_luck_level').innerText = data.upgrade_luck_level;
        document.getElementById('upgrade_luck_cost').innerText = data.upgrade_luck_cost;

        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyTimeOfflineUpgrade() {
    fetch('/buy-time-offline/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('time_offline').innerText = data.time_offline;
        document.getElementById('upgrade_time_offline_level').innerText = data.upgrade_time_offline_level;
        document.getElementById('upgrade_time_offline_cost').innerText = data.upgrade_time_offline_cost;

        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}


function buyShekelMultiplierUpgrade() {
    fetch('/buy-shekel-multiplier/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('points').innerText = data.points;
        document.getElementById('shekel_multiplier').innerText = data.shekel_multiplier;
        document.getElementById('upgrade_shekel_multiplier_level').innerText = data.upgrade_shekel_multiplier_level;
        document.getElementById('upgrade_shekel_multiplier_cost').innerText = data.upgrade_shekel_multiplier_cost;

        updateTitle(data.points);

        const upgradeSound = document.getElementById("upgrade_sound");
        upgradeSound.currentTime = 0;
        upgradeSound.play().catch(err => console.log(err));
    });
}

setInterval(() => {
    const points_per_second = parseInt(document.getElementById("points_per_second").innerText);
    const pointsEl = document.getElementById("points");

    let currentPoints = parseInt(pointsEl.innerText);

    currentPoints += points_per_second;

    pointsEl.innerText = currentPoints;

    updateTitle(currentPoints);
}, 1000);


function createFloatingText(x, y, value, isCrit = false) {
    const text = document.createElement("span");
    text.classList.add("floating-text");

    if (isCrit) {
        text.innerText = "💥 CRIT! +" + value;
        text.classList.add("crit");
    } else {
        text.innerText = "+" + value;
    }

    text.style.left = x + "px";
    text.style.top = y + "px";

    document.body.appendChild(text);

    setTimeout(() => {
        text.remove();
    }, 1000);
}



function updateUpgradeLocks() {
    const playerLevel = parseInt(document.getElementById("player_level").innerText);

    document.querySelectorAll(".upgrade-block").forEach(block => {
        const requiredLevel = parseInt(block.dataset.requiredPlayerLevel);
        const btn = block.querySelector("button");
        const lock = block.querySelector(".lock-overlay");
        const text = block.querySelector(".required-level-text");

        if (text) {
            text.innerText = requiredLevel;
        }

        if (playerLevel < requiredLevel) {
            btn.disabled = true;
            btn.style.opacity = "0.5";
            if (lock) lock.style.display = "flex";
        } else {
            btn.disabled = false;
            btn.style.opacity = "1";
            if (lock) lock.style.display = "none";
        }
    });
}