a = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


# Посчитать и вывести суммарное количество продаж для каждого товара
# Посчитать и вывести среднее количество продаж для каждого товара
# Посчитать и вывести суммарное количество продаж всех товаров
# Посчитать и вывести среднее количество продаж всех товаров


def main(price):
    items_sold_sum = 0
    for i in price:
        items_sold_sum += i
    return items_sold_sum
    # avg_items_sold = items_sold_sum / len(price)
    # print(avg_items_sold)


for phone_price in a:
    phone_price_sum = main(phone_price['items_sold'])
    print(f"Суммарное кол-во продаж для {phone_price['product']}: {phone_price_sum}")
    avg_items_sold = round(phone_price_sum / len(phone_price['items_sold']), 2)
    print(f"среднее количество продаж для {phone_price['product']}: {avg_items_sold}")

all_sum = 0

for phone_price in a:
    all_sum += main(phone_price['items_sold'])

all_price_avg = all_sum / len(a)

print(f"суммарное количество продаж всех товаров {all_sum}")
print(f"Среднее количество продаж всех товаров {all_price_avg}")


