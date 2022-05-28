with open('GuardianKid.csv','r') as f1:
    dataList = f1.readlines()
    kid = []
    guardian = []
    for line in dataList:
        entry = line.split(',')
        guardian.append(entry[0])
        kid.append(entry[1])

length = len(guardian)
data = []
for index in range(length):
    info = kid[index]+' picked By '+guardian[index]
    data.append(info)
print(data)