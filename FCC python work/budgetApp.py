class Category:
    def __init__(self, budgetType: str):
        self.type = budgetType
        self.ledger = []
        self.balance = 0.00
    
    def deposit(self, value, text:str = ''):
        self.ledger.append({'amount': float(value), 'description':text})
        self.balance += float(value)

    def withdraw(self, value, text:str = ''):
        if self.check_funds(value):
            self.ledger.append({'amount': 0-abs(float(value)), 'description':text})
            self.balance -= abs(float(value))
            return True
        return False

    def get_balance(self):
        return self.balance

    def check_funds(self, value):
        if abs(float(value)) > self.balance:
            return False
        return True
    
    def transfer(self, value, cat):
        if self.check_funds(value):
            self.withdraw(value, f'Transfer to {cat.type}')
            cat.deposit(value, f'Transfer from {self.type}')
            return True
        return False

    def __str__(self):
        final = ''
        if len(self.type) >= 30:
            final += self.type[0:30]+'\n'
        else: 
            startingStars = round((30-len(self.type))/2)
            final += '*'*startingStars + str(self.type) + '*' * (30 - (startingStars + len(self.type)))+'\n'
        for ind, item in enumerate(self.ledger):
            lenDesc = len(item['description'][0:23])
            strAmtList = [str(item['amount']).split('.')[0], str(item['amount']).split('.')[1]]
            if len(strAmtList[1]) == 1:
                strAmtList[1] += '0'
            strAmt = '.'.join(strAmtList)
            string = item['description'][0:23] + strAmt.rjust(30-lenDesc)+'\n'
            final+=string
        total = '.'.join([str(self.balance).split('.')[0], str(self.balance).split('.')[1][0:2]])
        final += f'Total: {total}'
        return final


def create_spend_chart(categoryList:list):
    percentArr = []
    for num in range(len(categoryList)):
        percentArr.append(0)
    totalSpent = 0
    for ind, item in enumerate(categoryList):
        for entry in item.ledger:
            if entry['amount'] < 0:
                totalSpent += abs(entry['amount'])
                percentArr[ind] += abs(entry['amount'])
    for ind, item in enumerate(percentArr):
        percentArr[ind] = round((((int(item)/totalSpent)*100)//10)*10)
    histogram = 'Percentage spent by category\n'
    
    for i in range(100,-1,-10):
        histogram += f'{i}|'.rjust(4)
        for ind, cat in enumerate(categoryList):
            if percentArr[ind] >= i:
                histogram += ' o '
            else:
                histogram += '   '
        histogram += ' \n'
    histogram += '    ' + ('-'* len(percentArr)*3) + '-'
    listCopy = list(map(lambda x: x.type, categoryList))
    longest = len(max(listCopy, key=len))
    for i in range(longest):
        histogram += '\n    '
        for j in range(len(categoryList)):
            try:
                histogram += f' {listCopy[j][i]} '
            except IndexError:
                histogram += '   '
        histogram += ' '
    return histogram
    
        

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)


print(food)
print(clothing)
print(auto)


print(create_spend_chart([food, clothing, auto]))