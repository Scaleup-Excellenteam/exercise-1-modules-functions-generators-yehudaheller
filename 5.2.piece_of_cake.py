def get_recipe_price(dictionary, **kwargs):
    price = 0
    optional_value = []

    for key, value in kwargs.items():
        if key == "optional":
            optional_value = value

    for key, value in kwargs.items():
        for dict_key in dictionary:
            if key == dict_key and key not in optional_value:
                price = price + dictionary[dict_key] * (value / 100)

    return price


# TESTING
#the_price = get_recipe_price({})
#the_price = get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
# the_price = get_recipe_price({'chocolate': 18, 'milk': 8, 'bamba': 20, 'salt': 8}, chocolate=200, milk=100, bamba= 300, salt=100, optional=['milk', 'chocolate'])
#print(the_price)
