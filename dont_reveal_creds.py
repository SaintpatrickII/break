from decouple import config
import yaml


user = config('myuser')
password_path = config('password')
print(user)
print(password_path)

with open(password_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            print(data)