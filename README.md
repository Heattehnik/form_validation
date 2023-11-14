# Тестовое задание для вакансии Junior+ Python разработчик.
## Web-приложение для определения заполненных форм.

### Описание

Приложение на основе FastAPI для проверки полей данных и 
сравнения их c шаблонами записаными в базу Tinydb. В случае, если в запросе есть все поля содержащиеся в шаблоне,
возвращается имя шаблона из базы данных. В противном случае возвращается список полей с типами данных этих полей.
Важно, что если в запросе кроме всех полей шаблона содержаться дополнительные поля форма считается правильной и 
возвращается имя шаблона.
Для отправки post запросов используется эндпоинт http://0.0.0.0:8000/get_form/


1. Какие техноллогии использовались при выполнении тестового задания:
    
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-FastAPI-informational?style=flat&logo=fastapi&logoColor=white&color=green)
![](https://img.shields.io/badge/Database-TinyDB-informational?style=flat&logo=tinydb&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)

2. Установка 

Клонируйте репозитория на свой компьютер:
```bash
   git clone https://github.com/Heattehnik/form_validation.git
```
Переходите в каталог:
``` bash
cd form_validation
```
3. Запуск в Docker:
Запуск осуществляется с помощью docker-compose
```bash
sudo docker-compose up
```

4. Запуск в терминале:

Перед запуском необходимо создать и активировать виртуальное окружение, а также установить необходимые зависимости из файла requirements.txt:

```bash
python3 -m venv venv
source myenv/bin/activate
pip install -r requirements.txt
```

Для запуска приложения введите команду:
```bash
python3 main.py
```

4. Использование:

После запуска документация приложения будет доступна по адресу:

http://0.0.0.0:8000/docs/

В каталоге database находится файл forms.json с заранее заполненными данными.

4. Тесты:

Для тестирования приложения используется тестовый клиент FastAPI. Тесты располагаются в файле test_main.py.

Чтобы запустить тесты необходимо ввести команду:

```bash
pytest test_main.py
```