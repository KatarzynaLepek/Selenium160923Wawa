#import pytest_funkcje    <- bezpieczniejsza opcja
#pytest_funkcje_kasia.dodawanie()

from pytest_funkcje_kasia import *

#def test_dodawanie1():
#    assert dodawanie(3,5) == 8
#    assert dodawanie(3,2) == 8

#def test_dodawanie2():
#    assert dodawanie(1,1) == 2

#def test_mnozenie():
#    assert mnozenie(10,5) == 50
#    assert mnozenie(10, 1.1) == 11
#    assert mnozenie(100, 1.1) == 110
#    assert mnozenie(2, 'mama') == 'mamamama'

def test_fizzbuzz_basic():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(9) == "fizz"
    assert fizzbuzz(15) == "fizzbuzz"

def test_fizzbazz_advanced():
    assert fizzbuzz(0) == None
    assert fizzbuzz(-5) == None
    assert fizzbuzz(5.8) == 'buzz'
    assert fizzbuzz("mama") == None