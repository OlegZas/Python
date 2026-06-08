# File Management Lab - World Cup

import html
import webbrowser
import os

try:
    user_input = input("Enter national team name (Morocco, Mexico, Usa, Japan, Canada): ")
    parts = [p.strip() for p in user_input.split(",")]

    team = parts[0].title() if len(parts) > 0 and parts[0] else "Unknown"

    teams = {
        "Morocco": ("8", "Defensive discipline, quick breaks, and strong team shape."),
        "Mexico": ("15", "Aggressive pressing, wide attacks, and using home support."),
        "Usa": ("16", "Energy, pressing, fast counter attacks, and young players."),
        "Japan": ("18", "Quick passing, smart movement, and hard work without the ball."),
        "Canada": ("30", "Speed, counter attacks, and attacking from wide areas.")
    }

    ranking, focus = teams.get(team, ("Not found", "Try Morocco, Mexico, USA, Japan, or Canada."))

    team = html.escape(team)
    ranking = html.escape(ranking)
    focus = html.escape(focus)

    html_page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{team}</title>
    <style>
        body {{ font-family: Arial; background-color: #e8f1ff; margin: 30px; }}
        .card {{ background: white; padding: 20px; border-radius: 10px; }}
        ul {{ line-height: 1.8; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{team}</h1>
        <h2>2026 World Cup Team Information</h2>
        <p>This page shows the national team and their FIFA ranking, and tactical focus.</p>
        <ul>
            <li>National Team: {team}</li>
            <li>FIFA Ranking: {ranking}</li>
            <li>Tactical Focus: {focus}</li>
        </ul>
    </div>
</body>
</html>
"""

    file_name = "world_cup_team_page.html"

    with open(file_name, "w") as file:
        file.write(html_page)

    webbrowser.open("file://" + os.path.abspath(file_name))

    print("HTML file created and opened:", file_name)

except Exception as error:
    print("Something went wrong.")
    print("Error:", error)