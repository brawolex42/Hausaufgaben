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



try:
    user = User(**example_data)
    print(" Данные прошли валидацию:")
    print(user)
except ValidationError as e:
    print(" Ошибка валидации:")
    print(e)

from pydantic import BaseModel, EmailStr



class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True

    def get_permissions(self):
        return ["read"]



class Admin(User):
    admin_level: int = 1

    def get_permissions(self):
        # Добавляем дополнительные права
        return super().get_permissions() + ["create", "update", "delete"]


# Проверка работы
basic_user = User(name="Иван", email="ivan@example.com")
admin_user = Admin(name="Анна", email="admin@example.com", admin_level=5)

print("Пользователь:", basic_user.name)
print("Права:", basic_user.get_permissions())

print("Админ:", admin_user.name)
print("Права:", admin_user.get_permissions())
print("Уровень админа:", admin_user.admin_level)
