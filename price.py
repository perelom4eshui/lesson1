price = 200
discount = 5

def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна превышать 100%')

    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price * (1-discount/100)
    return price_with_discount 

product = {'name': 'Samsung Galaxy S23', 'price': 80000, 'discount': 5}
product['with_discount'] = discounted(product['price'], product['discount'])

print(discounted(100, 5, max_discount=60))

print(discounted(100, 5, max_discount=60))

print(discounted(100, 5, max_discount=60))