import json

data2 = {
    
    'name': 'Stephen Gary Wozniak', 
    'age': 74,
    'city': 'Los Gatos, California',
    'interests': ['engineering','technology','education ','creativity'],
    'is_student': False
}

#
with open('data2.json','w') as json_file:
#
    json.dump(data2,json_file,indent=4)
#
print("Data has been written to data2.json")
    


#
with open('data2.json','r') as json_file:
    
    #
    loaded_data = json.load(json_file)

#    
print("Succesfully able to read data2.json")
print(loaded_data)


loaded_data['age'] = 34 
loaded_data['interests'].append('History')

#loaded_data['interests'].remove('Put Your String Here')

#Rewrite the changes to the json file. 
with open('data2.json','w') as json_file:
    
    json.dump(loaded_data,json_file,indent=4)
    
print("Data has been re-written to data2.json")