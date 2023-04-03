# This is a sample Python script.
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from problema2 import Flower

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from problem1 import Sport

sport=Sport('data/sports.csv')
sport.readFile()
sport.calculate()
sport.plotValuesWeight()
# sport.plotValuesWaist()
# sport.plotValuesPulse()

# flori=Flower('data/flowers.csv')
# flori.readFile()
# flori.calculateAccuracy()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
