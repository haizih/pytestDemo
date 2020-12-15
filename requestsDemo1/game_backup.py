# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/6

class Game:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

"""
第二个角色，他叫后裔，后裔继承了角色的 hp 和 power。并多了护甲属性.
houyi_hp = hp + defense - enemy_power
"""
class HouYi(Game):
    ## 如果在子类中重新定义了__init__，那么父类__init__将会被覆盖
    def __init__(self):
        super().__init__(1000,200)
        self.defense = 100

    def houyi_fight(self,enemy_hp, enemy_power):
        final_hp = self.hp + self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")


hp = 1000
power = 400

houyi = HouYi()
houyi.houyi_fight(hp, power)



