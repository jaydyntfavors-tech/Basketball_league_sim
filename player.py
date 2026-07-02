import random
from faker import Faker
from tabulate import tabulate

fake = Faker()

# 1. POSITIONS & ARCHETYPES SETUP
# Standard basketball positions
POSITIONS = ["PG", "SG", "SF", "PF", "C"]
# We will weight the league slightly toward guards/wings, making 7-foot centers a bit less common
POSITION_WEIGHTS = [25, 25, 20, 18, 12] 

ARCHETYPES = {
    "PG": ["Playmaker", "Shot Creator", "Floor General", "3-and-D Wing"],
    "SG": ["Sharpshooter", "Scoring Machine", "Lockdown Defender", "Slasher"],
    "SF": ["Two-Way Phenom", "Point Forward", "Slasher", "3-and-D Wing"],
    "PF": ["Stretch Four", "Paint Beast", "Glass Cleaner", "Post Playmaker"],
    "C":  ["Post Beast", "Rim Protector", "Stretch Big", "Glass Cleaner"]
}

# 2. HEIGHT & WEIGHT RULES
# Every height from 5'10" (70") to 7'3" (87")
ALL_POSSIBLE_HEIGHTS = list(range(70, 88))

# Probability weights for each height per position. 
# PG heavily favors 6'0"-6'4", but has a tiny micro-chance for 7'0"+
HEIGHT_WEIGHTS = {
    "PG": [10, 20, 25, 20, 15, 5, 3, 1, 0.5, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00001],
    "SG": [2, 5, 15, 25, 25, 15, 8, 3, 1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00001],
    "SF": [0.1, 0.5, 2, 8, 15, 25, 25, 15, 6, 2, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001],
    "PF": [0.0001, 0.001, 0.01, 0.1, 1, 4, 10, 20, 25, 20, 12, 5, 2, 0.5, 0.1, 0.05, 0.01, 0.005],
    "C":  [0.00001, 0.0001, 0.0005, 0.001, 0.01, 0.1, 0.5, 2, 5, 12, 20, 25, 20, 10, 4, 1, 0.2, 0.05]
}

class Player:
    def __init__(self):
        # Generate a realistic male name using Faker
        self.name = fake.name_male()
        
        # Age range for a standard league player
        self.age = random.randint(19, 38)
        
        # Roll for a random position based on position weights
        self.position = random.choices(POSITIONS, weights=POSITION_WEIGHTS, k=1)[0]
        
        # Roll for height based on that specific position's weights
        weights_for_pos = HEIGHT_WEIGHTS[self.position]
        self.height_inches = random.choices(ALL_POSSIBLE_HEIGHTS, weights=weights_for_pos, k=1)[0]
        
        # Roll for archetype matching their position
        self.archetype = random.choice(ARCHETYPES[self.position])
        
        # Generate a realistic weight that scales with their height
        self.weight_lbs = self.generate_dynamic_weight()
        
    def generate_dynamic_weight(self):
        # Baseline weight estimation formula: roughly 2.7 lbs per inch, adjusted up/down
        base_weight = int(self.height_inches * 2.7)
        
        # Give it some variance so players at the same height aren't identical weights
        # (e.g., a slim sniper vs. a bulky enforcer)
        weight_variance = random.randint(-25, 35)
        
        # Enforce hard limits so the physics stay somewhat normal
        final_weight = base_weight + weight_variance
        return max(160, min(final_weight, 310))

    def get_height_str(self):
        # Formats inches into standard feet'inches" basketball layout
        feet = self.height_inches // 12
        inches = self.height_inches % 12
        return f"{feet}'{inches}\""

# --- Test Script to verify generation works directly in terminal ---
if __name__ == "__main__":
    # Generate 15 random players to see the distribution
    test_roster = []
    for _ in range(15):
        test_roster.append(Player())
        
    # Format data for tabulate
    table_data = []
    for p in test_roster:
        table_data.append([p.name, p.age, p.position, p.get_height_str(), f"{p.weight_lbs} lbs", p.archetype])
        
    print("\n=== GENERATED PROSPECTS DISPLAY ===")
    print(tabulate(table_data, headers=["Name", "Age", "Pos", "Height", "Weight", "Archetype"]))


