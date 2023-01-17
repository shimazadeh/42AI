import sys

def delete_item(recipe_name, cookbook):
	del cookbook[recipe_name]

def print_content(recipe_name, cookbook):
	values = cookbook[recipe_name]
	for items in values:
		print(items, end=" ")
	print("\n")



def print_recepie_name(cookbook):
	keys = cookbook.keys()
	print("cookbook contains the following recepies: ")
	for i in keys:
		print(i, end=", ")
	print("\n")


def main(argv):
	cookbook = {'Sandwitch'	: ['lunch', ('ham', 'bread', 'cheese', 'tomatoes'), 10],
				'Cake'		: ['dessert', ('flour', 'suger', 'eggs'), 60],
				'Salad'		: ['lunch', ('avocado', 'arugula', 'tomatoes', 'spinach'), 15]}
	print_recepie_name(cookbook)
	print_content("Cake", cookbook)
	delete_item("Cake", cookbook)
	print_recepie_name(cookbook)

if __name__ == "__main__":
	main(sys.argv)
