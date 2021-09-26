import pickle

def num1():
    with open('mylife.txt', mode='a+') as fik:
        count = -1
        while count != 0:
            app = input('input something, please: ')
            if app == 'end':
                count += 1
            else:
                app1 = app + '\n'
                fik.write(app1)

#num1()

def num2():
    with open('picklew.txt', mode='wb') as defin:
        pickle.dump({'Fio': 'Valyaev G.A.', 'sum_balls': '273', 'grades': '5+'}, defin)
    with open('picklew.txt', mode='rb') as ws:
        print(pickle.load(ws))

#num2()
