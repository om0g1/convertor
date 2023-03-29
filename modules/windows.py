import sqlite3
import customtkinter as ctk

pady_m = 5
padx_m = 5


class Settings(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        self.visible_frame = None
        self.resizable(False,False)

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(column=0,row=0,sticky="nsew",columnspan=2, pady = pady_m, padx = padx_m,)
        self.title_label = ctk.CTkLabel(self.top_frame,text="Settings")
        self.title_label.pack()

        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(column=0,row=1, sticky="nsew", pady = pady_m, padx = padx_m,)
        self.appearance_btn = ctk.CTkButton(self.left_frame, text="Appearance", command=lambda: self.switch_frame(AppearanceSettings))
        self.appearance_btn.grid(row=0, pady = pady_m, padx = padx_m,)
        self.func_btn = ctk.CTkButton(self.left_frame, text="Functionality", command=lambda: self.switch_frame(FunctionalitySettings))
        self.func_btn.grid(row=1, pady = pady_m, padx = padx_m,)


        self.right_frame = ctk.CTkFrame(self, width=300,height=300)
        self.right_frame.grid(column=1,row=1, pady = pady_m, padx = padx_m,)

    def switch_frame(self, new_frame):
        if self.visible_frame is not None:
            self.visible_frame.destroy()
        self.visible_frame = new_frame(self)
        self.visible_frame.grid(column=1, row=1, pady = pady_m, padx = padx_m,)#, sticky="nsew")
    
    def change_title(self, text_choice):
        self.title_label.configure(text=text_choice)
    
class AppearanceSettings(ctk.CTkFrame):
    def __init__ (self, master):
        super().__init__(master)
        master.change_title("Theme")

        self.change_theme_btn = ctk.CTkOptionMenu(self,values=["light","dark"], command=lambda choice: self.change_theme(choice))
        self.change_theme_btn.grid(column=0,row=0, pady = pady_m, padx = padx_m,)
        #self.change_theme_btn.set(master.master.configurations[0])

        self.change_theme_colour_btn = ctk.CTkOptionMenu(self, values=["blue","dark-blue","green","pink","sweetkind"], command= lambda choice: self.change_colour(choice))
        self.change_theme_colour_btn.grid(column=0, row=1, pady = pady_m, padx = padx_m,)
        self.change_theme_colour_warning = ctk.CTkLabel(self, text="Restart to apply changes", font=ctk.CTkFont(family="Arial"))
        self.change_theme_colour_warning.grid(column=1,row=1, pady = pady_m, padx = padx_m)

    def change_theme(self, choice):
        ctk.set_appearance_mode(choice)
        con = sqlite3.connect("data/data.db")
        cur = con.cursor()
        cur.execute("UPDATE configs SET theme = ?",(choice,))
        con.commit()
        con.close()
        
    def change_colour(self, choice):
        ctk.set_default_color_theme(choice)
        con = sqlite3.connect("data/data.db")
        cur = con.cursor()
        cur.execute("UPDATE configs SET themecolour = ?",(choice,))
        con.commit()
        con.close()

class FunctionalitySettings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        master.change_title("Functionalty")

        self.temp_label = ctk.CTkLabel(self,text="Coming soon")
        self.temp_label.pack()

class Help(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Help")
        self.resizable(False,False)

        self.side_frame = ctk.CTkFrame(self)
        self.side_frame.grid(column=0,row=0, pady = pady_m, padx = padx_m, sticky="nsew")
        self.about_btn = ctk.CTkButton(self.side_frame, text="About", command = lambda: self.switch_frame(AboutFrame))
        self.about_btn.grid(column=0, row=0, pady = pady_m, padx = padx_m,)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(column=1,row=0, pady = pady_m, padx = padx_m)
        self.visible_frame = AboutFrame(self.main_frame)
        self.visible_frame.pack(fill = ctk.BOTH, expand = 1, pady = pady_m, padx = padx_m)

    def switch_frame(self, new_frame):
        if self.visible_frame is not None:
            self.visible_frame.destroy()
        self.visible_frame = new_frame(self.main_frame)
        self.visible_frame.pack(fill = ctk.BOTH, expand = 1, pady = pady_m, padx = padx_m)

class AboutFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.top_label = ctk.CTkLabel(self, text="About", anchor="center")
        self.top_label.grid(column=0, row=0, pady = pady_m, padx = padx_m)

        self.text_label = ctk.CTkLabel(self, text="This app was made by 0m0g1, read Omogi")
        self.text_label.grid(column=0, row=1, pady = pady_m, padx = padx_m)
        