from tkinter import*

class Qr_Gen:
    def __init__(self, root):
        # <-------- Main Frame Size ---------->
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("Items QR Code Generator | Developed by K.Nirushana")
        self.root.resizable(False, False)

        # <-------- Heading1 ---------->
        title=Label (self.root, text ="Items QR Code Generator", font=("arial", 36), bg='#053246', fg="white").place(x=0,y=0, relwidth=1)

        # <-------- Sub Frame Size1 (Add Info Window) ---------->
        addInfo_Frame= Frame(self.root, bd=2, relief=RIDGE, bg='white')
        addInfo_Frame.place(x=50, y=100, width =500, height=380)
        
        # <-------- Heading2 ---------->
        title=Label (addInfo_Frame, text ="Add Item Details", font=("arial", 20), bg='#043256', fg="white").place(x=0,y=0, relwidth=1)

        # <-------- Label ---------->
        itemID_lbl=Label (addInfo_Frame, text ="Item ID", font=("arial", 14, 'bold'), bg="white").place(x=20,y=60)      # Item  ID
        itemName_lbl=Label (addInfo_Frame, text ="Item Name", font=("arial", 14, 'bold'), bg="white").place(x=20,y=100)     # Item Name
        itemPrice_lbl=Label (addInfo_Frame, text ="Item Price", font=("arial", 14, 'bold'), bg="white").place(x=20,y=140)       # Item Price

        # <-------- TextInput ---------->
        itemID_txt=Entry (addInfo_Frame, font=("arial", 14), bg="lightyellow").place(x=200,y=60)      # Item  ID
        itemName_txt=Entry (addInfo_Frame, font=("arial", 14), bg="lightyellow").place(x=200,y=100)     # Item Name
        itemPrice_txt=Entry (addInfo_Frame, font=("arial", 14), bg="lightyellow").place(x=200,y=140)       # Item Price

        # <-------- Buttons ---------->
        btn_generate=Button(addInfo_Frame, text='Clear', font=("arial", 16), bg="#808080", fg="white").place(x=40, y=220, width=160, height=40)      #Btn to generate code
        btn_clear=Button(addInfo_Frame, text='Generate QR Code', font=("arial", 16), bg="#191970", fg="white").place(x=240, y=220, width=200, height=40)       #Btn to clear all

        # <-------- Messages ---------->
        self.msg="QR Code Generated Successfully!!"
        self.lbl_msg=Label (addInfo_Frame, text =self.msg, font=("arial", 14), bg="white", fg="green").place(x=0,y=310, relwidth=1)

        # <--------Sub Frame Size2 (QR code window) ---------->
        qrDis_Frame= Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qrDis_Frame.place(x=590, y=100, width =270, height=380)
        
        # <-------- Heading3 ---------->
        title=Label (qrDis_Frame, text ="Item QR Code", font=("arial", 20), bg='#043256', fg="white").place(x=0,y=0, relwidth=1)

        # <-------- QR dispplay ---------->
        self.qr_code= Label(qrDis_Frame, text="QR code \nNot Available", font=("arial", 14), bg='#3f51b5', fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=45, y=100, width=180, height=180)
        
root=Tk()
obj = Qr_Gen(root)
root.mainloop()