from tkinter import *

root = Tk()
root.title('VIRTUAL KEYBOARD - FULL VERSION')
root.geometry('1100x650')
root.config(bg='#2c3e50')
root.attributes('-topmost', True)

# --- Variables ---
is_shift_on = False
is_caps_on = False

# --- Functions ---

def update_display(text_to_add):
    display.insert(END, text_to_add)
    display.see(END) 

def press_key(normal, shifted):
    global is_shift_on
    if is_shift_on or is_caps_on:
        update_display(shifted if shifted else normal.upper())
    else:
        update_display(normal)
    
    if is_shift_on:
        is_shift_on = False
        update_ui_state()

def special_btn(name):
    
    update_display(f"[{name}]")

def backspace():
    content = display.get("1.0", END)
    display.delete("1.0", END)
    display.insert(END, content[:-2])

def enter_key():
    update_display('\n')

def space_key():
    update_display(' ')

def tab_key():
    update_display('\t')

def shift_key():
    global is_shift_on
    is_shift_on = not is_shift_on
    update_ui_state()

def capslock_key():
    global is_caps_on
    is_caps_on = not is_caps_on
    update_ui_state()

def update_ui_state():
    if is_caps_on:
        display.config(bg='#fdf2f2')
    elif is_shift_on:
        display.config(bg='#e8f4f8')
    else:
        display.config(bg='white')

# --- UI Setup ---
display = Text(root, font=('arial', 20), height=5, bd=10, relief=FLAT)
display.grid(row=0, column=0, columnspan=20, padx=20, pady=20)
display.focus_set()

# ROW 1
row1 = [('1','!'), ('2','@'), ('3','#'), ('4','$'), ('5','%'), ('6','^'), ('7','&'), ('8','*'), ('9','('), ('0',')'), ('-','_'), ('=','+')]
for i, (n, s) in enumerate(row1):
    Button(root, text=f"{s}\n{n}", font=('arial', 12, 'bold'), width=5, command=lambda n=n, s=s: press_key(n, s), takefocus=False).grid(row=1, column=i+2, padx=2, pady=2)

Button(root, text='←', bg='pink', font=('arial', 15, 'bold'), width=8, command=backspace, takefocus=False).grid(row=1, column=14, padx=2, pady=2)

# ROW 2
Button(root, text='Tab ⇥', bg='lightgray', width=10, command=tab_key, takefocus=False).grid(row=2, column=1, columnspan=2, padx=2, pady=2)
row2 = ['q','w','e','r','t','y','u','i','o','p']
for i, l in enumerate(row2):
    Button(root, text=l.upper(), bg='gray', font=('arial', 14, 'bold'), width=5, command=lambda l=l: press_key(l, l.upper()), takefocus=False).grid(row=2, column=i+3, padx=2, pady=2)

Button(root, text='{\n[', bg='pink', width=5, command=lambda: press_key('[', '{'), takefocus=False).grid(row=2, column=13, padx=2, pady=2)
Button(root, text='Enter ↵', bg='lightgray', font=('arial', 15, 'bold'), command=enter_key, takefocus=False).grid(row=2, column=14, rowspan=2, columnspan=3, sticky='news', padx=2, pady=2)

# ROW 3
Button(root, text='CAPS', bg='lightgray', width=10, command=capslock_key, takefocus=False).grid(row=3, column=1, columnspan=2, padx=2, pady=2)
row3 = ['a','s','d','f','g','h','j','k','l']
for i, l in enumerate(row3):
    Button(root, text=l.upper(), bg='gray', font=('arial', 14, 'bold'), width=5, command=lambda l=l: press_key(l, l.upper()), takefocus=False).grid(row=3, column=i+3, padx=2, pady=2)

Button(root, text=':\n;', bg='pink', width=5, command=lambda: press_key(';', ':'), takefocus=False).grid(row=3, column=12, padx=2, pady=2)
Button(root, text='~\n#', bg='pink', width=5, command=lambda: press_key('#', '~'), takefocus=False).grid(row=3, column=13, padx=2, pady=2)

# ROW 4
Button(root, text='Shift ⇧', bg='lightgray', width=6, command=shift_key, takefocus=False).grid(row=4, column=1, padx=2, pady=2)
Button(root, text='|\n\\', bg='lightgray', width=5, command=lambda: press_key('\\', '|'), takefocus=False).grid(row=4, column=2, padx=2, pady=2)
row4 = ['z','x','c','v','b','n','m']
for i, l in enumerate(row4):
    Button(root, text=l.upper(), bg='gray', font=('arial', 14, 'bold'), width=5, command=lambda l=l: press_key(l, l.upper()), takefocus=False).grid(row=4, column=i+3, padx=2, pady=2)

Button(root, text='<', bg='pink', width=5, command=lambda: press_key(',', '<'), takefocus=False).grid(row=4, column=10, padx=2, pady=2)
Button(root, text='>', bg='pink', width=5, command=lambda: press_key('.', '>'), takefocus=False).grid(row=4, column=11, padx=2, pady=2)
Button(root, text='?', bg='pink', width=5, command=lambda: press_key('/', '?'), takefocus=False).grid(row=4, column=12, padx=2, pady=2)
Button(root, text='Shift ⇧', bg='lightgray', width=12, command=shift_key, takefocus=False).grid(row=4, column=13, columnspan=3, padx=2, pady=2)

# ROW 5
Button(root, text='Ctrl', bg='lightgray', width=6, command=lambda: special_btn('Ctrl'), takefocus=False).grid(row=5, column=1, padx=2, pady=2)
Button(root, text='Fn', bg='lightgray', width=5, command=lambda: special_btn('Fn'), takefocus=False).grid(row=5, column=2, padx=2, pady=2)
Button(root, text='❖', bg='lightgray', font=('arial', 15), width=5, command=lambda: special_btn('Win'), takefocus=False).grid(row=5, column=3, padx=2, pady=2)
Button(root, text='Alt', bg='lightgray', width=6, command=lambda: special_btn('Alt'), takefocus=False).grid(row=5, column=4, padx=2, pady=2)
Button(root, text='SPACE', bg="silver", font=('arial', 15, 'bold'), command=space_key, takefocus=False).grid(row=5, column=5, columnspan=7, sticky="news", padx=2, pady=2)
Button(root, text='AltGr', bg='lightgray', width=6, command=lambda: special_btn('AltGr'), takefocus=False).grid(row=5, column=12, padx=2, pady=2)
Button(root, text='Menu', bg='lightgray', width=6, command=lambda: special_btn('Menu'), takefocus=False).grid(row=5, column=13, padx=2, pady=2)
Button(root, text='Ctrl', bg='lightgray', width=12, command=lambda: special_btn('Ctrl'), takefocus=False).grid(row=5, column=14, columnspan=2, padx=2, pady=2)

root.mainloop()
