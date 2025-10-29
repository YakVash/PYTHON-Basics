#A program for farmers and items river crossing
def is_safe(farmer, fox, goose, corn) :

    # Check for unsafe conditions: goose with fox or goose with corn without farmer
    if (goose == fox and farmer != goose) or (goose == corn and farmer != goose) :

        return False
    
    return True

def river_crossing(moves) :

    # Initial positions (all on the East side)
    farmer = fox = goose = corn = 'E'
    
    for move in moves.split() :

        # Move farmer and potentially an item
        if move == 'F' :  # Farmer moves with Fox

            if farmer == fox :  # Can only move fox if they're on the same side

                farmer = fox = 'W' if farmer == 'E' else 'E'

            else :

                return "Invalid move: Farmer and Fox not on the same side!"
            
        elif move == 'G' :  # Farmer moves with Goose

            if farmer == goose :

                farmer = goose = 'W' if farmer == 'E' else 'E'

            else :

                return "Invalid move: Farmer and Goose not on the same side!"
            
        elif move == 'C' :  # Farmer moves with Corn

            if farmer == corn :

                farmer = corn = 'W' if farmer == 'E' else 'E'

            else :

                return "Invalid move: Farmer and Corn not on the same side!"
            
        elif move == 'N' :  # Farmer moves alone

            farmer = 'W' if farmer == 'E' else 'E'

        else :

            return "Invalid input! Use F, G, C, or N only."

        # Check if the new state is safe
        if not is_safe(farmer, fox, goose, corn) :

            return "Unsafe state encountered!"

    # If all items safely reach the west side
    if farmer == fox == goose == corn == 'W' :

        return "All items are safe on the west side!"
    
    else :

        return "Not all items are on the west side yet."

# Example usage
moves = input("Enter the sequence of moves (F for Fox, G for Goose, C for Corn, N for Nothing): ").strip().upper()
result = river_crossing(moves)
print(result)
