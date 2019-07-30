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


def sort_by_name_desc(sub_li):
    return sorted(sub_li, key=lambda x: x[0])
