# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]
   
    
def add_or_remove_cash(pet_shop, cash):
    #take the original cash total and adds cash
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop["admin"]["total_cash"]


def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, new_pets_sold):
    pet_shop["admin"]["pets_sold"] += new_pets_sold
    return new_pets_sold


# def get_stock_count(count):
#     count = ["pets"].index(1)
#     return count
    # for pet_number in pet_shop:
    #     if len(["pets"]) == count:
    #         return pet_number
    # stock_count += pet_number
    # return stock_count


def get_pets_by_breed(pet_shop, breed_given):
    named_breed = []
    for breed in pet_shop["pets"]:
        if breed["breed"] == breed_given:
            named_breed.append(breed)
    return named_breed


def find_pet_by_name(pet_shop, name):
    for name_of_pet in pet_shop["pets"]:
        if name_of_pet["name"] == name:
            return name_of_pet
    




