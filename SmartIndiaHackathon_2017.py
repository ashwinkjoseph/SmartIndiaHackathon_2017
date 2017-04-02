import socket
import json
from tkinter import *


ret = []
select = ['']
listm = []
selected = []

def addf(frame_left):
    i = -1
    for view in ret:
        i+=1;
        viewm = Label(frame_left, text=view['id'])
        listm.append([viewm, view]);
        def fun(vie):
            vie[0].config(bg="blue");
            for v in listm:
                if v!=vie:
                    v[0].config(bg="white")
            select[0]=vie;
            print("vie=="+str(vie))
        listm[i][0].bind("<Button-1>", lambda x, vie=listm[i] : fun(vie))
        listm[i][0].grid(row=i, column=0)

def addto(frame_right):
    selected.append(select[0]);
    i=0;
    for item in selected:
        viewm = Label(frame_right, text=item[1]);
        viewm.grid(row=i, column=0);
        i+=1;
    send = Button(root, text="SEND")
    send.grid(row=2, columnspan=2, column=1)
    send.bind("<Button-1>", sendit)

def sendit(event):
    smessage = {"intention":"add", "data":list()}
    
    for c in selected:
        smessage['data'].append(c[1]);

    smessage = json.dumps(smessage);
    p.send(smessage.encode());
    recieved = p.recv(3072);
    recieved = recieved.decode()
    print(recieved)
    if(recieved == "done"):
        message = {"intention":"delete", "data":list()}
        for c in selected:
            message['data'].append(c[1]);
        message = json.dumps(message);
        s.send(message.encode());
    else:
        print("Failed");

def click(event):
    typ = var.get() 
    message = Entry1.get()
    if(typ=="id"):
        smessage = {"intention":"search", "type":typ, "id":message}
    else:
        smessage = {"intention":"search", "type":typ, "name":message}
    smessage = json.dumps(smessage);
    if message!="quit":
        s.send(smessage.encode())
        while True:
            recieved = s.recv(3072);
            recieved = recieved.decode()
            if recieved == "1":
                s.close();
                break;
            if recieved == "error":
                print("Error");
                break;
            if recieved == "2":
                print("done")
                break;
            else:
                print(recieved)
                recieved = json.loads(recieved);
                ret.append({"id":recieved['emp_id'], "name":recieved['emp_name']});
                print("\n")
    else:
        s.send(message.encode())
        recieved = s.recv(3072);
        recieved = recieved.decode()
        if recieved == "1":
            s.close();
            root.quit();
    frame_left = Frame(root)
    frame_right = Frame(root)
    idd = Label(frame_left, text="ID")
    idd.grid(row=0, column=0)
    namee = Label(frame_left, text="Name")
    namee.grid(row=0, column=1)
    idd = Label(frame_right, text="ID")
    idd.grid(row=0, column=0)
    namee = Label(frame_right, text="Name")
    namee.grid(row=0, column=1)
    add = Button(root, text="ADD-->")
    frame_left.grid(row=1, column=0)
    add.grid(row=1, column=1)
    add.bind("<Button-1>", lambda event, x=frame_right: addto(x))
    frame_right.grid(row=1, column=2)
    addf(frame_left)

root = Tk();
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#s.connect(('192.168.43.239', 8000));
s.connect(('localhost', 8000));
p = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
p.connect(('localhost', 8010));
print("client is running");
spiders = Label(root, text="Spiders_2017_Hackathon_2017")
spiders.grid(row=0, columnspan=4)
var = StringVar(root)
var.set("Search By:")
fe = Frame(root)
fe.grid(row=0)
w=OptionMenu(fe, var, "Id", "Name");
tem = Label(fe, text="")
tem.pack()
w.pack()
Entry1 = Entry(fe)
Entry1.pack()
go = Button(fe, text="Search");
go.bind("<Button-1>", click)
go.pack()

root.mainloop()
#ch = []
#n = int(input("Enter the number of items to be transferred"));
#for i in range (n):
#    ch.append(int(input("Enter the item to be transferred")));
