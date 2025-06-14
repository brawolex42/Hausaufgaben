from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str
    state: str


class User(BaseModel):
    id: int = 0
    name: str = ""
    email: str = ""
    password: str = ""
    is_active: bool = True


class UserIn(BaseModel):
    name: str = ""
    email: str = ""
    password: str = ""
    is_active: bool = True


# Примеры объектов:
address = Address(city="Bogota", country="Colombia", state="Antioquia")

user = User(id=1, name="Juan", email="juan@juan.com", password="123456", is_active=True)

print(address)
print(user)
print(user.id)
print(user.name)
print(user.email)
print(user.password)
print(user.is_active)

# дополнительные поля

class Address(BaseModel):
    city: str
    street: str
    house_numb: int
    index: int


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True
    address: Address


address = Address(city="Minsk", street="Street", house_numb=13, index=6000)

user = User(id=2, name="Tomas", age=27, address=address)

print(user)

print(user.address.street)
class Address(BaseModel):
    city: str
    street: str
    house_numb: int
    index: int


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True
    address: Address


address = Address(city="Minsk", street="Street", house_numb=13, index=6000)
user = User(id=2, name="Tomas", age=27, address=address)

print(user)

print(user.address.street)


# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,



from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional


# Класс адреса
class Address(BaseModel):
    city: str
    street: str
    house_number: int


# Класс пользователя
class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    address: Address


# Пример JSON-данных (может быть получен через API, из файла и т.д.)
example_data = {
    "name": "Александр",
    "age": 25,
    "email": "alex@example.com",
    "address": {
        "city": "Москва",
        "street": "Тверская",
        "house_number": 12
    }
}


# Проверка и валидация
try:
    user = User(**example_data)
    print(" Данные прошли валидацию:")
    print(user)
except ValidationError as e:
    print(" Ошибка валидации:")
    print(e)
