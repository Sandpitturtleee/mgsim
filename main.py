from src.Items.rings import Rings
from src.Player.blade_dancer import BladeDancer
from src.Player.hunter import Hunter
from src.Player.mage import Mage
from src.Player.paladin import Paladin
from src.Player.tracker import Tracker
from src.Player.warrior import Warrior

if __name__ == "__main__":
    m1 = Mage(lvl_p=64, lvl_e=64)
    h1 = Hunter(lvl_p=64, lvl_e=64)
    w1 = Warrior(lvl_p=64, lvl_e=64)
    t1 = Tracker(lvl_p=64, lvl_e=64)
    p1 = Paladin(lvl_p=64, lvl_e=64)
    bd1 = BladeDancer(lvl_p=64, lvl_e=64)
    # print(f"Mag: {vars(m1)}")
    # print()
    # print(f"Pal: {vars(p1)}")
    # print()
    # print(f"Trop: {vars(t1)}")
    # print()
    # print(f"Woj: {vars(w1)}")
    # print()
    # print(f"Łowca: {vars(h1)}")
    # print()
    # print(f"Tancerz: {vars(bd1)}")
    # print()

    r1 = Rings(lvl=40, rarity_lvl=3)
    print(f"Pierścień: {vars(r1)}")
