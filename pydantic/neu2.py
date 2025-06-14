from enum import StrEnum
from pydantic import BaseModel
from datetime import date


class Test(StrEnum):
    BLOOM = "blood"
    XRA = "X-ray"
    CT = "CT"
    MRI = "MRI"
    PET = "PET"
    PETCT = "PET-CT"
    PETMRI = "PET-MRI"
    PETCTMRI = "PET-CT-MRI"
    PETCTXRA = "PET-CT-X-ray"
    PETMRIXRA = "PET-MRI-X-ray"
    PETCTMRIXRA = "PET-CT-MRI-X-ray"


class TestModel(BaseModel):
    name: str
    test: Test
    date: date
    result: str

    class Config:
        use_enum_values = True  # Вот сюда надо, если ты хочешь, чтобы enum хранился как строка


class LabTestRequest(BaseModel):
    patient_id: int
    tests: list[TestModel]


class Lab(LabTestRequest):
    lab_name: str
    technician: str


# Пример
example = Lab(
    patient_id=101,
    lab_name="Central Lab",
    technician="Dr. House",
    tests=[
        TestModel(name="CT scan", test=Test.CT, date=date.today(), result="OK"),
        TestModel(name="Full scan", test=Test.PETCTMRIXRA, date=date.today(), result="Waiting")
    ]
)

print(example.model_dump())
