def fix_price(price):
    price = price.replace('COP', '')
    price = price.replace('$', '')
    price = price.replace('a', '')
    price = price.split("  ", maxsplit=1)[0]
    price = price.replace(' ', '')
    price2 = float(price)
    return price2


def sort_by_price_asc(sub_li):
    return sorted(sub_li, key=lambda x: x[1], reverse=True)


def sort_by_price_desc(sub_li):
    return sorted(sub_li, key=lambda x: x[1])


def sort_by_name_asc(sub_li):
    return sorted(sub_li, key=lambda x: x[0])


def build_items_list(self, items_name, items_price, items_number):
    items = []
    for x in range(items_number):
        price = fix_price(items_price[x].text)
        items.append([items_name[x + 1].text, price])
    return items


def print_results(list, msg):
    print("\n")
    print(msg)
    print("\n")
    for x in range(len(list)):
        print(str(list[x]) + "\n")
    print("........................................................................................\n")
