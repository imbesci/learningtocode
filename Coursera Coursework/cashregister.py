class CashRegister:
    '''A cash register.'''

    def __init__(self, loonies, toonies, fives, tens, twenties):
        '''
        >>> register = CashRegister(5,5,5,5,5)
        >>> register.loonies
        5
        >>> register.toonies
        5
        >>> register.twenties
        5
        '''

        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def __eq__(self, other):
        '''
        >>> reg = CashRegister(2,0,0,0,0)
        >>> reg2 = CashRegister(0,1,0,0,0)
        >>> reg1 == reg2
        True
        '''

        return self.gettotal() == other.gettotal()
    
    def __str__(self):

        return 'Cash Register: ' + \
            '${0} ($1x{1}, $2x{2}, $5x{3}, $10x{4}, $20x{5})'.format(
                self.gettotal(), self.loonies, self.toonies, self.fives, self.tens, self.twenties)

##        return 'Cash Register: $' + str(self.gettotal()) + ' ($1x' + str(self.loonies) + \
##            ', $2x' + str(self.toonies) + ', $5x' + str(self.fives) + ', $10x' + str(self.tens) + ', $20x' + str(self.twenties) + ')'
    

    def gettotal(self):
        '''Return the total money in the cash register'''
        return (self.loonies)+(self.toonies * 2) + (self.fives * 5) + (self.tens * 10) + (self.twenties * 20)

    def add(self, count, denom):
        '''Add currency to the cash register'''
        if denom == 'loonies':
            self.loonies += count
        elif denom == 'toonies':
            self.toonies += count
        elif denom == 'fives':
            self.fives += count
        elif denom == 'tens':
            self.tens += count
        elif denom == 'twenties':
            self.twenties += count

    def remove(self, count, denom):
        '''Add currency to the cash register'''
        if denom == 'loonies':
            self.loonies -= count
        elif denom == 'toonies':
            self.toonies -= count
        elif denom == 'fives':
            self.fives -= count
        elif denom == 'tens':
            self.tens -= count
        elif denom == 'twenties':
            self.twenties -= count
    
    
if __name__ == '__main__':
##    #A cash register with 5 loonies, 5 toonies, 5 fives, 5 tens, and 5 twenties
##    #loonie = 1 dollar coin, toonie = 2 dollar coin
##    #total == 190
##
##    register = CashRegister(5,5,5,5,5)
##    print(register.gettotal())
##
##    register.add(3, 'toonies')
##    register.remove(2, 'twenties')
##    print(register.gettotal())
    cr1 = CashRegister(2,0,0,0,0)
    cr2 = CashRegister(0,1,0,0,0)
    cr3 = CashRegister(1,1,0,0,0)
    print(cr1)
    print(cr1 == cr2)
    print(cr2 == cr3)
