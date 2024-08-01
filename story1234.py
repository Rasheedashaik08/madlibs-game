from tkinter import *
root = Tk()
root.title("Mad Libs Generator")
root.geometry('360x300')
root.background='Gainsboro'
root.resizable(False, False)
Label(root, font=("ALGERIAN", 16), text='*Mad Libs Generator*').place(x=70, y=7)
Label(root, font=("ALGERIAN", 16), text='Have fun!!!!').place(x=130, y=35)
root.update()
def first_madlib(win):
    pass
def second_madlib(win):
    pass
def third_madlib(win):
    pass
ml1 = Button(root, text='1.The Ant Accident', font=("vivaldi", 20), command=lambda: first_madlib(root), bg='red')
ml1.place(x=75, y=90)
ml2 = Button(root, text='2.Night dinner', font=("vivaldi", 20), command=lambda: second_madlib(root) , bg='skyblue')
ml2.place(x=75, y=150)
ml3 = Button(root, text='3.The Friendship story', font=("vivaldi", 20), command=lambda: third_madlib(root), bg='light green')
ml3.place(x=75, y=210)
def first_madlib(win):
  def finish_madlib(tl: Toplevel, animal, insect, spouse, favourite, movement, preposition):
    text = f'''
 In a city,there lived a couple,the {animal} and his {spouse} the {insect}.One day,they were returing from {favourite} by {movement}.They met with an accident.The elephant gets badly wounded,{preposition} the insect escapes scratch proof.Guess how?
 because the insect is safe rider and was wearing a helmet.'''
    tl.geometry(newGeometry='375x550')
    Label(tl, text='Your Story:', font=("Times", 13, 'bold'), background='Gold', wraplength=tl.winfo_width()).place(x=130, y=310)
    Label(tl, text=text, font=("Times", 13), background='Gold', wraplength=tl.winfo_width()).place(x=0, y=330)
  ml1_wn = Toplevel(win, bg='Gold')
  ml1_wn.title("The ant accident")
  ml1_wn.geometry('375x500')
  ml1_wn.resizable(False, False)
  Label(ml1_wn, text='The ant accident', font=("Helvetica", 20, 'bold'), bg='Gold').place(x=60, y=0)
  Label(ml1_wn, text='An animal:', font=("Times", 15), bg='Gold').place(x=0, y=35)
  Label(ml1_wn, text='An insect:', font=("Times", 15), bg='Gold').place(x=0, y=70)
  Label(ml1_wn, text='Choose your spouse:', font=("Times", 15), bg='Gold').place(x=0, y=110)
  Label(ml1_wn, text='Choose a favourite:', font=("Times", 15), bg='Gold').place(x=0, y=150)
  Label(ml1_wn, text='Choose a movement:', font=("Times", 15), bg='Gold').place(x=0, y=190)
  Label(ml1_wn, text='Choose a preposition:', font=("Times", 15), bg='Gold').place(x=0, y=230)  
  animal_entry = Entry(ml1_wn, width=17)
  animal_entry.place(x=250, y=35)
  insect_entry = Entry(ml1_wn, width=17)
  insect_entry.place(x=250, y=70)  
  spouse = ['wife', 'husband']
  favourite = ['movie', 'garden', 'mall', 'store', 'playground']
  preposition = ['but', 'and']
  movement= ['cycle', 'bike']
  spouse_opt = StringVar(ml1_wn)
  spouse_opt.set(spouse[0])
  OptionMenu(ml1_wn, spouse_opt, *spouse).place(x=270, y=110)
  favourite_opt = StringVar(ml1_wn)
  favourite_opt.set(favourite[0])
  OptionMenu(ml1_wn, favourite_opt, *favourite).place(x=255, y=150)
  movement_opt = StringVar(ml1_wn)
  movement_opt.set(movement[0])
  OptionMenu(ml1_wn, movement_opt, *movement).place(x=270, y=190)
  preposition_opt = StringVar(ml1_wn)
  preposition_opt.set(preposition[0])
  OptionMenu(ml1_wn, preposition_opt, *preposition).place(x=265, y=230)
  submit_btn = Button(ml1_wn, text="Submit", background="SteelBlue", font=('Times', 12), command=lambda:finish_madlib(ml1_wn, animal_entry.get(), insect_entry.get(),spouse_opt.get(), favourite_opt.get(), movement_opt.get(), preposition_opt.get()))
  submit_btn.place(x=150, y=300)
  ml1_wn.mainloop()
def second_madlib(win):
  def finish_madlib(tl: Toplevel, Yourname, Friendname , Drink, Food, Restaurant,Passion):
    text = f'''
{Yourname}&{Friendname} are two friends.who are {Passion},visited a {Reastaurant} & ordered {Drink}.They don't order anything to eat as they have {Food} in their briefcases which was bought from outside.The two friends take out their {Food} and started eating.The waiter comes
comes,& says you are not allowed to eat your own {Food}.The smart friends look at eachother & laugh & exchanged their {Food}.'''
    tl.geometry(newGeometry='375x700')
    Label(tl, text='Your Story:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='RoyalBlue2').place(x=130, y=335)
    Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='RoyalBlue2').place(x=0, y=360)
  ml2_wn = Toplevel(win, bg='RoyalBlue2')
  ml2_wn.title("Night dinner")
  ml2_wn.geometry('375x600')
  ml2_wn.resizable(False, False)
  Label(ml2_wn, text='Night dinner', font=("Times", 17, 'bold'), bg='RoyalBlue2').place(
    x=10, y=0)
  Label(ml2_wn, text='Yourname:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=35)
  Label(ml2_wn, text='Friendname:', font=("Times", 15), bg='RoyalBlue2').place(x=0, y=70)
  Label(ml2_wn, text='Choose Yourname :', font=("Times", 15), bg='Gold').place(x=0, y=110)
  Label(ml2_wn, text='Choose a Friendname:', font=("Times", 15), bg='Gold').place(x=0, y=150)
  Label(ml2_wn, text='Choose a Drink:', font=("Times", 15), bg='Gold').place(x=0, y=190)
  Label(ml2_wn, text='Choose a Food:', font=("Times", 15), bg='Gold').place(x=0, y=230)
  Label(ml2_wn, text='Choose passion:', font=("Times", 15), bg='Gold').place(x=0, y=110)
  Yourname_entry = Entry(ml2_wn, width=19)
  Yourname_entry.place(x=255, y=35)
  Friendname_entry = Entry(ml2_wn, width=19)
  Friendname_entry.place(x=255, y=70)
  Drink  = ['coke', 'pepsi']
  Food = ['biryani', 'sandwich']
  Passion =['doctor','engineer']
  Drink_opt = StringVar(ml2_wn)
  Drink_opt.set(Drink[0])
  OptionMenu(ml2_wn, Drink_opt, *Dink).place(x=270, y=190)
  Food_opt = StringVar(ml2_wn)
  Food_opt.set(Food[0])
  OptionMenu(ml2_wn, Food_opt, *Food).place(x=270, y=190)
  Passion_opt = StringVar(ml2_wn)
  Passion_opt.set(Passion[0])
  OptionMenu(ml2_wn, Passion_opt, *Passion).place(x=270, y=190)
  submit_btn = Button(ml2_wn, text="Submit", background="SteelBlue", font=('Times', 12), command=lambda: finish_madlib(ml2_wn, Yourname_entry.get(), Friendname_entry.get(), Drink_entry.get(), Food_entry.get(), Passion_entry.get())
   submit_btn.place(x=150, y=300)
  ml2_wn.mainloop()
def third_madlib(win):
  def finish_madlib(tl: Toplevel, boy1, boy2, girl1, girl2, animal, exclamation):
    text = f
    tl.geometry(newGeometry='375x700')
    Label(tl, text='Your Story:', font=("Times", 13, "bold"), wraplength=tl.winfo_width(), bg='DarkOrange').place(
      x=130, y=305)
    Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='DarkOrange').place(x=0, y=330)
  ml3_wn = Toplevel(win, bg='DarkOrange')
  ml3_wn.title("The Ring")
  ml3_wn.geometry('375x550')
  ml3_wn.resizable(False, False)
  Label(ml3_wn, text='The Ring - Mad Libs', font=("Times", 17, 'bold'), bg='DarkOrange').place(
    x=85, y=0)
  Label(ml3_wn, text='A boy\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=35)
  Label(ml3_wn, text='Another boy\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=70)
  Label(ml3_wn, text='A girl\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=110)
  Label(ml3_wn, text='Another girl\'s name:', font=("Times", 15), bg='DarkOrange').place(x=0, y=150)
  Label(ml3_wn, text='An animal:', font=("Times", 15), bg='DarkOrange').place(x=0, y=190)
  Label(ml3_wn, text='An exclamation:', font=("Times", 15), bg='DarkOrange').place(x=0, y=230)
  boy1_name_entry = Entry(ml3_wn, width=19)
  boy1_name_entry.place(x=255, y=35)
  boy2_name_entry = Entry(ml3_wn, width=19)
  boy2_name_entry.place(x=255, y=70)
  girl1_name_entry = Entry(ml3_wn, width=19)
  girl1_name_entry.place(x=255, y=110)
  girl2_name_entry = Entry(ml3_wn, width=19)
  girl2_name_entry.place(x=255, y=150)
  animal_entry = Entry(ml3_wn, width=19)
  animal_entry.place(x=255, y=190)
  exclamation_entry = Entry(ml3_wn, width=19)
  exclamation_entry.place(x=255, y=230)
  submit_btn = Button(ml3_wn, text="Submit", background="SteelBlue", font=('Times', 12), command=lambda: finish_madlib(ml3_wn, boy1_name_entry.get(), boy2_name_entry.get(), girl1_name_entry.get(), girl2_name_entry.get(), animal_entry.get(), exclamation_entry.get()))
  submit_btn.place(x=150, y=270)
  ml3_wn.mainloop()

