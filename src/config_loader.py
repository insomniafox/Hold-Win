import yaml


class GameConfig:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        self.INITIAL_BALANCE = data["initial_balance"]
        self.BET_AMOUNT = data["bet_amount"]
        self.SPIN_WIN_MIN = data["spin_win_min"]
        self.SPIN_WIN_MAX = data["spin_win_max"]
        self.BONUS_TRIGGER_CHANCE = data["bonus_trigger_chance"]
        self.BONUS_SYMBOL_CHANCE = data["bonus_symbol_chance"]
        self.BONUS_SYMBOL_MIN_VALUE = data["bonus_symbol_min_value"]
        self.BONUS_SYMBOL_MAX_VALUE = data["bonus_symbol_max_value"]
        self.BONUS_ATTEMPTS = data["bonus_attempts"]
        self.BONUS_MAX_TURNS = data["bonus_max_turns"]
