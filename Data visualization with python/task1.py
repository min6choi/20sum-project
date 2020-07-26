import pandas as pd
import matplotlib.pyplot as plt


# creat the detaframes using the json file..
df = pd.read_json (r'./rain.json')
print(df)

print("df statistics: " ,df.describe())

df.plot(x='Month' , y = 'Tempearture')
df.plot(x='Month' , y = 'Rainfall')
plot.show()