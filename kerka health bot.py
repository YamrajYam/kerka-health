#importing libraries and functions 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pandas as pd
#root geometry
root = Tk()
root.title("KERKA Health")
root.geometry("1360x700")
root.configure(bg="#0E0220")
root.state("normal")
font="consolas 16 "
font1="impact 22 "
font2="calibri 12 bold"

 #diffrent frames for diest plans and details

aframe = Frame(root, width=655, height=700, background="#3e497a")
aframe.pack()
aframe.place(x=0,y=5)

rframe = Frame(root, width=685, height=700, background="#82a6cb")
rframe.pack()
rframe.place(x=670,y=5)

r2frame = Frame(root, width=665, height=220,background="#93B1A6")
r2frame.pack()
r2frame.place(x=680,y=10)

r3frame = Frame(root, width=665, height=460, background="#c5ecbe")
r3frame.pack()
r3frame.place(x=680,y=240)




#PROJECT NAME

project=Label(root,text="KERKA HEALTH",height="1",width="15",font=font1,background="#bcfcc9")
project.pack()
project.place(x=200,y=0)


#list items for diffrent diet plans
#diebetes type 2
db2=["Veggie omelet (1 whole egg plus 2 egg whites)",
     "Fruit smoothie made with low-fat milk",
     "Low-fat plain yogurt","Chia seeds",
     "Oatmeal made with low-fat milk",
     "Fruit and nuts"]

dl2=["Turkey sandwich with sliced veggies",
     "Turkey chili",
     "Salad (dark lettuce or leafy greens)",
     "Chicken breast",
     "Chickpeas with olive oil"]

dd2=["Grilled Salmon",
     "Steamed Broccoli",
     "Quinoa",
     "Tofu",
     "Veggie stir-fry over brown rice",
     "Tray bake made with shrimp",
     "Roasted vegetables"]



#diebetes type 1 diet
db1=["Veggie omelet (1 whole egg plus 2 egg whites)",
     "Fruit smoothie made with low-fat milk",
     "Low-fat plain yogurt","Chia seeds",
     "Oatmeal made with low-fat milk","Apples","Flax","Berries","Pears",
     "Fruit and nuts"]

dl1=["Turkey sandwich with sliced veggies",
     "Turkey chili",
     "Salad (dark lettuce or leafy greens)",
     "Chicken breast","Peas","Beans",
     "Chickpeas with olive oil"]

dd1=["Grilled Salmon",
     "Steamed Broccoli",
     "Quinoa",
     "Tofu","Yogurt","Chicken","Peas",
     "Veggie stir-fry over brown rice",
     "Tray bake made with shrimp",
     "Roasted vegetables"]




#anemia
ab=["Oatmeal",
    "Raspberries",
    "Hemp seeds",
    "cacao nibs",
    "Orange juice",
    "Chicken sausage",
    "Mushrooms",
    "Sweet potatoes",
    "Spinach"]


al=["Beef chili",
    "Tuna burger",
    "Spinach salad",
    "Bagel",
    "Cream cheese",
    "Spinach"]

ad=["Lamb chops",
    "Boiled potatoes"
    "Steamed broccoli"
    "Curly kale",
    "Kidney beans",
    "Chickpeas",
    "black-eyed peas",
    "Tinned tomatoes",
    "Yogurt"]

#thyroid diet plan
tb=["Scrambled eggs with salmon",
    "Fruit salad with yogurt",
    "Sliced almonds",
    "Omelet with mushrooms",
    "Zucchini",
    "Protein smoothie with berries",
    "Poached or boiled eggs",
    "Nut butter",
    "Avocados",
    "Berries",
    "Coconut yogurt",
    "Almond butter",
    "A frittata with vegetables"]
tl=["A quinoa bowl with vegetables",
    "Chickpeas",
    "A turkey burger",
    "Green salad",
    "Sweet potato fries",
    "Tuna salad lettuce cups",
    "Gluten-free crackers"
    "Cauliflower",
    "black beans",
    "Salsa",
    "Guacamole",
    "Veggies",
    "A grilled chicken salad",
    "A salad with grilled shrimp"]

td=["A black bean",
    "Grilled shrimp skewers",
    "Pineapple",
    "Pan-fried crab cakes",
    "Brown rice",
    "A grilled steak",
    "Baked sweet potato",
    "Roasted chicken",
    "Quinoa",
    "Broccoli",
    "Shrimp fajitas",
    "Corn tortillas",
    "Baked salmon"]

#heart disease

hdb = [
    "Whole-grain cereal with skim milk",
    "Fresh berries",
    "Almonds",
    "Soft cooked egg on whole wheat toast",
    "Whole-grain English muffin with melted cheese ",
    "Greek yogurt with whole-grain cereal",
    "Fruit, whole-grain crackers",
    "Homemade cereal bar, plain yogurt cup"
]


hdl = [
    "Grilled chicken salad with olive oil dressing",
    "Steamed broccoli",
    "Quinoa",
    "Leafy green vegetables like spinach",
    "Whole grains such as barley, rye or oats",
    "Fatty fish like salmon, mackerel, sardines, and tuna",
    "Beans"
]

hdd = ["Baked salmon","Brown rice","Asparagus","Low-sodium canned vegetables","Vegetables with creamy sauces","Frozen fruit with sugar added",
       "High-fiber cereal with 5 g or more fiber in a serving",
       "Oatmeal (steel-cut or regular)",
       "High-fat snack crackers"
]

#celieac disease
cdb= [
    "Gluten-free oatmeal",
    "Mixed berries",
    "Chopped nuts",
    "Sliced turkey on warmed corn tortillas with baby carrots",
    "Grilled sliced chicken over mixed greens",
    "Chicken salad made with cooked chicken",
    "Broiled sirloin burger with lettuce, tomato, sliced onion",
    "Cottage cheese with mixed fruit"
]

cdl= [
    "Quinoa and black bean salad",
    "Grilled chicken breast",
    "Spinach",
    "Applesauce with cinnamon",
    "Canned fruit in its own juices",
    "Strawberries with Cool Whip",
    "Hard-boiled egg",
    "Creamy Egg Salad",
    "Shrimp Avacado Salad",
    "Bean and Beaf Slow cooked Chilli"
]

cdd = [
    "Baked cod",
    "Sweet potato",
    "Green beans","Salmon baked with mustard","Brown rice and steamed green beans",
    "Baked flounder cooked with chopped onions",
    "Broiled skirt steak with garlic, onion powder",
    "Rice, corn, or quinoa pasta ",
    "Frozen gluten-free pizza baked"
    "Roasted chicken with carrots"
]


no=Label(root,text="NOTE",font=font,background="#6bcb77")
no.pack()
no.place(x=450,y=450)

nam=Label(root,text="If any other \nallergic item is\nincluded in your\ncustomized\n diet, then \nkindly ignore it\nThank You",height="7",width="16",font=font,background="#ff7600")
nam.pack(side="top")
nam.place(x=450,y=490)

#labels and entry field

nam=Label(root,text="Pateint Name",height="1",width="19",font=font,background="#b4aee8")
nam.pack(side="left")
nam.place(x=5,y=75)


e1=Entry(root,font=font,background="white",width="25")
e1.pack()
e1.place(x=350,y=75)



age=Label(root,text="Pateint Age",height="1",width="19",font=font,background="#b4aee8")
age.pack(side="left")
age.place(x=5,y=150)


e2=Entry(root,font=font,background="white",width="25")
e2.pack()
e2.place(x=350,y=150)


gen=Label(root,text="Gender",height="1",width="19",font=font,background="#b4aee8")
gen.pack(side="left")
gen.place(x=5,y=225)


cat=StringVar()
opti=OptionMenu(root,cat,"Male","Female")
opti.pack()
opti.config(width = 43)
opti.place(x=350,y=225)

weig=Label(root,text="Pateint Weight(Kg)",height="1",width="19",font=font,background="#b4aee8")
weig.pack(side="left")
weig.place(x=5,y=300)


e3=Entry(root,font=font,background="white",width="25")
e3.pack()
e3.place(x=350,y=300)


#selecting disease
pdc=Label(root,text="Disease",height="1",width="19",font=font,background="#b4aee8")
pdc.pack(side="left")
pdc.place(x=5,y=375)

catg=StringVar()
opt=OptionMenu(root,catg,"Diabetes Type 1", "Diabetes Type 2","Anemia","Thyroid","Heart Diesease","Celieac Diesease")
opt.pack()
opt.config(width = 43)
opt.place(x=350,y=375)


aler=Label(root,text="Select Allergies all that apply",height="1",width="36",font=font,background="#b4aee8")
aler.pack(side="left")
aler.place(x=5,y=450)


#allergies
a1 = StringVar()
a2 = StringVar()
a3 = StringVar()
a4 = StringVar()
a5 = StringVar()
a6 = StringVar()
a7 = StringVar()




def sub():
    x=random.sample(db2,k=3)
    xx=pd.Series(list(x))
    dbb2=pd.concat([xx],axis=1)

    y=random.sample(dl2,k=3)
    yy=pd.Series(list(y))
    dll2=pd.concat([yy],axis=1)


    z=random.sample(dd2,k=3)
    zz=pd.Series(list(z))
    ddd2=pd.concat([zz],axis=1)

    #selection for anemia

    ax=random.sample(ab,k=3)
    axc=pd.Series(list(ax))
    an1=pd.concat([axc],axis=1)

    ay=random.sample(al,k=3)
    ayc=pd.Series(list(ay))
    an2=pd.concat([ayc],axis=1)


    az=random.sample(ad,k=3)
    azc=pd.Series(list(az))
    an3=pd.concat([azc],axis=1)


    #selection for thyroid

    th=random.sample(tb,k=3)
    thy=pd.Series(list(th))
    t1=pd.concat([thy],axis=1)

    th1=random.sample(tl,k=3)
    th11=pd.Series(list(th1))
    t2=pd.concat([th11],axis=1)


    th2=random.sample(td,k=3)
    th22=pd.Series(list(th2))
    t3=pd.concat([th22],axis=1)

    #selection for diabetes type 1

    o=random.sample(db1,k=3)
    oo=pd.Series(list(o))
    oo1=pd.concat([oo],axis=1)

    o1=random.sample(dl1,k=3)
    ooo=pd.Series(list(o1))
    oo2=pd.concat([ooo],axis=1)


    o2=random.sample(dd1,k=3)
    op=pd.Series(list(o2))
    oo3=pd.concat([op],axis=1)

    #selection for heart diesease
    hd=random.sample(hdb,k=3)
    hdk=pd.Series(list(hd))
    hd1=pd.concat([hdk],axis=1)

    hp=random.sample(hdl,k=3)
    hdp=pd.Series(list(hp))
    hd2=pd.concat([hdp],axis=1)

    hk=random.sample(hdd,k=3)
    hkd=pd.Series(list(hk))
    hd3=pd.concat([hkd],axis=1)


    #selection for celieac disease
    cd=random.sample(cdb,k=3)
    cdk=pd.Series(list(cd))
    cd1=pd.concat([cdk],axis=1)

    cd2=random.sample(cdl,k=3)
    cdp=pd.Series(list(cd2))
    cdpp=pd.concat([cdp],axis=1)

    cd3=random.sample(cdd,k=3)
    cdh=pd.Series(list(cd3))
    cd33=pd.concat([cdh],axis=1)
    
    

    
    a=[a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get()]
    i=0
    for i in a:
        if i=='':
            a.remove(i)
            ls = ' '.join([str(elem) for elem in a])


    if e2.get()=="" or e1.get()=="" or  e3.get()=="" or cat.get()=="" or catg.get()=="":
        messagebox.showerror("Error","Kindely Enter all values")
        return
    elif e2.get().isdigit() and e3.get().isdigit():
        l1=Label(root,text="",background="#93B1A6")
        l1.config(text="NAME:  "+e1.get().title(),font=font)
        l1.pack()
        l1.place(x=690,y=25)

        l2=Label(root,text="",background="#93B1A6")
        l2.config(text="Age:  "+e2.get().title(),font=font)
        l2.pack()
        l2.place(x=950,y=25)

        l3=Label(root,text="",background="#93B1A6")
        l3.config(text="Weight:  "+e3.get(),font=font)
        l3.pack()
        l3.place(x=1190,y=25)

        l4=Label(root,text="",background="#93B1A6")
        l4.config(text="Gender:  "+cat.get().title(),font=font)
        l4.pack()
        l4.place(x=690,y=100)

        l5=Label(root,text="",background="#93B1A6")
        l5.config(text="Disease:  "+catg.get().title(),font=font)
        l5.pack()
        l5.place(x=950,y=100)

        l6=Label(root,text="",background="#93B1A6")
        l6.config(text="Allergies:  "+ls,font=font,width=50)
        l6.pack()
        l6.place(x=690,y=175)

        lb=Label(root,text="",background="#93B1A6")
        lb.config(text="BREAKFAST:",font=font,bg="#c5ecbe")
        lb.pack()
        lb.place(x=690,y=250)

        ll=Label(root,text="",background="#93B1A6")
        ll.config(text="LUNCH:",font=font,bg="#c5ecbe")
        ll.pack()
        ll.place(x=690,y=400)

        ld=Label(root,text="",background="#93B1A6")
        ld.config(text="DINNER:",font=font,bg="#c5ecbe")
        ld.pack()
        ld.place(x=690,y=550)

        #output of diet plan as per the input

        if catg.get()=="Diabetes Type 2":
            ax=Label(root,text="",width=50)
            ax.config(text=dbb2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=280)

            ax=Label(root,text="",width=50)
            ax.config(text=dll2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=430)

            ax=Label(root,text="",width=50)
            ax.config(text=ddd2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=580)

        elif catg.get()=="Diabetes Type 1":
            ax=Label(root,text="",width=50)
            ax.config(text=oo1,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=280)

            ax=Label(root,text="",width=50)
            ax.config(text=oo2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=430)

            ax=Label(root,text="",width=50)
            ax.config(text=oo3,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=580)



        elif catg.get()=="Anemia":
            ax=Label(root,text="",width=50)
            ax.config(text=an1,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=280)

            ax=Label(root,text="",width=50)
            ax.config(text=an2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=430)

            ax=Label(root,text="",width=50)
            ax.config(text=an3,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=580)



        elif catg.get()=="Thyroid":
            ax=Label(root,text="",width=50)
            ax.config(text=t1,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=280)

            ax=Label(root,text="",width=50)
            ax.config(text=t2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=430)

            ax=Label(root,text="",width=50)
            ax.config(text=t3,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=580)

        elif catg.get()=="Heart Diesease":
            ax=Label(root,text="",width=50)
            ax.config(text=hd1,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=280)

            ax=Label(root,text="",width=50)
            ax.config(text=hd2,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=430)

            ax=Label(root,text="",width=50)
            ax.config(text=hd3,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=580)

        elif catg.get()=="Celieac Diesease":
            ax=Label(root,text="",width=50)
            ax.config(text=cd1,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=280)

            ax=Label(root,text="",width=50)
            ax.config(text=cdpp,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=430)

            ax=Label(root,text="",width=50)
            ax.config(text=cd33,font=font,bg="#d9d7f1")
            ax.pack()
            ax.place(x=690,y=580)

    else:
        messagebox.showerror("Error","Only Numaric value allowed for Weight and Age")
#allergies items
        
c1=Checkbutton(root,
                text='Eggs',
                
                variable=a1,
                onvalue='eggs',
                offvalue='',fg="black",bg="#42c2ff",width=15)
c1.pack()
c1.place(x=5,y=500)


c2=Checkbutton(root,
                text='Soyabeen', variable=a2,
                onvalue='soyabeen',
                offvalue='',fg="black",bg="#42c2ff",width=15)
c2.pack()
c2.place(x=155,y=500)

c3=Checkbutton(root,
                text='Wheat',
                
                variable=a3,
                onvalue='wheat',
                offvalue='',fg="black",bg="#42c2ff",width=15)
c3.pack()
c3.place(x=305,y=500)


c4=Checkbutton(root,
                text='Corn',
                
                variable=a4,
                onvalue='corn',offvalue='',fg="black",bg="#42c2ff",width=15)
c4.pack()
c4.place(x=5,y=550)


c5=Checkbutton(root,
                text='Food-Colour',
                
                variable=a5,
                onvalue='foodcolor',offvalue='',fg="black",bg="#42c2ff",width=15)
c5.pack()
c5.place(x=155,y=550)


c6=Checkbutton(root,
                text='Fish',
                
                variable=a6,
                onvalue='fish',offvalue='',fg="black",bg="#42c2ff",width=15)

c6.pack()
c6.place(x=305,y=550)


c7=Checkbutton(root,
                text='Peanuts',
                
                variable=a7,
                onvalue='peanuts',offvalue='',fg="black",bg="#42c2ff",width=15)
c7.pack()
c7.place(x=5,y=600)






jj=Button(root,text="Submit" ,command=sub,fg="black",bg="#6edcd9",width=39)
jj.pack()
jj.place(x=155,y=600)

root.mainloop()
