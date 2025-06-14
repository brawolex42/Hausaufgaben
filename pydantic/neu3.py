# from pydantic import BaseModel, Field
# from decimal import Decimal
#
#
# class Product(BaseModel):
#     name: str
#     description: str = Field(default=None, description="Описание товара")
#     price: Decimal = Field(gt=0, max_digits=6, decimal_places=2) # 8888.88
#     in_stock: bool = Field(default=True, alias="available") # ... -> elipsys
#
#
# product = Product(
#     name="Chair",
#     price=Decimal("9.23"),
#     available=False
# )
#
# print(product)
# print(product.price)
#
# from pydantic import BaseModel, Field
# from decimal import Decimal
# import typing
#
# class Product(BaseModel):
#     name: str
#     description: str = Field(default=None, description="Описание товара")
#     price: Decimal = Field(gt=0, max_digits=6, decimal_places=2) # 8
#     in_stock: bool = Field(default=True, alias="available") # ... -> elipsys
#
# product = Product(
#     name="Chair",
#     price=Decimal("9.23"),
#     available=False
# )
#
#
#
#
# class Product2(BaseModel):
#     name: str
#     description: str = Field(default=None, description="Описание товара")
#     price: Decimal = Field(gt=0, max_digits=6, decimal_places=2) # 8
#
# product = Product2(
#     name="Chair",
#     price=Decimal("9.23"),
#     available=False
# )
#
#
#
#
# print(product)
# print(product.price)
#
# from pydantic import BaseModel, EmailStr, HttpUrl, Field
# from decimal import Decimal
# import typing
#
#
# class Product(BaseModel):
#     name: str
#     price: Decimal
#     tags: list[str]
#
#
# class User(BaseModel):
#     full_name: str
#     age: int
#     email: EmailStr
#     homepage: HttpUrl # https://
#     # products: list[Product] = []  # WRONG!!!!
#     products: list[Product] = Field(default_factory=list)
#
#
# user = User(
#     full_name="J. Johanson",
#     age=32,
#     email="j.johanson@google.com",
#     homepage="https://example.com"
# )
#
# print(user)
#
#
# from pydantic import BaseModel, Field
# from decimal import Decimal
#
#
# class Product(BaseModel):
#     name: str
#     description: str = Field(default=None, description="Описание товара")
#     price: Decimal = Field(gt=0, max_digits=6, decimal_places=2) # 8888.88
#     in_stock: bool = Field(default=True, alias="available") # ... -> elipsys
#
#
# product = Product(
#     name="Chair",
#     price=Decimal("9.23"),
#     available=False
# )
#
# print(product)
# print(product.price)


