import math
import customtkinter as ctk

pady_m = 5
padx_m = 5

#largest number
#99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

class convertor(ctk.CTk):
    def __init__ (self):
        super().__init__()
        self.visible_frame = length_frame(self)
        
        self.geometry("470x320")
        ctk.set_appearance_mode("dark")

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)

        self.header = ctk.CTkFrame(self.top_frame)
        self.header.pack(fill = ctk.X, expand = 1)
        self.help_button = ctk.CTkButton(self.header, text="Help", command = lambda: self.switch_frame(length_frame))
        self.help_button.grid(column = 0, row = 0, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.options_button = ctk.CTkButton(self.header, text="Options", command = lambda: self.switch_frame(length_frame))
        self.options_button.grid(column = 1, row = 0, pady = pady_m, padx = padx_m, sticky = "nsew")
        #self.place_holder_label = ctk.CTkFrame(self.top_frame, height = 25, width = 145, fg_color=self.top_frame._fg_color)
        #self.place_holder_label.grid(column = 2, row = 0, sticky = "nsew", pady = pady_m, padx = padx_m)

        self.tabs = ctk.CTkScrollableFrame(self.top_frame, orientation = "horizontal", height = 35)
        self.tabs.pack(fill = ctk.BOTH, expand = 1)
        self.length_button = ctk.CTkButton(self.tabs, text="Length", command = lambda: self.switch_frame(length_frame))
        self.length_button.grid(column = 1, row = 0, pady = pady_m, padx = padx_m)
        self.area_button = ctk.CTkButton(self.tabs, text="area", command = lambda: self.switch_frame(length_frame))
        self.area_button.grid(column = 2, row = 0, pady = pady_m, padx = padx_m)
        self.volume_button = ctk.CTkButton(self.tabs, text="volume", command = lambda: self.switch_frame(length_frame))
        self.volume_button.grid(column = 3, row = 0, pady = pady_m, padx = padx_m)
        self.wm_button = ctk.CTkButton(self.tabs, text="weight and mass", command = lambda: self.switch_frame(length_frame))
        self.wm_button.grid(column = 4, row = 0, pady = pady_m, padx = padx_m)
        self.temp_button = ctk.CTkButton(self.tabs, text="temperature", command = lambda: self.switch_frame(length_frame))
        self.temp_button.grid(column = 5, row = 0, pady = pady_m, padx = padx_m)
        self.energy_button = ctk.CTkButton(self.tabs, text="energy", command = lambda: self.switch_frame(length_frame))
        self.energy_button.grid(column = 6, row = 0, pady = pady_m, padx = padx_m)
        self.speed_button = ctk.CTkButton(self.tabs, text="speed", command = lambda: self.switch_frame(length_frame))
        self.speed_button.grid(column = 7, row = 0, pady = pady_m, padx = padx_m)
        self.time_button = ctk.CTkButton(self.tabs, text="time", command = lambda: self.switch_frame(length_frame))
        self.time_button.grid(column = 8, row = 0, pady = pady_m, padx = padx_m)
        self.power_button = ctk.CTkButton(self.tabs, text="power", command = lambda: self.switch_frame(length_frame))
        self.power_button.grid(column = 9, row = 0, pady = pady_m, padx = padx_m)
        self.data_button = ctk.CTkButton(self.tabs, text="data", command = lambda: self.switch_frame(length_frame))
        self.data_button.grid(column = 10, row = 0, pady = pady_m, padx = padx_m)
        self.pressure_button = ctk.CTkButton(self.tabs, text="pressure", command = lambda: self.switch_frame(length_frame))
        self.pressure_button.grid(column = 11, row = 0, pady = pady_m, padx = padx_m)
        self.angle_button = ctk.CTkButton(self.tabs, text="angle", command = lambda: self.switch_frame(length_frame))
        self.angle_button.grid(column = 12, row = 0, pady = pady_m, padx = padx_m)

        self.visible_frame.pack(fill = ctk.BOTH, expand = 1, pady = pady_m, padx = padx_m)
    
    def switch_frame(self, new_frame):
        if self.visible_frame is not None:
            self.visible_frame.destroy()
        self.visible_frame = new_frame(self)
        self.visible_frame.pack(fill = ctk.BOTH, expand = 1, pady = pady_m, padx = padx_m)
    

class length_frame(ctk.CTkFrame):
    def __init__ (self,master):
        super().__init__(master)

        self.top_frame = ctk.CTkLabel(self, text = "Convert length")
        self.top_frame.grid(column = 0, row = 0, columnspan = 5, pady = pady_m, padx = padx_m, sticky = "nsew")

        self.length_entry = ctk.CTkEntry(self, placeholder_text = "180", width=230)
        self.length_entry.grid(column = 0, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew", columnspan = 2)
        self.length_entry.bind("<Key>", command= lambda event: self.convert(self.current_unit.get(), self.conversion_unit.get(), event))
        self.warning_label = ctk.CTkLabel(self, text = "*", text_color="red")
        self.units = {
            "Plancks":{
                "name":"Plancks",
                "unit":"Planck",
                "conversion":(1.6*(10**(-35)))
            },
            "Angstrom":{
                "name":"Angstrom",
                "unit":"Å",
                "conversion":(1*(10**(-10)))
            },
            "Nanometers":{
                "name":"Nanometers",
                "unit":"nm",
                "conversion":(10**(-9))
            },
            "Millimeters":{
                "name":"Millimeters",
                "unit":"mm",
                "conversion":(1*(10**(-3)))
            },
            "Centimeters":{
                "name":"Centimeters",
                "unit":"cm",
                "conversion":(1*(10**(-2)))
            },
            "Inches":{
                "name":"Inches",
                "unit":"Inches",
                "conversion":(0.0254)
            },
            "Feet":{
                "name":"Feet",
                "unit":"Feet",
                "conversion":(0.3048000097536)
            },
            "Cubits":{
                "name":"Cubits",
                "unit":"Cubits",
                "conversion":(0.5334)
            },
            "Rubu":{
                "name":"Rubu",
                "unit":"Rubu",
                "conversion":(8.15625*(10**(-2)))
            },
            "Endaze":{
                "name":"Endaze",
                "unit":"Endaze",
                "conversion":(6.525*(10**(-1)))
            },
            "Paces":{
                "name":"Paces",
                "unit":"Paces",
                "conversion":(7.5*(10**(-1)))
            },
            "Yards":{
                "name":"Yards",
                "unit":"Yards",
                "conversion":(0.9144)
            },
            "Meters":{
                "name":"Meters",
                "unit":"m",
                "conversion":(1)
            },
            "Rods":{
                "name":"Rods",
                "unit":"Rods",
                "conversion":(5.0292)
            },
            "Kilometers":{
                "name":"Kilometers",
                "unit":"km",
                "conversion":(1*(10**3))
            },
            "Miles":{
                "name":"Miles",
                "unit":"Miles",
                "conversion":(1609.34)
            },
            "Nautical Miles":{
                "name":"Nautical Miles",
                "unit":"Nm",
                "conversion":(1852)
            },
            "Astronomical unit":{
                "name":"Astronomical unit",
                "unit":"AU",
                "conversion":(1.496*(10**11))
            },
            "Light Year":{
                "name":"Light Year",
                "unit":"ly",
                "conversion":(9.461*(10**15))
            },
            "Parsec":{
                "name":"Parsec",
                "unit":"pc",
                "conversion":(3.086*(10**16))
            }
        }
        self.unit_values = []#["Plancks","Angstrom","Nanometers","Millimeters","Centimeters","Inches","Feet","Cubits","Rubu","Endaze","Paces","Meters","Rods","Kilometers","Yards","Miles","Nautical Miles", "Astronomical unit","Light Year","Parsec"]
        for unit in self.units:
            self.unit_values.append(self.units[unit]["name"])
        self.current_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(my_value, self.conversion_unit.get(), None), width=210)
        self.current_unit.grid(column = 4, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.current_unit.set("Plancks")
        self.convert_label = ctk.CTkLabel(self, text = "Convert to:", anchor="w")
        self.convert_label.grid(column = 0, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(self.current_unit.get(),my_value, None))
        self.conversion_unit.grid(column = 4, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit.set("Plancks")
        self.answer_label = ctk.CTkLabel(self, text = "Answer", anchor="w")
        self.answer_label.grid(column = 0, row = 4, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.answer = ctk.CTkLabel(self, text = "")
        self.answer.grid(column = 4, row = 4, pady = pady_m, padx = padx_m)
        #self.Convert_btn = ctk.CTkButton(self, text = "Convert", command = self.convert)
        #self.Convert_btn.grid(column = 2, row = 5, pady = pady_m, padx = padx_m)

        self.bottom_label = ctk.CTkLabel(self, text = "Input a number", text_color="red")

        self.bottom_frame = ctk.CTkFrame(self, fg_color = self._fg_color)
        self.bottom_frame.grid(column = 4, row = 5, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.input_digits_count = ctk.CTkLabel(self.bottom_frame, text = "0", anchor = "e")
        self.input_digits_count.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)
        #self.answer_digits_count = ctk.CTkLabel(self.bottom_frame, text = "0")
        #self.answer_digits_count.grid(column = 1, row = 0, pady = pady_m, padx = padx_m)

    def convert(self, current_unit, convertion_unit, event):
        if self.length_entry.get() == "":
            self.input_digits_count.configure(text  = "0")
            #self.answer_digits_count.configure(text  = "0")
        else:
            self.input_digits_count.configure(text = str(len(self.length_entry.get())+1))
            #self.answer_digits_count.configure(text = str(len(self.answer._text.replace(f' {convertion_unit}',""))))
        try:
            try:
                length = float(f'{self.length_entry.get()}{event.char}')
            except:
                length = float(self.length_entry.get())
            
            length = (length*self.units[current_unit]["conversion"])/self.units[convertion_unit]["conversion"]
            self.answer.configure(text = f'{float(length)} {self.units[convertion_unit]["unit"]}')#2dp or more
            self.warning_label.grid_remove()
            self.bottom_label.grid_remove()
        except:
            if self.length_entry.get() == "":
                pass
            else:
                self.warning_label.grid(column = 2, row = 1)
                self.bottom_label.grid(column = 4, row = 5)
            
            

if __name__ == "__main__":
    app = convertor()
    app.title("Convertor")
    app.resizable(False,False)
    app.mainloop()
