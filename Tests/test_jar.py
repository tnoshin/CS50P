
from jar import Jar

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'

def test_deposit():
    jar =Jar()
    jar.deposit(3)
    assert jar.size ==3


def test_withdraw():
    jar =Jar()
    jar.deposit(3)
    jar.withdraw(3)
    assert jar.size ==0

def test_init():
    jar = Jar()
    assert jar.capacity ==12

