#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Michael Alonso
Class: CS 521 - Spring 1
Date: 03/03/2020
Final Project
Class CoffeeShops creates objects with passed arguements name, city, int(rank),
and favorite drink
"""


class CoffeeShops:
    '''
    This class constructs the CoffeeShops objects and its contents
    '''
    def __init__(self, name, city='BIRMINGHAM', rank=5, favorite_drink='DRIP'):
        self.__city = city.upper()
        self.__local = True

        self.name = name.upper()
        self.rank = rank
        self.favorite_drink = favorite_drink.upper()

    def __str__(self):
        return ("{name} is a {location} coffee shop with a rank of {rank}. "
                "The {drink} is the best.".format(
                        name=self.name,
                        location=('local' if self.get_local()
                                  is True else self.__city),
                        rank=self.rank,
                        drink=self.favorite_drink))

    def __set_local(self):
        '''
        Return the variable local boolean value
        '''
        if self.__city == 'BIRMINGHAM':
            return self.__local is True
        else:
            return self.__local is False

    def get_local(self):
        '''
        Return the variable local boolean value
        '''
        return (self.__set_local())

    def get_name(self):
        '''
        Return the name
        '''
        return self.name

    def get_rank(self):
        '''
        Return the rank
        '''
        return self.rank

    def get_city(self):
        '''
        Return the city
        '''
        return self.__city

    def get_favorite_drink(self):
        '''
        Return the favorite drink
        '''
        return self.favorite_drink

    def __update_city(self, city):
        '''
        Set the city of Coffee Shop
        '''
        self.__city = city.upper()

    def __update_name(self, name):
        '''
        Set the name of Coffee Shop
        '''
        self.name = name.upper()

    def __update_rank(self, rank):
        '''
        Set the rank of Coffee Shop
        '''
        self.rank = rank

    def __update_favorite_drink(self, drink):
        '''
        Set the favorite drink of Coffee Shop
        '''
        self.favorite_drink = drink.upper()

    def update_shop(self, selection, update):
        '''
        Update name, rank, favorite drink, or city of coffee shop
        '''
        if selection == 1:
            self.__update_name(update)

        elif selection == 2:
            self.__update_rank(update)

        elif selection == 3:
            self.__update_favorite_drink(update)

        elif selection == 4:
            self.__update_city(update)
        else:
            return 'Selection invalid'


if __name__ == '__main__':

    city_local = 'BIRMINGHAM'
    city_non_local = 'BOSTON'
    name = 'REVELATOR'
    rank = 3
    drink = 'POUR OVER'

    shop = CoffeeShops(name, city_local, rank, drink)
    shop2 = CoffeeShops('Seeds', city_non_local)

    assert shop.get_local() is True, (
            'Error setting local True, {} != {}'.
            format(shop.get_city(), city_local))

    assert shop2.get_local() is False, (
            'Error setting local False, {} != {}'.format(shop2.get_city(),
                                                         city_non_local))

    assert shop.get_name() == name, (
            'Error matching name, {} != {}'.format(shop.get_name(), name))

    assert shop.get_rank() == rank, (
            'Error matchin rank, {} != {}'.format(shop.get_rank(), rank))

    assert shop.get_favorite_drink() == drink, (
            'Error matching rank, {} != {}'.format(shop.get_favorite_drink(),
                                                   drink))

    assert shop.get_city() == city_local, (
            'Error matching rank, {} != {}'.
            format(shop.get_city(), city_local))

    shop2.update_shop(1, name)
    assert shop2.get_name() == name, (
            'Error updating name, {} != {}'.format(shop2.get_name(), name))

    shop2.update_shop(2, rank)
    assert shop2.get_rank() == rank, (
            'Error updating rank, {} != {}'.format(shop2.get_rank(), rank))

    shop2.update_shop(3, drink)
    assert shop2.get_favorite_drink() == drink, (
            'Error updating favorite drink, {} != {}'.
            format(shop2.get_favorite_drink(), drink))

    shop2.update_shop(4, city_local)
    assert shop2.get_city() == city_local, (
            'Error updating city, {} != {}'.
            format(shop2.get_city(), city_local))
