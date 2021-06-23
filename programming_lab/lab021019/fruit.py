# -*- coding: utf-8 -*-
name = input("Enter your name")
fruit = input("Enter the fruit")
print(name, "loves to eat", fruit)
print(name + " loves to eat " + fruit)
print("%s loves to eat %s" % (name, fruit))
s = "{} loves to eat {}"
print(s.format(name, fruit))
