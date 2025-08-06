import random
import time


class RandomSource:
    def __init__(self, source=None, seed=None, size=100_000):
        if source is not None:
            self.src = source
        else:
            if seed is None:
                seed = int(time.time() * 1000)
                print(f"[RandomSource] Auto-seed used: {seed}")
            self.seed = seed
            rnd = random.Random(seed)
            self.src = [rnd.randint(0, 100) for _ in range(size)]
        self.index = 0

    def get(self):
        value = self.src[self.index % len(self.src)]
        self.index += 1
        return value
