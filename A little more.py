from tkinter import *

root = Tk();
select = []
selected = []
listm = []
def addf(event):
    view = ['entry1', 'entry2', 'entry3']
    i = -1
    for view_text in view:
        i+=1;
        viewm = Label(frame_left, text=view_text)
        listm.append([viewm, view_text]);
        def fun(vie):
            vie[0].config(bg="blue");
            for v in listm:
                if v!=vie:
                    v[0].config(bg="white")
            select.append(vie);
        listm[i][0].bind("<Button-1>", lambda x, vie=listm[i] : fun(vie))
        listm[i][0].grid(row=i, column=0)

def addto(event):
    selected.append(select[-1]);
    i=0;
    for item in selected:
        viewm = Label(frame_right, text=item[1]);
        viewm.grid(row=i, column=0);
        i+=1;

title = Label(root, text="Spiders_2017", height=2)
title.grid(row=0,columnspan=3)
search_title = Label(root, text="Search: ");
search_entry = Entry(root, text="Search");
search_press = Button(root, text="Go")
frame_left = Frame(root);
add = Button(root, text="Add");
frame_right = Frame(root);
search_title.grid(row=1, column=0);
search_entry.grid(row=1, column=1);
search_press.grid(row=1, column=2);
frame_left.grid(row=2, column=0);
add.grid(row=2, column=1)
frame_right.grid(row=2, column=2)
search_press.bind("<Button-1>", addf)
add.bind("<Button-1>", addto);
root.mainloop()