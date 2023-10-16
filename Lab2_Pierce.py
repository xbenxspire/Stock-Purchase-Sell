'''
Lab 2 stock purchase/sell program
Date: Sep 1, 2023
@author: Benjamin Pierce
'''
#Shares bought
bought = float(input('Enter number of shares to purchase: '))

#Share purchase price
purchasePrice = float(input('Amount paid per share: '))
purchaseTotal = bought * purchasePrice
print(f'You paid ${purchaseTotal:.2f} for the stock')

#Stockbroker commission for purchase
commissionP = purchaseTotal * 0.03
print(f'You paid your broker ${commissionP} for the purchase')

#Shares sold
sold = float(input('Enter number of shares to sell: '))

#Share sell price
sellPrice = 2.25 * purchasePrice
sellTotal = sold * sellPrice
print(f'You made ${sellTotal:.2f} off the stock')

#Stockbroker commission for sale
commissionS = sellTotal * 0.03
print(f'You paid your broker ${commissionS} for the sale')

#Display amount leftover.
initialPayment = purchaseTotal + commissionP
finalSale = sellTotal - commissionS
difference = finalSale - initialPayment
print(f'You made ${difference:.2f}')

#If positive, print "You made a profit!", else if negative print "You lost money."
if finalSale > initialPayment:
    print('You made profit!')
    
else:
    print('You lost money.')