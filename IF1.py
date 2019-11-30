
# age=int(input('Введите возраст:\n'))

# def ask_for_age (age):
#     if age < 7:
#         return 'Детский сад'
#     elif 7 <= age <= 17:   
#         return 'Школа'
#     elif 17 <= age <= 22: 
#         return 'Вуз'
#     else:
#         return 'Работа'


# print(ask_for_age(age))

def check (discount, price):
    if type(discount) != str or type(price) != str:
        return '0'
    elif discount==price:
        return '1'
    elif len(discount)>len(price):
        return '2'
    elif price=="learn":
        return '3'
discount="пять"
price="learn"
print (check(discount,price))



    
     