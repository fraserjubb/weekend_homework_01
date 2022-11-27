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


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


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
    

def remove_pet_by_name(pet_shop, name):
    pet_to_remove = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_remove)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, total_spent):
    customer["cash"] = get_customer_cash(customer) - total_spent
    return customer["cash"]


def get_customer_pet_count(pets):
    return len(pets["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

    # --- OPTIONAL ---

# def customer_can_afford_pet(customer, new_pet):
#     True = "can_buy_pet"
#     if customer["cash"] >= new_pet["price"]:
#         return "can_buy_pet"


#     # def test_customer_can_afford_pet__sufficient_funds(self):
#     #     customer = self.customers[0]
#     #     can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
#     #     self.assertEqual(True, can_buy_pet)