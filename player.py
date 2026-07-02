import random 
from faker import faker
from tabulate import tabulate 

faker = Faker()

#positions and archtypes
positions = ["PG","SG","SF","PF","C"]
# PG=25% SG=25% SF=20% PF=15% C=15%
positions_weights =[25,25,20,15,15]

Archetypes ={
  "PG": ["Playmaker", "Shot Creator", "Floor General, "3-and-D Point"],
  "SG": ["Sharpshooter", "Scoring Machine", "Lockdown Defender", "Slasher"],
  "SF": ["Two-Way Phenom", "Point Foward", "Slasher", "3-and-D Wing"],
  "PF": ["Stretch Four", "Paint Beast", "Glass Cleaner", "Post Playmaker"],
  "C": ["Post Beast", "Rim Protector", "Stretch Big", "Glass Cleaner"],
  }

All_possible_heights = list(range(70,88))
Height_Weights = {
"PG": [10, 20, 25, 20, 15, 5, 3, 1, 0.5, 0.2, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00001],
"SG": [2, 5, 15, 25, 25, 15, 8, 3, 1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00001],
"SF": [0.1, 0.5, 2, 8, 15, 25, 25, 15, 6, 2, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00001],
"PF": [0.0001, 0.001, 0.01, 0.1, 1, 4, 10, 20, 25, 20, 12, 5, 2, 0.5, 0.1, 0.05, 0.01, 0.005],
"C": [0.00001, 0.0001, 0.0005, 0.001, 0.01, 0.1, 0.5, 2, 5, 12, 20, 25, 20, 10, 4, 1, 0.2, 0.05]
}

class Player:
    def__init__(self):
      # Name generator
      self.name = fake.name_male()
      # age generator
      self.age = random.randint(19, 40)
      #position Generator
      self.position = random.choices(positions, weights = positions_weights, k=1)[0]
      # Height Generator
      weights_for_pos = height_weights[self.position]
      self.height_inches = random.choices(All_possible_heights, weights = weights_for_pos, k=1) [0]
      #archetypes generator
      self.archetype = random.choice(Archetypes[self.position])
      self.weight_lbs = self.generate_dynamic_weight()
    
    def generate_dynamic_weight(self):
        base weight = int(self.height_inches * 2.7)
        # weight variance 
        weight_variance = random.randint(-25, 35)
        final_weight = base_weight + weight_variance
        return max(160, min(final_weight, 310))

    def get_height_str(self):
        # Formats inches to foot'inches
        feet = self.height_inches // 12
        inches = self.height_inches % 12
        return f"{feet}'{inches}/""

_______________________## test ## ___________

if __name__ == "__main__":
test_roster =[]
for _ in range(15):
    test_roster.append(player())

