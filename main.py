from tkinter import *

root = Tk()

root.title('Smart Calculator')
root.geometry('450x400')
root.config(padx=20, pady=20)
root.config(bg='lightblue')

hi = Label(root, text='Hi, My name is Jarvis!!', font=('Helvetica',15,'bold')).pack()
ser = Label(root, text='How can I help you!', font=('Times',12,'bold')).pack(pady=20)

cal = Label(root, text='I can do math calculations, type what you want below', font=('Helvetica',15,'bold')).pack(pady=30)

var= StringVar()
inp = Entry(root, textvariable=var)
inp.pack()


def click():
    ask = var.get()
    print(ask)
    q = ask.split(' ')
    if 'add' in q or 'addition' in q or 'plus' in q or 'sum' in q:
        nums = [x for x in q if x.isnumeric()]
        print(nums)
        res = float(nums[0]) + float(nums[1])
        out.config(text=f'results is: {res}')
    elif 'subtract' in q or 'sub' in q or 'minus' in q or 'difference' in q:
        print('hey')
        nums = [x for x in q if x.isnumeric()]
        print(nums)
        res = float(nums[0]) - float(nums[1])
        out.config(text=f'results is: {res}')
    elif 'multiply' in q or 'multiplication' in q or 'product' in q or 'mul' in q:
        nums = [x for x in q if x.isnumeric()]
        print(nums)
        res = float(nums[0]) * float(nums[1])
        out.config(text=f'results is: {res}')
    elif 'divide' in q or 'div' in q or 'division':
        nums = [x for x in q if x.isnumeric()]
        print(nums)
        res = float(nums[0]) / float(nums[1])
        out.config(text=f'results is: {res}')
    elif 'power' in q:
        nums = [x for x in q if x.isnumeric()]
        print(nums)
        res = float(nums[0])**2
        out.config(text=f'results is: {res}')

run = Button(root, text='Do it',  padx=20, pady=10, relief=RAISED, command=click)
run.pack(pady=20)

out = Label(root, text='  ', font=('Helvetica',15,'bold'))

out.pack()

root.mainloop()