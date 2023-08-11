
class TennisScore:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.game_points = [0, 0]
        self.set_points = [0, 0]
        self.match_points = [0, 0]
        self.score_history = []

    def _add_score_history(self):
        self.score_history.append(
            (self.game_points.copy(), self.set_points.copy(), self.match_points.copy())
        )

    def _increment_game_point(self, player_index):
        if self.game_points[player_index] == 40:
            self._add_score_history()
            self.game_points[player_index] = 0
            self.game_points[1 - player_index] = 0
            self._increment_set_point(player_index)
        else:
            self.game_points[player_index] = {0: 15, 15: 30, 30: 40}[self.game_points[player_index]]

    def _decrement_game_point(self, player_index):
        self.game_points[player_index] = {15: 0, 30: 15, 40: 30}.get(self.game_points[player_index], 0)

    def _increment_set_point(self, player_index):
        if self.set_points[player_index] == 6:
            self.set_points[player_index] = 0
            self.set_points[1 - player_index] = 0
            self._increment_match_point(player_index)
        else:
            self.set_points[player_index] += 1

    def _decrement_set_point(self, player_index):
        if self.set_points[player_index] > 0:
            self.set_points[player_index] -= 1

    def _increment_match_point(self, player_index):
        self.match_points[player_index] += 1

    def _decrement_match_point(self, player_index):
        if self.match_points[player_index] > 0:
            self.match_points[player_index] -= 1

    def add_point_player1(self):
        self._increment_game_point(0)
        self._add_score_history()

    def add_point_player2(self):
        self._increment_game_point(1)
        self._add_score_history()

    def remove_point_player1(self):
        self._decrement_game_point(0)
        self._add_score_history()

    def remove_point_player2(self):
        self._decrement_game_point(1)
        self._add_score_history()

    def get_current_score(self):
        return {
            "player1_name": self.player1_name,
            "player2_name": self.player2_name,
            "game_points": self.game_points,
            "set_points": self.set_points,
            "match_points": self.match_points,
            "score_history": self.score_history,
        }
