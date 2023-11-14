import requests
template_data = 'user_name_1=gadjka@mail.ru&order_date_1=22.01.2023'
params = {'template_data': template_data}
response = requests.post('http://0.0.0.0:8000/get_form', params=params)
print(response.text)
