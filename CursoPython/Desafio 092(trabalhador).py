from datetime import datetime
data = {}
now = datetime.now().year
print('-='*20)
print("		CTPS	")
print('-='*20)

data['Name'] = str(input('Name: '))
year = int(input('Year of birth: '))
age = now - year
data['Age'] = age
data['CTPS'] = int(input('CTPS[if dont have, type "0"]: '))
    
if data['CTPS'] > 0:
    data['Hiring year'] = int(input('What was the hiring year: '))
    data['Salary'] = float(input('Salary: R$ '))
    retirement = (data['Hiring year'] + 35) - year
    data['Retirement'] = retirement
elif data['CTPS'] == 0:
    data['Message'] = 'Get a job, man!'

print('-='*10)
print('	DATA')
print('-='*10)

for k, v in data.items():
    print(f'{k} = {v}')
        

        
        
    