#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Subpackage: fan:
Attributes:
    Name
    Favourite Player
    Purchased Merchandise
    Home City
Functions:
    Initialize Fan
    Update Favourite Player
    Update Purchased Merchandise Info (count of purchases, bool of if purchased, or array of items?. I'm thnking Count)
    Moved: Updates home city and country (if international)
Module: Domestic (Inherits Fan Properties)
Attributes:
    hasSeasonTickets
Functions:
    Initialize Domestic Fan
    updateTicketStatus
Module: International (Inherits Fan Properties)
Attributes:
    Home Country
    Functions:
Initialize Domestic Fan'''

class fan:
    def __init__(self, name, favouritePlayer, purchasedMerchandise, currentCity):
        self.name = name
        self.__favouritePlayer = favouritePlayer
        self.__purchasedMerchandise = purchasedMerchandise
        self.__currentCity = currentCity
        
    def getFavouritePlayer(self):
        return(self.__favouritePlayer)
        
    def setFavouritePlayer(self, newFavouritePlayer):
        self.__favouritePlayer = newFavouritePlayer
        
    def getPurchasedMerchandise(self):
        return(self.__purchasedMerchandise)
    
    def setPurchasedMerchandise(self, updateMerchandise):
        self.__purchasedMerchandise = updateMerchandise
    
    def getCurrentCity(self):
        return(self.__currentCity)
    
    def setCurrentCity(self, newCity):
        self.__currentCity = newCity

    def display(self):
        print("                 Name: {}\n     Favourite Player: {}\nPurchased Merchandise: {} \n         Current City: {}".format(self.name, self.getFavouritePlayer(), self.getPurchasedMerchandise(), self.getCurrentCity()))

