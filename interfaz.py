from tkinter import *

ventana=Tk()
ventana.title('Cambio de Tasa')
ventana.configure(bg='light blue')
Label(ventana,text='Tasa',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=0,column=0)
Entry(ventana,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=0,column=1)
Label(ventana,text='%',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=0,column=2)
Label(ventana,text='Inicial',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=1,column=0)
Label(ventana,text='Final',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=2,column=0)
Combobox(ventana,state='readonly',values=('Anual','Semestral','Trimestral','Bimestral','Mensual','Quincenal','Diario',' '),bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=1,column=1)

ventana.mainloop()
