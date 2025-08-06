from typing import Optional

from src.config_loader import GameConfig
from src.rng import RandomSource


class BaseGame:
    def __init__(
        self,
        random_source: Optional[RandomSource] = None,
        config: Optional[GameConfig] = None
    ):
        self.ctx = {}
        self.cur = {}
        self.random_source = random_source or RandomSource()
        self.config = config
        self.setup_states()
        self.current_state = 'init'

    def setup_states(self):
        self.states = {
            'init': self.handler_init,
            'spin': self.handler_spin,
            'bonus_init': self.handler_bonus_init,
            'bonus': self.handler_bonus,
        }

    def run(self, num_spins=1000):
        total_spins = 0
        total_bonus_games = 0
        total_win = 0
        total_bet = 0

        self.handler_init()
        print(f"Game initialized with starting balance: {self.cur['balance']}")

        while total_spins < num_spins:
            self.current_state = 'spin'
            self.handler_spin()
            total_spins += 1
            total_bet += self.cur['bet']
            total_win += self.cur.get('spin_win', 0)

            if self.cur.get('bonus_triggered'):
                total_bonus_games += 1
                self.handler_bonus_init()
                while self.cur['rounds_left'] != 0:
                    self.handler_bonus()
                    total_win += self.cur.get('bonus_total_win', 0)

        rtp = (total_win / total_bet) * 100 if total_bet else 0

        print(f"Simulation completed after {total_spins} spins.")
        print(f"Total bonus games triggered: {total_bonus_games}")
        print(f"Final balance: {self.cur['balance']}")
        print(f"Total win accumulated: {total_win}")
        print(f"Total bet amount: {total_bet}")
        print(f"Calculated RTP: {rtp:.2f}%")

    def get_next_random(self):
        return self.random_source.get()

    def handler_init(self):
        raise NotImplementedError

    def handler_spin(self):
        raise NotImplementedError

    def handler_bonus_init(self):
        raise NotImplementedError

    def handler_bonus(self):
        raise NotImplementedError
