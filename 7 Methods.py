class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):  # Fixed typo: 'calss_discount' to 'calc_discount'
        final_price = price - (discount * price / 100)
        print(f"final price is {final_price}")

# Creating an instance
l1 = Laptop("16 gb", "512gb")

# Calling the static method using the Class name (best practice)
Laptop.calc_discount(40_000, 10)

# Calling the class method
Laptop.get_storage_type()
