from src.config_loader import GameConfig
from src.games.game import Game
from src.rng import RandomSource


if __name__ == "__main__":
    cfg = GameConfig("config.yaml")
    game = Game(random_source=RandomSource(), config=cfg)
    game.run(num_spins=1_000_000)
