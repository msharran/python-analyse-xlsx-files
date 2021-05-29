import inventory


def main():
    products = inventory.read_products_from(file_name="inventory.xlsx", sheet_name="Sheet1")
    product_count_by_supplier = inventory.group_products_by_supplier(products)
    print(product_count_by_supplier)


if __name__ == '__main__':
    main()
