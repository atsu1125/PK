import tkinter
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(root,width=600,height=600)
cvs.pack()

for i in range(10):
    if i%2==0:
        cvs.create_oval(50+50*i,50,100+50*i,100,fill="orange")
    else:
        cvs.create_rectangle(50+50*i,50,100+50*i,100,fill="green")
for i in range(10):
    if i%3==0:
        cvs.create_oval(50+50*i,150,100+50*i,200,fill="orange")
    elif i%3==1:
        cvs.create_rectangle(50+50*i,150,100+50*i,200,fill="green")
  

root.mainloop()
