
import tkinter as tk
from tkinter import ttk
from tennis_score_logic import TennisScore

class TennisScoreGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Tennis Score Manager")

        self.score_manager = TennisScore("Player 1", "Player 2")

        # Player Names
        self.player1_name_var = tk.StringVar(value="Player 1")
        self.player2_name_var = tk.StringVar(value="Player 2")

        self.player1_name_entry = ttk.Entry(self, textvariable=self.player1_name_var)
        self.player1_name_entry.grid(row=0, column=0, padx=10, pady=10)

        self.player2_name_entry = ttk.Entry(self, textvariable=self.player2_name_var)
        self.player2_name_entry.grid(row=0, column=2, padx=10, pady=10)

        # Score Display
        self.score_display_var = tk.StringVar(value="0 - 0")
        self.score_display_label = ttk.Label(self, textvariable=self.score_display_var, font=("Arial", 24))
        self.score_display_label.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.add_point_player1_button = ttk.Button(self, text="Add Point", command=self.add_point_player1)
        self.add_point_player1_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_point_player1_button = ttk.Button(self, text="Remove Point", command=self.remove_point_player1)
        self.remove_point_player1_button.grid(row=3, column=0, padx=10, pady=10)

        self.add_point_player2_button = ttk.Button(self, text="Add Point", command=self.add_point_player2)
        self.add_point_player2_button.grid(row=2, column=2, padx=10, pady=10)

        self.remove_point_player2_button = ttk.Button(self, text="Remove Point", command=self.remove_point_player2)
        self.remove_point_player2_button.grid(row=3, column=2, padx=10, pady=10)

        self.update_display()

    def add_point_player1(self):
        self.score_manager.add_point_player1()
        self.update_display()

    def add_point_player2(self):
        self.score_manager.add_point_player2()
        self.update_display()

    def remove_point_player1(self):
        self.score_manager.remove_point_player1()
        self.update_display()

    def remove_point_player2(self):
        self.score_manager.remove_point_player2()
        self.update_display()

    def update_display(self):
        current_score = self.score_manager.get_current_score()
        game_score = f"{current_score['game_points'][0]} - {current_score['game_points'][1]}"
        set_score = f"{current_score['set_points'][0]} - {current_score['set_points'][1]}"
        match_score = f"{current_score['match_points'][0]} - {current_score['match_points'][1]}"
        self.score_display_var.set(f"Game: {game_score} | Set: {set_score} | Match: {match_score}")

if __name__ == '__main__':
    app = TennisScoreGUI()
    app.mainloop()
