
coocking_book = {}

with open("recipes.txt") as file:
	while True:
		dish = file.readline().rstrip()
		if not dish:
			break
		ingridients = []
		number_of_ingridients = int(file.readline().rstrip()) 
		while number_of_ingridients > 0:
			ingr_info = {}
			all_ingr_info = file.readline().rstrip().split(" | ")
			ingr_info["ingridient_name"] = all_ingr_info[0]
			ingr_info["quantity"] = all_ingr_info[1]
			ingr_info["neasure"] = all_ingr_info[2]
			ingridients.append(ingr_info)
			number_of_ingridients -= 1
		coocking_book[dish] = ingridients
		file.readline()
		



def print_coocling_book():
	print(coocking_book)



def get_shop_list_by_dishes(dishes, person_count):
	shop_list = {}
	for dish in dishes:
		dish_recipe = coocking_book[dish]
		for ingridient in dish_recipe:
			new_in_shop_list = ingridient.pop("ingridient_name")
			if new_in_shop_list in shop_list.keys():
				new_quantity = int(shop_list[new_in_shop_list]["quantity"]) + int(ingridient["quantity"]) * person_count
				shop_list[new_in_shop_list]["quantity"] = str(new_quantity)
			else:
				new_quantity = int(ingridient["quantity"]) * person_count
				ingridient["quantity"] = str(new_quantity)
				shop_list[new_in_shop_list] = ingridient
	print(shop_list)



get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print("\n \n")
print_coocling_book()






	


