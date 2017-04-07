class Handler:

    def clear_screen():
        print("\033c", end="")

    def print_legend():
        """Print legend of board symbols"""
        print("Legend: Ships(| or -) Empty(O) Miss(.) Hit(*) Sunk(#)")
