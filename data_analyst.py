import matplotlib.pyplot as plt

with open('temperature_record.txt','r', encoding='utf-8') as f:
    global t_list
    t_list = f.readlines()
# 일단 온도만 가져옵니다. 
temperature = []  
for i in t_list:       
    temperature.append(i[-3:-1])

print(temperature)
plt.plot(temperature,'ro')
plt.show()