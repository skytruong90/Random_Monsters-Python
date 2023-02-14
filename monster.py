import random
import time

# Lists of possible names and abilities
names = ["Gorgon", "Kraken", "Cerberus", "Manticore", "Hydra"]
abilities = {
    "Gorgon": ["Petrifying Gaze", "Venomous Bite"],
    "Kraken": ["Tentacle Slam", "Ink Cloud"],
    "Cerberus": ["Fire Breath", "Shadow Step"],
    "Manticore": ["Poison Quills", "Flight"],
    "Hydra": ["Regeneration", "Acidic Spit"]
}

# Wait for 3 seconds before generating the monster name and abilities
print("Get ready! Starting in 3 seconds...")
time.sleep(3)

# Randomly choose a monster name from the list
name = random.choice(names)

# Choose two random abilities for the monster
chosen_abilities = random.sample(abilities[name], 2)

# Print the monster's name and abilities
print("Your monster's name is:", name)
print("Your monster's abilities are:", chosen_abilities[0], "and", chosen_abilities[1])
