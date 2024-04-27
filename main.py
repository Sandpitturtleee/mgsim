from src.Player.hunter import Hunter
from src.Player.mage import Mage
from src.Player.warrior import Warrior

if __name__ == "__main__":
    m1 = Mage(lvl_p=64, lvl_e=64)
    h1 = Hunter(lvl_p=64, lvl_e=64)
    w1 = Warrior(lvl_p=40, lvl_e=64)
    print(vars(m1))
    print(vars(h1))
    print(vars(w1))

