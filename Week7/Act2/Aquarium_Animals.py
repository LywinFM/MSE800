# Define a class that will act as the Singleton for managing the aquarium
class AquariumManager:
    # Class-level variable to store the single instance
    _instance = None

    # __new__ controls object creation before __init__ runs
    def __new__(cls):
        # Check if an instance already exists
        if cls._instance is None:
            # If not, create a new instance using the parent class method
            cls._instance = super(AquariumManager, cls).__new__(cls)
            # Initialize a shared list to store fish in the aquarium
            cls._instance.fish_list = []
        # Return the same instance every time
        return cls._instance

    # Method to add a fish to the aquarium
    def add_fish(self, fish_type):
        self.fish_list.append(fish_type)  # Add fish to the list
        print(f"{fish_type} added to the Auckland Aquarium.")

    # Method to display all fish currently in the aquarium
    def show_fish(self):
        print("Current fish in the Auckland Aquarium:")
        for fish in self.fish_list:  # Loop through the list of fish
            print(f"- {fish}")


# Define constants for fish types
GOLDFISH = "Goldfish"
SHARK = "Shark"
ANGELFISH = "Angelfish"
TUNA = "Tuna"
SALMON = "Salmon"


# Create two variables pointing to the Singleton instance
aquarium1 = AquariumManager()  # First reference
aquarium2 = AquariumManager()  # Second reference (same instance)

# Add fish using the Singleton
aquarium1.add_fish(GOLDFISH)
aquarium1.add_fish(SHARK)
aquarium2.add_fish(ANGELFISH)  # Still modifies the same aquarium

# Display all fish in the aquarium
aquarium1.show_fish()