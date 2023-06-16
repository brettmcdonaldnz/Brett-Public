# By Brett McDonald
# SID: 10158931
# Assignment 2A
# Question 1: Sale Price Table

normalPriceList = [9.95, 14.95, 19.95, 24.95, 29.95, 34.95, 39.95, 44.95, 49.95] # for generating the normal price row

discountList = [5,10,15,20,25,30,35,40,45,50] # for percent discounts

print('\t\t\t\t**Sale prices**') # table header

print('Normal price:\t',end='') # set up normal price row

for i in normalPriceList:
    print('${}\t'.format(i),end='') # generate column headers

print('\n---------------------------------------------------------------------------------------') # table boundary

rowString = '' # initiate row with rowString

for j in discountList:
    for k in normalPriceList:
        rowString += str('{:.2f}\t'.format((k*(100-j))/100)) # apply discount to each normal price and add result to rowString

    if j == discountList[0]: # This ensures only the first row of discount prices will show '%off' at the start of the row
        print('\t%off: {}%   '.format(j),rowString) # print the discount values as a row
        rowString = '' # reset the rowString to empty

    else:
        print('\t\t {}%   '.format(j),rowString) # print discount percentage and results for all other rows
        rowString = ''

