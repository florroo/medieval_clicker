
function updateTitle(points) {
    document.title = "Medieval Clicker - " + points;
}

function playClickSound() {
    const sound = new Audio("/static/game/click.mp3");
    sound.volume = 0.1;
    sound.playbackRate = 0.95 + Math.random() * 0.1;
    sound.play();
}

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
        document.getElementById('cost').innerText = data.upgrade_cost;

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
        document.getElementById('points').innerText = data.points;
        document.getElementById('points_per_click').innerText = data.points_per_click;
        document.getElementById('cost').innerText = data.upgrade_cost;
        document.getElementById('points_per_second').innerText = data.points_per_second;
        document.getElementById('auto_upgrade_cost').innerText = data.auto_upgrade_cost;
        document.getElementById('crit_chance').innerText = data.crit_chance;
        document.getElementById('crit_chance_upgrade_cost').innerText = data.crit_chance_upgrade_cost;
        document.getElementById('crit_multiplier').innerText = data.crit_multiplier;
        document.getElementById('crit_multiplier_upgrade_cost').innerText = data.crit_multiplier_upgrade_cost;

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
        document.getElementById('auto_upgrade_cost').innerText = data.auto_upgrade_cost;

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