# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/6
from requestsDemo1.game.game import Game


class HouYi(Game):
    ## 如果在子类中重新定义了__init__，那么父类__init__将会被覆盖
    def __init__(self):
        super().__init__(1000, 200)
        self.defense = 100

    # def houyi_fight(self,enemy_hp, enemy_power):
    #     final_hp = self.hp + self.defense - enemy_power
    #     enemy_final_hp = enemy_hp - self.power
    #
    #     if final_hp > enemy_final_hp:
    #         print("我赢了")
    #     elif final_hp < enemy_final_hp:
    #         print("敌人赢了")
    #     else:
    #         print("平局")

    def houyi_fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power

            if self.hp <= 0:
                print("我输了")
                break
            elif enemy_hp <= 0:
                print("敌人输了")
                break


hp = 1000
power = 200

houyi = HouYi()
houyi.houyi_fight(hp, power)
