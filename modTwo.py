import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.spesh_attack = attack_power
        # self.attacking = attack_power

    def attack(self, opponent):
        # for i in range(0,20):
        self.attack_power = random.randrange(20)
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def spesh(self, opponent):
        opponent.health -= self.spesh_attack
        print(f"{self.name} uses special ability for {self.spesh_attack} damage")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        x = self.max_health - self.health
        if self.health < self.max_health:
            self.health = self.health + x
            
        print(f"You have been restored to {self.health} health.")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        attacking = random.randrange(25)
        super().__init__(name, health=140, attack_power=attacking)  # Boost health and attack power
        

    # Add your power attack method here


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        attacking = random.randrange(35)
        super().__init__(name, health=100, attack_power=attacking)  # Boost attack power

    # Add your cast spell method here
# Giant class (Inherits from Character)
class Giant(Character):
    def __init__(self, name):
        attacking = random.randrange(55)
        super().__init__(name, health=150, attack_power=attacking)
    def special(self):
        self.attack_power = 65
        print(f"{self.name} gives a Holy Strike for {self.attack_power} damage!")
        

class Reptile(Character):
    def __init__(self, name):
        attacking = random.randrange(40)
        super().__init__(name, health=135, attack_power=attacking)


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        attacking = random.randrange(15)
        super().__init__(name, health=150, attack_power=attacking)  # Lower attack power
        
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Giant")  # Add Scratcher
    print("4. Reptile")  # Add Alaado
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Giant(name)
    elif class_choice == '4':
        return Reptile(name)
    # elif class_choice == 'quit':
    #     exit
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        prompt = "Choose an action "
        prompt += "\nOr enter 'quit' to quit: " 
        choice = input(prompt)

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.spesh(wizard)
           
        elif choice == '3':
            # Call the heal method here
            player.heal()
        elif choice == '4':
            player.display_stats()
        elif choice == 'quit':
            break
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()