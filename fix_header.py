import os
import re

ROOT_DIR = r"c:\mokyu\site"


def get_relative_path_prefix(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    depth = len(os.path.dirname(rel_path).split(os.sep))
    if os.path.dirname(rel_path) == '':
        depth = 0
    return "../" * depth


def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    prefix = get_relative_path_prefix(filepath)

    # 1. Prepare Top Bar Content
    top_bar = f"""    <!-- Top Bar -->
    <div class="top-bar">
        <div class="container">
            <a href="{prefix}about.html#access">交通アクセス</a> | 
            <a href="{prefix}admissions.html">資料請求</a> | 
            <a href="#">お問い合わせ</a> | 
            <a href="#">English</a>
        </div>
    </div>"""

    # 2. Inject Top Bar (if missing)
    if 'class="top-bar"' not in content:
        # Insert before <header> if it exists, otherwise after <body>
        if '<header' in content:
            content = re.sub(
                r'(<header)', f'{top_bar}\n    \\1', content, count=1)
        else:
            content = re.sub(
                r'(<body.*?>)', f'\\1\n{top_bar}', content, count=1, flags=re.IGNORECASE)
        print(f"Added Top Bar to {filepath}")

    # 3. Prepare Access Button
    access_btn = f'<li><a href="{prefix}portal/login.html" class="access-btn">在学生・教職員</a></li>'

    # 4. Inject Access Button (if missing)
    if 'class="access-btn"' not in content:
        # Look for the navigation ul
        # Pattern: <nav> ... <ul> ... </ul> ... </nav>
        # We want to insert before the closing </ul> inside the nav

        # Simple regex to find the closing </ul> of the PRIMARY nav
        # We assume the first <ul> inside <nav> is the main menu
        if '<nav>' in content:
            # Find the nav block
            nav_match = re.search(r'(<nav>.*?</nav>)',
                                  content, re.DOTALL | re.IGNORECASE)
            if nav_match:
                nav_content = nav_match.group(1)
                if 'class="access-btn"' not in nav_content:
                    # Inject before last </ul> in this nav block
                    new_nav_content = re.sub(
                        r'(</ul>)', f'    {access_btn}\n                \\1', nav_content, count=1, flags=re.IGNORECASE)
                    content = content.replace(
                        nav_match.group(1), new_nav_content)
                    print(f"Added Access Button to {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))

print("Header standardization complete.")
