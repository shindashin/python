coffee = ['americano', 'latte', 'vanilla']
price = [2500,3000,3500]
ediya=list(zip(coffee,price))
print(ediya)

starbucks = dict(zip(coffee,price))
print(starbucks)

#[{'name':'americano','price':3500},{'name':'americano','price':3500},{'name':'americano','price':3500},{'name':'americano','price':3500}]

starbucks=[{'coffeeName':c, 'coffeePrice':p} for c,p in zip(coffee,price)]
print(starbucks)


