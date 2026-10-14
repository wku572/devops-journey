import json

# Variables and f-strings
name = "santa"
weeks = 12
print(f"Hello {name}, my plan is {weeks} weeks long")

# Lists and loops
skills = ["Linux", "Bash", "Git", "Python", "Docker"]
for skill in skills:
    print("Learning:", skill)

# Dictionaries
progress = {"Linux": True, "Bash": True, "Git": True, "Python": True, "Docker": False}

# Functions
def percent_done(data):
	return sum(100 for done on data.values() if done)

def count_done(data):
    return sum(1 for done in data.values() if done)

done = count_done(progress)
print(f"{done} of {len(progress)} skills done")

# Conditions
if done == len(progress):
    print("All done!")
else:
    print("Keep going")

# Write a JSON file
with open("progress.json", "w") as f:
    json.dump(progress, f, indent=2)

# Read it back
with open("progress.json") as f:
    loaded = json.load(f)
print("Loaded from file:", loaded)
