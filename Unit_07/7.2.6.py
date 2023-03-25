MENU = """----- Main Menu -----
1. Print products.
2. Print number of products.
3. Check existence of some product.
4. Check amount of some product.
5. Delete product.
6. Add product.
7. Print ilegal products.
8. Remove duplicate products.
9. Exit."""

EXIT = 9


def get_product_list_from_user():
    """
    Get list of products from user.
    Example of the format: 'banana,apples,chocolate'
    :return: the list from user..
    :rtype: list of strings.
    """
    return input("Enter your products:\n").split(',') 


def get_user_choice():
    """
    Print the menu and ask to choose option.
    :return: the user chooden option. maybe invalid...
    :rtype: int
    """
    print(MENU)
    return int(input("Enter your choice: "))


def is_ilegal_product(product):
    """
    Check if product len less then 3,
    or maybe contain non letters chars.
    :param product: product name
    :type product: str
    :return: True if abouve, False if not.
    :rtype: bool
    """
    return len(product) < 3 or not product.isalpha()


def print_product(products):
    """
    Prints the products.
    :param products: list of products.
    :type products: list of strings.
    """
    print(', '.join(products))


def print_number_of_products(products):
    """
    Prints the number of products.
    :param products: list of products.
    :type products: list of strings.
    """
    print("Number of products in list is", len(products))


def check_existence_of_product(products):
    """
    Checks if some product are in the list.
    :param products: list of products.
    :type products: list of strings.
    """
    product = input("Enter a product name: ")
    print(product in products)


def check_amount_of_product(products):
    """
    Prints amount of some product in the list.
    :param products: list of products.
    :type products: list of strings.
    """
    product = input("Enter a product name: ")
    print(product, "appears", products.count(product), "times in the list")


def delete_product(products):
    """
    Deletes ONE appearance of some product.
    :param products: list of products.
    :type products: list of strings.
    """
    product = input("Enter a product name to delete: ")
    if product in products:
        products.remove(product)


def add_product(products):
    """
    add product to the list.
    :param products: list of products.
    :type products: list of strings.
    """
    products.append(input("Enter a product name to add: "))


def print_ilegal_products(products):
    """
    Prints ilegals product from the list.
    :param products: list of products.
    :type products: list of strings.
    """
    print_product(list(filter(is_ilegal_product, products)))


def remove_duplicate_products(products):
    """
    remove duplicates from the list.
    :param products: list of products.
    :type products: list of strings.
    """    
    products_without_duplicates = list(set(products))
    products.clear()
    products.extend(products_without_duplicates)


OPTIONS =\
{
    1 : print_product,
    2 : print_number_of_products,
    3 : check_existence_of_product,
    4 : check_amount_of_product,
    5 : delete_product,
    6 : add_product,
    7 : print_ilegal_products,
    8 : remove_duplicate_products
}


def main():
    products = get_product_list_from_user()
    
    user_choice = get_user_choice()
    while user_choice != EXIT:
        OPTIONS[user_choice](products)
        user_choice = get_user_choice()
    
    print("Bye bye!")



if __name__ == '__main__':
    main()
