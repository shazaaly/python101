class Product:
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc


class Category:
    def __init__(self, cat_name):
        self.cat_name = cat_name

    def display_cat(self):
        print(f"display category: {self.cat_name}")


class OnlineProduct(Product, Category):
    def __init__(self, name, price, desc, cat_name, shipping):
        Product.__init__(self, name, price, desc)
        Category.__init__(self, cat_name)
        self.shipping = shipping

    def displat_online_data(self):
        print(f"Online product name{self.name}")
        print(f"Online product cat_name{self.cat_name}")
        print(f"Online product shipping{self.shipping}")


online_product = OnlineProduct("Laptop", 1500, "High-performance laptop",
                               "Electronics", "Free shipping")

online_product.displat_online_data()
