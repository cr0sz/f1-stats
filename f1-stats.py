import requests

def get_f1_drivers(year):
    url = f"https://api.openf1.org/v1/drivers?session_key=latest"
    
    response = requests.get(url)
    data = response.json()

    print(f"\n🏎️  F1 Drivers - Latest Session")
    print("-" * 45)

    seen = []
    for driver in data:
        name = driver.get("full_name", "Unknown")
        team = driver.get("team_name", "Unknown")
        number = driver.get("driver_number", "?")
        country = driver.get("country_code", "?")

        if name not in seen:  # avoid duplicates
            seen.append(name)
            print(f"#{number} {name}")
            print(f"   Team: {team} | Country: {country}")
            print()

get_f1_drivers(2024)

def get_team_drivers(team_name):
    url = "https://api.openf1.org/v1/drivers?session_key=latest"
    response = requests.get(url)
    data = response.json()

    print(f"\n🏎️  Drivers for: {team_name}")
    print("-" * 45)

    seen = []
    for driver in data:
        team = driver.get("team_name", "")
        name = driver.get("full_name", "Unknown")
        number = driver.get("driver_number", "?")

        if team_name.lower() in team.lower() and name not in seen:
            seen.append(name)
            print(f"#{number} {name} — {team}")

team_input = input("Enter a team name: ")
get_team_drivers(team_input)

def save_to_file(team_name):
    url = "https://api.openf1.org/v1/drivers?session_key=latest"
    response = requests.get(url)
    data = response.json()

    filename = f"{team_name}_drivers.txt"

    with open(filename, "w") as f:
        f.write(f"F1 Drivers - {team_name}\n")
        f.write("-" * 45 + "\n")

        seen = []
        for driver in data:
            team = driver.get("team_name", "")
            name = driver.get("full_name", "Unknown")
            number = driver.get("driver_number", "?")
            country = driver.get("country_code", "?")

            if team_name.lower() in team.lower() and name not in seen:
                seen.append(name)
                f.write(f"#{number} {name} — {team} | {country}\n")

    print(f"✅ Saved to {filename}")

save_to_file("McLaren")