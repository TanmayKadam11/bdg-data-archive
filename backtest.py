import csv

wins = 0
losses = 0

rows = []

with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Example strategy:
# Agar pichhle 3 results Big hain,
# to next Small predict karo.

for i in range(3, len(rows)):
    last3 = [
        rows[i-1]["BigSmall"],
        rows[i-2]["BigSmall"],
        rows[i-3]["BigSmall"]
    ]

    prediction = None

    if last3 == ["Big", "Big", "Big"]:
        prediction = "Small"

    if prediction:
        actual = rows[i]["BigSmall"]

        if prediction == actual:
            wins += 1
        else:
            losses += 1

print("Wins:", wins)
print("Losses:", losses)

total = wins + losses

if total > 0:
    print("Win Rate:", round((wins / total) * 100, 2), "%")
else:
    print("No trades found")
