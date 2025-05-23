import datatier

class Riven:
    def __init__(self, name, weapon, disposition, stats):
        self.name = name
        self.weapon = weapon
        self.disposition = disposition
        self.stats = stats

    def __repr__(self):
        return f"Riven(name={self.name}, weapon={self.weapon}, disposition={self.disposition}, stats={self.stats})"

