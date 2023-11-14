from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_case_1():
    data = {"user_name_1": "Ivan", "order_date_1": "01.01.1999"}
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "MyForm1"}


def test_case_2():
    data = {
        "employee_phone_2": "+79000000000",
        "user_email_2": "some@email.com",
        "order_description_2": "hello",
        "delivery_date_2": "22.01.2023",
    }
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "Order_Form2"}


def test_case_3():
    data = {
        "first_name_3": "Ivan",
        "last_name_3": "Ivanov",
        "phone_3": "+79999999999",
        "email_3": "ivan@mail.ru",
        "birthday_3": "1987-05-07",
    }

    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "employer_form3"}


def test_case_4():
    data = {
        "first_name_4": "Anna",
        "last_name_4": "Petrova",
        "phone_4": "+78880005544",
        "email_4": "petra@gmail.com",
    }
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "customer_form4"}


def test_case_5():
    data = {"user_name_5": "Milflover", "order_date_5": "2020-05-10"}
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "MyForm5"}


def test_case_6():
    data = {
        "employee_phone_6": "+78955556432",
        "user_email_6": "best@proton.net",
        "order_description_6": "Some description",
        "delivery_date_6": "10.08.2023",
    }
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "Order_Form6"}


def test_case_7():
    data = {
        "first_name_7": "Alla",
        "last_name_7": "Pugacheva",
        "phone_7": "+71234567890",
        "email_7": "primadona@russia.ru",
        "birthday_7": "15.04.1949",
    }
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "employer_form7"}


def test_case_8():
    data = {}
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {}


def test_case_9():
    data = {
        "first_name_4": "Anna",
        "last_name_4": "Petrova",
        "phone_4": "+78880005544",
        "email_4": "petra@gmail.com",
        "additional_field_1": "additional text",
        "another_phone": "+71112223344",
        "another_email": "pork@mail.ru",
    }
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {"template_name": "customer_form4"}


def test_case_10():
    data = {
        "some_phone": "+79506542522",
        "some_text": "what a wonderful world",
        "some_email": "vova@russia.ru",
        "some_date": "12.02.2020",
    }
    response = client.post("/get_form", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "some_date": "date",
        "some_email": "email",
        "some_phone": "phone",
        "some_text": "text",
    }
