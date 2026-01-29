document.addEventListener('DOMContentLoaded', function () {
    console.log("Ashifune Gen. Univ. System Init - ver 3.4.2");

    // Search Logic
    const searchBtn = document.getElementById('searchBtn');
    const searchInput = document.getElementById('searchInput');

    if (searchBtn && searchInput) {
        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') performSearch();
        });
    }

    // Context Aware Triggers (e.g. Hovering specific elements)
    setupContextTriggers();
});

function performSearch() {
    const query = document.getElementById('searchInput').value.trim().toLowerCase();

    // Hidden & Normal Keywords
    const secretKeywords = {
        // Secrets
        'specimen': 'archive/log.html',
        'escape': 'news/2024_08_30_construction.html',
        'mirror': '404.html',
        'water': '404.html',
        '25-c-0992': 'portal/dashboard.html',
        '304': 'archive/log.html',

        // Normal Navigation
        'syllabus': 'faculties.html',
        'シラバス': 'faculties.html',
        'access': 'about.html#access',
        'アクセス': 'about.html#access',
        'map': 'about.html#access',
        'library': 'library/index.html',
        '図書館': 'library/index.html',
        'news': 'index.html#news',
        'ニュース': 'index.html#news',
        'login': 'portal/login.html'
    };

    if (secretKeywords[query]) {
        // "Loading" simulation
        document.body.style.cursor = 'wait';
        setTimeout(() => {
            window.location.href = secretKeywords[query];
        }, 800);
    } else {
        alert("検索結果: 0件\n該当する公開情報は存在しません。\n\nヒント: 学内専用のキーワード（ID、管理用語など）を入力してください。");
    }
}

function setupContextTriggers() {
    // Example: President's image distorts if hovered too long
    const presidentImg = document.querySelector('.president-img');
    if (presidentImg) {
        presidentImg.addEventListener('mouseenter', () => {
            presidentImg.dataset.timer = setTimeout(() => {
                presidentImg.style.filter = "invert(1)";
                // Ideally swap src to a scary one if available
            }, 3000); // 3 seconds hover
        });
        presidentImg.addEventListener('mouseleave', () => {
            clearTimeout(presidentImg.dataset.timer);
            presidentImg.style.filter = "none";
        });
    }
}
