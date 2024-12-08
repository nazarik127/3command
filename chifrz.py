text = input().strip().replace(' ', '_')


def chifrz(arr, count = 2):
    string = ''
    for i in range(count//2):
        arr_temp = arr[:2]
        arr = arr[2:]
        for i in range(6):
            for j in range(2):
                string += arr_temp[j][i]
    return string

def fill_arr(text):
    count = 0
    arr = []
    a = True
    mass = ['_','_','_','_','_','_']
    while a:
        count += 1
        temp = []
        for i in range(6):
            temp.append(text[0])
            text = text[1:]
            if text == '':
                if count % 2 != 0:
                    if i < 5:
                        for j in range(1):
                            for g in range(5-i):
                                temp.append('_')
                            arr.append(temp)
                            arr.append(mass)
                            return arr, count+1
                elif i < 5:
                    for g in range(5-i):
                        temp.append('_')
                arr.append(temp)
                return arr, count
        arr.append(temp)
    return arr, count

arr, count = fill_arr(text)

for i in range(len(arr)):
    print(arr[i])

print(chifrz(arr, count))