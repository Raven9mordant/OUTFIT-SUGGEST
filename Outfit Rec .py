class Outfit:
    def __init__(self, model_name, colors):
        self.model_name = model_name
        self.colors = colors  # List of colors available for this outfit

    def __str__(self):
        return f"{self.model_name} - Available colors: {', '.join(self.colors)}"


class OutfitRecommender:
    def __init__(self, outfits):
        self.outfits = outfits

    def recommend_by_color(self, preferred_color):
        recommended_outfits = []
        for outfit in self.outfits:
            if preferred_color.lower() in (color.lower() for color in outfit.colors):
                recommended_outfits.append(outfit)
        return recommended_outfits

    def recommend_based_on_trend(self, recommended_color):
        # This can be adjusted to provide a color-based recommendation
        return self.recommend_by_color(recommended_color)


# Sample outfits
outfits = [
    Outfit("Casual T-shirt", ["Red", "Blue", "White"]),
    Outfit("Summer Dress", ["Yellow", "White", "Pink"]),
    Outfit("Sports Jacket", ["Black", "Grey", "Navy"]),
    Outfit("Evening Gown", ["Gold", "Black", "Silver"]),
    Outfit("Jeans and Hoodie", ["Grey", "Black", "Blue"]),
    Outfit("Business Suit", ["Black", "Navy", "Charcoal"]),
]

# Instantiate OutfitRecommender with sample outfits
outfit_recommender = OutfitRecommender(outfits)

def show_outfits_based_on_color():
    # Ask user for their preferred color or recommended color
    print("Welcome to the Outfit Recommender!")
    print("You can either:")
    print("1. Choose your favorite color.")
    print("2. See outfits recommended for a specific color.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        favorite_color = input("Enter your favorite color: ").strip()
        recommended_outfits = outfit_recommender.recommend_by_color(favorite_color)
    elif choice == "2":
        recommended_color = input("Enter a recommended color (e.g., Black, White, Red, etc.): ").strip()
        recommended_outfits = outfit_recommender.recommend_based_on_trend(recommended_color)
    else:
        print("Invalid choice, please try again.")
        return
    
    if recommended_outfits:
        print("\nOutfits based on your selection:")
        for outfit in recommended_outfits:
            print(outfit)
    else:
        print(f"No outfits found for color: {favorite_color if choice == '1' else recommended_color}")

show_outfits_based_on_color()