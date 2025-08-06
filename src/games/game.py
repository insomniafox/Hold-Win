from typing import Optional

from src.config_loader import GameConfig
from src.games.base import BaseGame
from src.models.game_model import GameModel
from src.constants import SYMBOL_REGULAR, SYMBOL_BONUS
from src.rng import RandomSource


class Game(BaseGame):
    def __init__(
        self,
        random_source: Optional[RandomSource] = None,
        config: Optional[GameConfig] = None
    ):
        super().__init__(random_source=random_source)
        self.model_cls = GameModel
        self.cfg = config

    def handler_init(self):
        self.ctx = self.model_cls.blank()
        self.ctx['spins'] = self.model_cls.spins()
        self.ctx['bonus'] = self.model_cls.bonus()
        self.cur['bet'] = self.cfg.BET_AMOUNT
        self.cur['balance'] = self.cfg.INITIAL_BALANCE
        self.cur['bonus_triggered'] = False
        self.cur['spin_win'] = 0
        self.cur['bonus_total_win'] = 0

    def handler_spin(self):
        self.cur['spin_win'] = 0
        self.cur['board'] = [SYMBOL_REGULAR for _ in range(5)]
        bonus_chance = self.get_next_random()

        if bonus_chance < self.cfg.BONUS_TRIGGER_CHANCE:
            self.cur['board'][2] = SYMBOL_BONUS
            self.cur['bonus_triggered'] = True
        else:
            win = (
                self.get_next_random()
                % (self.cfg.SPIN_WIN_MAX - self.cfg.SPIN_WIN_MIN + 1)
                + self.cfg.SPIN_WIN_MIN
            )
            self.cur['balance'] += win
            self.cur['spin_win'] = win
            self.cur['bonus_triggered'] = False

    def handler_bonus_init(self):
        self.ctx['bonus'] = self.model_cls.bonus()
        self.cur['rounds_left'] = self.ctx['bonus']['rounds_left']
        self.cur['bonus_symbols'] = []
        self.cur['bonus_total_win'] = 0
        self.cur['bonus_turns'] = 0
        self.cur['bonus_fail_streak'] = 0

    def handler_bonus(self):
        self.cur['bonus_turns'] += 1

        # 1. Прекращаем бонус, если превысили лимит по общим ходам
        if self.cur['bonus_turns'] > self.cfg.BONUS_MAX_TURNS:
            self.cur['rounds_left'] = 0
            return

        # 2. Пытаемся получить символ
        symbol_roll = self.get_next_random()

        if symbol_roll < self.cfg.BONUS_SYMBOL_CHANCE:
            new_value = (
                self.get_next_random()
                % (self.cfg.BONUS_SYMBOL_MAX_VALUE - self.cfg.BONUS_SYMBOL_MIN_VALUE + 1)
                + self.cfg.BONUS_SYMBOL_MIN_VALUE
            )
            self.cur['bonus_symbols'].append(new_value)
            self.cur['rounds_left'] = self.ctx['bonus']['rounds_left']
            self.cur['bonus_fail_streak'] = 0
        else:
            self.cur['rounds_left'] -= 1
            self.cur['bonus_fail_streak'] += 1

        # 3. Прекращаем бонус, если достигли лимита подряд неудач
        if self.cur['bonus_fail_streak'] >= self.cfg.BONUS_ATTEMPTS:
            self.cur['rounds_left'] = 0

        # 4. Если игра окончена — начисляем выигрыш
        if self.cur['rounds_left'] == 0:
            total_bonus_win = sum(self.cur['bonus_symbols'])
            self.cur['balance'] += total_bonus_win
            self.cur['bonus_total_win'] = total_bonus_win
