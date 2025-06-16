# # from flask import Flask, request, jsonify
# # from flask_sqlalchemy import SQLAlchemy
# # from pydantic import BaseModel, Field, ValidationError
# #
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
# #
# # # Модель SQLAlchemy
# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)
# #
# # # Модель Pydantic для валидации
# # class UserCreate(BaseModel):
# #     username: str = Field(..., min_length=3, max_length=20)
# #     email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
# #
# # class UserResponse(BaseModel):
# #     id: int
# #     username: str
# #     email: str
# #
# #     class Config:
# #         from_attributes = True  # Для Pydantic v2 (замена orm_mode)
# #
# # # Создание таблиц
# # with app.app_context():
# #     db.create_all()
# #
# # # Базовый маршрут для проверки
# # @app.route('/')
# # def home():
# #     return 'Welcome to the Flask API!'
# #
# # # Маршрут для создания пользователя
# # @app.route('/users', methods=['POST'])
# # def create_user():
# #     try:
# #         user_data = UserCreate(**request.get_json())
# #         user = User(username=user_data.username, email=user_data.email)
# #         db.session.add(user)
# #         db.session.commit()
# #         return jsonify(UserResponse.from_orm(user).dict()), 201
# #     except ValidationError as e:
# #         return jsonify({"error": e.errors()}), 400
# #     except Exception as e:
# #         db.session.rollback()
# #         return jsonify({"error": str(e)}), 500
# #
# # # Маршрут для получения пользователя
# # @app.route('/users/<int:id>', methods=['GET'])
# # def get_user(id):
# #     user = User.query.get_or_404(id)
# #     return jsonify(UserResponse.from_orm(user).dict())
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
# # 🟦 ЗАДАЧА 1: Patient с alias и default_factory
# # Создать базовую модель пациента с алиасами для
# # first_name и last_name(CamelCase), и автоматическим временем регистрации.
# #
# # Требования:
# # Поля: first_name, last_name (алиасы: firstName, lastName)
# # Поле registration_time: генерируется автоматически через default_factory
# #
# # Включить populate_by_name = True
# # Добавить описание в json_schema_extra
#
# from pydantic import BaseModel, Field, ConfigDict
# from datetime import datetime
#
# class Patient(BaseModel):
#     first_name: str = Field(alias="firstName", description="Имя пациента")
#     last_name: str = Field(alias="lastName", description="Фамилия пациента")
#     registration_time: datetime = Field(default_factory=datetime.utcnow, description="Время регистрации пациента")
#
#
#
#
#
#     model_config = ConfigDict(
#         populate_by_name=True,
#         json_schema_extra={
#             "example": {
#                 "firstName": "Ivan",
#                 "lastName": "Petrov"
#             }
#         }
#     )
# patient = Patient(firstName="Ivan", lastName="Petrov")
# #print(patient)
# print(patient.model_dump(by_alias=True))
#
# from pydantic import BaseModel, Field, ConfigDict
# from datetime import datetime
#
# class Patient(BaseModel):
#     first_name: str = Field(alias="firstName", description="Имя пациента")
#     last_name: str = Field(alias="lastName", description="Фамилия пациента")
#     registration_time: datetime = Field(default_factory=datetime.utcnow, description="Время регистрации пациента")
#
#     model_config = ConfigDict(
#         populate_by_name=True,
#         json_schema_extra={
#             "example": {
#                 "firstName": "Ivan",
#                 "lastName": "Petrov"
#             }
#         }
#     )
#
# # Создание нескольких пациентов
# patients = [
#     Patient(firstName="Ivan", lastName="Petrov"),
#     Patient(firstName="Anna", lastName="Ivanova"),
#     Patient(firstName="Sergey", lastName="Smirnov")
# ]
#
# # Вывод информации о каждом пациенте
# for i, patient in enumerate(patients, 1):
#     print(f"Пациент {i}:")
#     print(f"  Имя: {patient.first_name}")
#     print(f"  Фамилия: {patient.last_name}")
#     print(f"  Время регистрации: {patient.registration_time.strftime('%Y-%m-%d %H:%M:%S')}")
#     print("  JSON:", patient.model_dump(by_alias=True))
#     print("-" * 40)
#
# """"""
# from pydantic import BaseModel, Field, ConfigDict
# from datetime import datetime
# from uuid import uuid4, UUID
# import json
#
# class Patient(BaseModel):
#     id: UUID = Field(default_factory=uuid4, description="Уникальный ID пациента")
#     first_name: str = Field(alias="firstName", description="Имя пациента")
#     last_name: str = Field(alias="lastName", description="Фамилия пациента")
#     registration_time: datetime = Field(default_factory=datetime.utcnow, description="Время регистрации пациента")
#
#     model_config = ConfigDict(
#         populate_by_name=True,
#         json_schema_extra={
#             "example": {
#                 "firstName": "Ivan",
#                 "lastName": "Petrov"
#             }
#         }
#     )
#
# # Список пациентов
# patients = [
#     Patient(firstName="Ivan", lastName="Petrov"),
#     Patient(firstName="Anna", lastName="Ivanova"),
#     Patient(firstName="Sergey", lastName="Smirnov")
# ]
#
# # Сохранение в файл JSON
# with open("patients.json", "w", encoding="utf-8") as f:
#     json.dump([p.model_dump(by_alias=True) for p in patients], f, ensure_ascii=False, indent=4, default=str)
#
# # Вывод на экран
# for i, patient in enumerate(patients, 1):
#     print(f"Пациент {i}:")
#     print(f"  ID: {patient.id}")
#     print(f"  Имя: {patient.first_name}")
#     print(f"  Фамилия: {patient.last_name}")
#     print(f"  Время регистрации: {patient.registration_time.strftime('%Y-%m-%d %H:%M:%S')}")
#     print("-" * 40)




from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import Optional
import json
import re

# Модель для адреса
class Address(BaseModel):
    city: str
    street: str
    house_number: int

    @field_validator('city')
    @classmethod
    def city_must_be_valid(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError('City must be at least 2 characters long')
        return v

    @field_validator('street')
    @classmethod
    def street_must_be_valid(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError('Street must be at least 3 characters long')
        return v

    @field_validator('house_number')
    @classmethod
    def house_number_must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError('House number must be positive')
        return v

# Модель для пользователя
class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator('name')
    @classmethod
    def name_must_be_letters(cls, v: str) -> str:
        if not re.match(r'^[A-Za-z\s]+$', v):
            raise ValueError('Name must contain only letters and spaces')
        if len(v.strip()) < 2:
            raise ValueError('Name must be at least 2 characters long')
        return v

    @field_validator('age')
    @classmethod
    def age_must_be_valid(cls, v: int) -> int:
        if not 0 <= v <= 120:
            raise ValueError('Age must be between 0 and 120')
        return v

    @field_validator('is_employed')
    @classmethod
    def employment_age_validation(cls, v: bool, values: dict) -> bool:
        if v and 'age' in values.data:  # Если is_employed=True
            if not 18 <= values.data['age'] <= 65:
                raise ValueError('Employed users must be between 18 and 65 years old')
        return v

# Функция для обработки JSON
def process_user_registration(json_input: str) -> dict:
    try:
        # Десериализация JSON в объект Pydantic
        user = User.model_validate_json(json_input)
        # Сериализация объекта обратно в JSON
        return {
            "status": "success",
            "user": user.model_dump(),
            "json_output": user.model_dump_json(indent=2)
        }
    except ValidationError as e:
        # Преобразуем ошибки валидации в JSON-сериализуемый формат
        errors = [
            {
                "loc": err["loc"],
                "msg": err["msg"],
                "type": err["type"],
                "input": err.get("input", None)
            }
            for err in e.errors()
        ]
        return {
            "status": "error",
            "errors": errors
        }
    except json.JSONDecodeError as e:
        return {
            "status": "error",
            "errors": [{"msg": f"Invalid JSON format: {str(e)}"}]
        }

# Примеры JSON для тестирования
test_cases = [
    # Успешный случай
    """{
        "name": "John Smith",
        "age": 30,
        "email": "john.smith@example.com",
        "is_employed": true,
        "address": {
            "city": "London",
            "street": "Baker Street",
            "house_number": 221
        }
    }""",

    # Успешный случай (не работает, возраст < 18)
    """{
        "name": "Alice Brown",
        "age": 16,
        "email": "alice.brown@example.com",
        "is_employed": false,
        "address": {
            "city": "Paris",
            "street": "Champs Elysees",
            "house_number": 10
        }
    }""",

    # Ошибка: возраст не соответствует статусу занятости
    """{
        "name": "John Doe",
        "age": 70,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }""",

    # Ошибка: некорректное имя (содержит цифры)
    """{
        "name": "John123",
        "age": 25,
        "email": "john123@example.com",
        "is_employed": true,
        "address": {
            "city": "Berlin",
            "street": "Unter den Linden",
            "house_number": 1
        }
    }""",

    # Ошибка: некорректный email
    """{
        "name": "Emma Watson",
        "age": 25,
        "email": "invalid-email",
        "is_employed": true,
        "address": {
            "city": "Rome",
            "street": "Via Roma",
            "house_number": 5
        }
    }""",

    # Ошибка: город слишком короткий
    """{
        "name": "Robert Johnson",
        "age": 40,
        "email": "robert.j@example.com",
        "is_employed": true,
        "address": {
            "city": "A",
            "street": "Main Street",
            "house_number": 15
        }
    }""",

    # Ошибка: некорректный JSON
    """{
        "name": "Invalid JSON",
        "age": 30,
        "email": "invalid.json@example.com",
        "is_employed": true,
        "address": {
            "city": "Tokyo",
            "street": "Shibuya",
            "house_number": 100
        }
    """
]

# Тестирование всех случаев
for i, json_input in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:")
    result = process_user_registration(json_input)
    print(json.dumps(result, indent=2, ensure_ascii=False))