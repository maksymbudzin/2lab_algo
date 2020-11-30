class Hamster:
    def __init__(self, daily_norm, greed):
        self.daily_norm = daily_norm
        self.greed = greed

    def __str__(self):
        return (f"Daily norm:{self.daily_norm}  greed:{self.greed}")
