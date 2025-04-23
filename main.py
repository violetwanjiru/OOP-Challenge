#Creating objects
from pet import Pet

# Create a new pet
my_pet = Pet("Buddy")

# Initial status
print("Initial status:")
my_pet.get_status()

# Test eat method
print("\nAfter eating:")
my_pet.eat()
my_pet.get_status()

# Test sleep method
print("\nAfter sleeping:")
my_pet.sleep()
my_pet.get_status()

# Test play method
print("\nAfter playing:")
my_pet.play()
my_pet.get_status()

# Test training and showing tricks
print("\nTraining Buddy:")
my_pet.train("roll over")
my_pet.train("sit")
my_pet.train("roll over")  # duplicate test

print("\nShowing tricks:")
my_pet.show_tricks()
