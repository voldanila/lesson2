# # balance = 5
# # price = 10


# # print(bool(balance < 0 or price > balance))

# # if balance < 0 or price > balance:
# #     print('eee')

# # balance = 5
# # price = 10

# # if balance > price:
# #     print('Thanks!')
# # else:
# #     print('Need money!')



# def weather(temperature):
#     if temperature < 0:
#         return 'Cold!'
#     elif 0 <= temperature < 15:
#         return 'Not cold, not warm'
#     elif 15 < temperature < 25:
#         return 'Warm'
#     else:
#         return 'Hot'
# print(weather(-2))
# print(weather(0))
# print(weather(2))
# print(weather(17))
# print(weather(122))

phone1 = {'name': 'iPhone 13 Pro Max', 'price': 50000.0, 'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'price': 150000.0, 'discount': 80}
phone3 = {'name': '', 'price': 10000.0, 'discount': 10}

def discounted(price, discount, max_discount = 20, name = ''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Max skidka be doljna byt bolee 100')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        price_with_discount = price
    else:    
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

apple_desc = discounted(phone1['price'], phone1['discount'], name = phone1['name'])
print(apple_desc)

android_desc = discounted(phone2['price'], phone2['discount'], name = phone2['name'])
print(android_desc)

noname_desc_desc = discounted(phone3['price'], phone3['discount'], name = phone3['name'])
print(noname_desc_desc)

vozrast = int(input('Vvedite vash vozrast: '))
def func1(vozrast):
    if vozrast == 0:
        return 'Vi eshe ne rodilis'
    elif 0 < vozrast <= 6:
        return 'Vam nado v detsad'
    elif 7 <= vozrast <= 16:
        return 'Vam nado s shkolu'
    elif 17 <= vozrast <= 21:
        return 'Vam nado v VUZ'
    elif 22 <= vozrast <= 65:
        return 'Vam nado na rabotu'
    elif 66 <= vozrast:
        return 'Pora na pensiy'

vozrast_res = func1(vozrast)
print(vozrast_res)


def stroky(strk1, strk2):
    if not type(str(strk1)) and not type(str(strk2)):
        return 0
    else:
        print(stroky('a1', 'a2'))




