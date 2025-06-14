# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from pydantic import BaseModel, Field, ValidationError
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# # Модель SQLAlchemy
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
# # Модель Pydantic для валидации
# class UserCreate(BaseModel):
#     username: str = Field(..., min_length=3, max_length=20)
#     email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
#
# class UserResponse(BaseModel):
#     id: int
#     username: str
#     email: str
#
#     class Config:
#         from_attributes = True  # Для Pydantic v2 (замена orm_mode)
#
# # Создание таблиц
# with app.app_context():
#     db.create_all()
#
# # Базовый маршрут для проверки
# @app.route('/')
# def home():
#     return 'Welcome to the Flask API!'
#
# # Маршрут для создания пользователя
# @app.route('/users', methods=['POST'])
# def create_user():
#     try:
#         user_data = UserCreate(**request.get_json())
#         user = User(username=user_data.username, email=user_data.email)
#         db.session.add(user)
#         db.session.commit()
#         return jsonify(UserResponse.from_orm(user).dict()), 201
#     except ValidationError as e:
#         return jsonify({"error": e.errors()}), 400
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({"error": str(e)}), 500
#
# # Маршрут для получения пользователя
# @app.route('/users/<int:id>', methods=['GET'])
# def get_user(id):
#     user = User.query.get_or_404(id)
#     return jsonify(UserResponse.from_orm(user).dict())
#
# if __name__ == '__main__':
#     app.run(debug=True)
# 🟦 ЗАДАЧА 1: Patient с alias и default_factory
# Создать базовую модель пациента с алиасами для
# first_name и last_name(CamelCase), и автоматическим временем регистрации.
#
# Требования:
# Поля: first_name, last_name (алиасы: firstName, lastName)
# Поле registration_time: генерируется автоматически через default_factory
#
# Включить populate_by_name = True
# Добавить описание в json_schema_extra

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class Patient(BaseModel):
    first_name: str = Field(alias="firstName", description="Имя пациента")
    last_name: str = Field(alias="lastName", description="Фамилия пациента")
    registration_time: datetime = Field(default_factory=datetime.utcnow, description="Время регистрации пациента")





    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "firstName": "Ivan",
                "lastName": "Petrov"
            }
        }
    )
patient = Patient(firstName="Ivan", lastName="Petrov")
#print(patient)
print(patient.model_dump(by_alias=True))

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class Patient(BaseModel):
    first_name: str = Field(alias="firstName", description="Имя пациента")
    last_name: str = Field(alias="lastName", description="Фамилия пациента")
    registration_time: datetime = Field(default_factory=datetime.utcnow, description="Время регистрации пациента")

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "firstName": "Ivan",
                "lastName": "Petrov"
            }
        }
    )

# Создание нескольких пациентов
patients = [
    Patient(firstName="Ivan", lastName="Petrov"),
    Patient(firstName="Anna", lastName="Ivanova"),
    Patient(firstName="Sergey", lastName="Smirnov")
]

# Вывод информации о каждом пациенте
for i, patient in enumerate(patients, 1):
    print(f"Пациент {i}:")
    print(f"  Имя: {patient.first_name}")
    print(f"  Фамилия: {patient.last_name}")
    print(f"  Время регистрации: {patient.registration_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("  JSON:", patient.model_dump(by_alias=True))
    print("-" * 40)

""""""
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from uuid import uuid4, UUID
import json

class Patient(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Уникальный ID пациента")
    first_name: str = Field(alias="firstName", description="Имя пациента")
    last_name: str = Field(alias="lastName", description="Фамилия пациента")
    registration_time: datetime = Field(default_factory=datetime.utcnow, description="Время регистрации пациента")

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "firstName": "Ivan",
                "lastName": "Petrov"
            }
        }
    )

# Список пациентов
patients = [
    Patient(firstName="Ivan", lastName="Petrov"),
    Patient(firstName="Anna", lastName="Ivanova"),
    Patient(firstName="Sergey", lastName="Smirnov")
]

# Сохранение в файл JSON
with open("patients.json", "w", encoding="utf-8") as f:
    json.dump([p.model_dump(by_alias=True) for p in patients], f, ensure_ascii=False, indent=4, default=str)

# Вывод на экран
for i, patient in enumerate(patients, 1):
    print(f"Пациент {i}:")
    print(f"  ID: {patient.id}")
    print(f"  Имя: {patient.first_name}")
    print(f"  Фамилия: {patient.last_name}")
    print(f"  Время регистрации: {patient.registration_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
