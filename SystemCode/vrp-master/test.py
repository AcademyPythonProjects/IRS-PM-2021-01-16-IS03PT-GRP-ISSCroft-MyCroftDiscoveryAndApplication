import requests 

# e.g. postal code sequence for vehicle 5 ...560529->560324->560153->761512->762432->791456->550201
# use any of these 6 digit postal code as input for below 'current_postalCode'
# or use wrong postal code: 5502019

input_data = {
    'vehicle_num': '5',
    'current_postalCode': 560324
}

response = requests.post('http://127.0.0.1:8000/get_address', params=input_data)
print(response.content)

# if the input is 560324, then the output should be as below
#b'"There are 5 more locations to go and the next one is 560153"'