from dis import dis

def func(path, no):
    if no == 5:
        return
    else:
        path.append(no)
        no += 1
        func(path, no)

no = 3
path = [2]
func(path, no)
print(path)
    
