# # 내편 피카츄
# pikachu_1_hp = 100
# # 상대편 피카츄
# pikachu_2_hp = 100


class Pikachu:
    def __init__(self):
        self.health = 100
        self.energy = 0

pikachu_1_hp = Pikachu()
pikachu_2_hp = Pikachu()

pikachu_1_hp.health = pikachu_1_hp.health - 20

print(pikachu_1_hp.health, pikachu_2_hp.health)