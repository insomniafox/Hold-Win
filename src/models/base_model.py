class BaseModel:
    @classmethod
    def blank(cls):
        return {}

    @classmethod
    def spins(cls):
        return {'round_win': 0}

    @classmethod
    def bonus(cls):
        return {'round_win': 0, 'rounds_left': 3}
