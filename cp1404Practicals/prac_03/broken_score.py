"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if 0 <= score <= 100:
    if score >= 90:
        result = "Excellent"
    elif score < 50:
        result = "bad"
    else:
        result = "pass"
else:
    result = "Invalid score"

print(result)

