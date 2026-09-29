TOTAL = 150000

print("========== VIT COUNSELLING SIMULATOR ==========")
print(f"Total candidates appeared: {TOTAL}\n")
def get_int(prompt, low, high):
    while True:
        try:
            val = int(input(prompt))
            if low <= val <= high:
                return val
            print(f"Invalid input! Enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

rank = get_int(f"Enter your rank (1 to {TOTAL}): ", 1, TOTAL)
campuses = {1: "VIT Vellore", 2: "VIT Chennai", 3: "VIT AP", 4: "VIT Bhopal"}
branches = {
    1: "CSE",
    2: "CSE (AI & ML)",
    3: "CSE (Data Science)",
    4: "ECE",
    5: "EEE",
    6: "Mechanical Engineering",
}

print("\nCampus Choices:")
for k, v in campuses.items():
    print(f"{k} - {v}")
print("\nBranch Choices:")
for k, v in branches.items():
    print(f"{k} - {v}")
print("\nFee Category: REGULAR")
n = get_int("\nHow many preferences do you want to enter? ", 1, 24)
prefs = []
i = 0
while i < n:
    print(f"\n--- Preference {i + 1} ---")
    c = get_int("Enter campus number (1-4): ", 1, 4)
    b = get_int("Enter branch number (1-6): ", 1, 6)

    pair = (c, b)
    if pair in prefs:
        print(" You already selected this option! Choose another one.")
        continue
    prefs.append(pair)
    i += 1

cutoffs = {
    ("VIT Vellore", "CSE"): 5000,
    ("VIT Vellore", "CSE (AI & ML)"): 8000,
    ("VIT Vellore", "CSE (Data Science)"): 10000,
    ("VIT Vellore", "ECE"): 16000,
    ("VIT Vellore", "EEE"): 28000,
    ("VIT Vellore", "Mechanical Engineering"): 35000,

    ("VIT Chennai", "CSE"): 12000,
    ("VIT Chennai", "CSE (AI & ML)"): 16000,
    ("VIT Chennai", "CSE (Data Science)"): 18000,
    ("VIT Chennai", "ECE"): 25000,
    ("VIT Chennai", "EEE"): 32000,
    ("VIT Chennai", "Mechanical Engineering"): 40000,

    ("VIT AP", "CSE"): 100000,
    ("VIT AP", "CSE (AI & ML)"): 115000,
    ("VIT AP", "CSE (Data Science)"): 130000,
    ("VIT AP", "ECE"): 140000,
    ("VIT AP", "EEE"): 145000,
    ("VIT AP", "Mechanical Engineering"): 149000,

    ("VIT Bhopal", "CSE"): 80000,
    ("VIT Bhopal", "CSE (AI & ML)"): 90000,
    ("VIT Bhopal", "CSE (Data Science)"): 100000,
    ("VIT Bhopal", "ECE"): 110000,
    ("VIT Bhopal", "EEE"): 125000,
    ("VIT Bhopal", "Mechanical Engineering"): 135000,
}
print("\n========== EVALUATING PREFERENCES ==========")
eligible = []
for idx, (c_code, b_code) in enumerate(prefs, start=1):
    c_name = campuses[c_code]
    b_name = branches[b_code]
    cutoff = cutoffs.get((c_name, b_name))

    print(f"\nChecking Preference {idx}: {c_name} - {b_name}")

    if cutoff is None:
        print("Status: No cutoff available.")
        continue

    if rank <= cutoff:
        print(f"Status: Eligible (Cutoff: {cutoff})")
        eligible.append(
            {"pref": idx, "campus": c_name, "branch": b_name, "cutoff": cutoff}
        )
    else:
        print(f"Status: Not Eligible (Rank: {rank} > Cutoff: {cutoff})")
print("\n========== COUNSELLING RESULT ==========")
if eligible:
    best = min(eligible, key=lambda x: x["cutoff"])

    print("\n🎉 BEST SEAT ALLOTTED!")
    print("-----------------------------")
    print("VITEEE Rank  :", rank)
    print("Preference   :", best["pref"])
    print("Campus       :", best["campus"])
    print("Branch       :", best["branch"])
    print("Min Cutoff   :", best["cutoff"])
    print("Fee Category : Regular")
    print("Status       : ALLOTTED")
    print("-----------------------------")
else:
    print("\n NO SEAT ALLOTTED")
    print("None of your choices matched the cutoff criteria.")
