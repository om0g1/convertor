import customtkinter as ctk

pady_m = 5
padx_m = 5

class LengthFrame(ctk.CTkFrame):
    def __init__ (self,master):
        super().__init__(master)
        answer_font = ctk.CTkFont("Arial",12,"bold")

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
        self.unit_values = []
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
        self.answer = ctk.CTkLabel(self, text = "", font = answer_font)
        self.answer.grid(column = 4, row = 4, pady = pady_m, padx = padx_m)

        self.bottom_frame = ctk.CTkFrame(self, fg_color = self._fg_color)
        self.bottom_frame.grid(column = 4, row = 5, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.bottom_label = ctk.CTkLabel(self.bottom_frame, text = "Input a number", text_color="red", anchor="e")

    def convert(self, current_unit, convertion_unit, event):
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
                self.bottom_label.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)

class AreaFrame(ctk.CTkFrame):
    def __init__ (self,master):
        super().__init__(master)
        answer_font = ctk.CTkFont("Arial",12,"bold")

        self.top_frame = ctk.CTkLabel(self, text = "Convert Area")
        self.top_frame.grid(column = 0, row = 0, columnspan = 5, pady = pady_m, padx = padx_m, sticky = "nsew")

        self.length_entry = ctk.CTkEntry(self, placeholder_text = "180", width=230)
        self.length_entry.grid(column = 0, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew", columnspan = 2)
        self.length_entry.bind("<Key>", command= lambda event: self.convert(self.current_unit.get(), self.conversion_unit.get(), event))
        self.warning_label = ctk.CTkLabel(self, text = "*", text_color="red")
        self.units = {
            "Square Millimeters":{
                "name":"Square Millimeters",
                "unit":"mm²",
                "conversion":(1*(10**(-6)))
            },
            "Square Centimeters":{
                "name":"Square Centimeters",
                "unit":"cm²",
                "conversion":(1*(10**(-4)))
            },
            "Square Inches":{
                "name":"Square Inches",
                "unit":"Inches²",
                "conversion":(0.0254**2)
            },
            "Square Feet":{
                "name":"Square Feet",
                "unit":"Feet",
                "conversion":(0.3048000097536**2)
            },
            "Square Yards":{
                "name":"Square Yards",
                "unit":"Yards²",
                "conversion":(0.8361269999970039)
            },
            "Square Meters":{
                "name":"Square Meters",
                "unit":"m²",
                "conversion":(1)
            },
            "Hectare":{
                "name":"Hectare",
                "unit":"ha",
                "conversion":(10**4)
            },
            "Square Kilometers":{
                "name":"Square Kilometers",
                "unit":"km²",
                "conversion":((1*(10**3))**2)
            },
            "Square Miles":{
                "name":"Square Miles",
                "unit":"Miles²",
                "conversion":(2589986.9951907200739)
            },
            "Acre":{
                "name":"Acre",
                "unit":"a",
                "conversion":(4046.856)
            }
        }
        self.unit_values = []
        for unit in self.units:
            self.unit_values.append(self.units[unit]["name"])
        self.current_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(my_value, self.conversion_unit.get(), None), width=210)
        self.current_unit.grid(column = 4, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.current_unit.set("Square Millimeters")
        self.convert_label = ctk.CTkLabel(self, text = "Convert to:", anchor="w")
        self.convert_label.grid(column = 0, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(self.current_unit.get(),my_value, None))
        self.conversion_unit.grid(column = 4, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit.set("Square Millimeters")
        self.answer_label = ctk.CTkLabel(self, text = "Answer", anchor="w")
        self.answer_label.grid(column = 0, row = 4, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.answer = ctk.CTkLabel(self, text = "", font = answer_font)
        self.answer.grid(column = 4, row = 4, pady = pady_m, padx = padx_m)

        self.bottom_frame = ctk.CTkFrame(self, fg_color = self._fg_color)
        self.bottom_frame.grid(column = 4, row = 5, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.bottom_label = ctk.CTkLabel(self.bottom_frame, text = "Input a number", text_color="red", anchor = "e")


    def convert(self, current_unit, convertion_unit, event):
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
                self.bottom_label.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)

class VolumeFrame(ctk.CTkFrame):
    def __init__ (self,master):
        super().__init__(master)
        answer_font = ctk.CTkFont("Arial",12,"bold")
    
        self.top_frame = ctk.CTkLabel(self, text = "Convert Volume")
        self.top_frame.grid(column = 0, row = 0, columnspan = 5, pady = pady_m, padx = padx_m, sticky = "nsew")

        self.length_entry = ctk.CTkEntry(self, placeholder_text = "180", width=230)
        self.length_entry.grid(column = 0, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew", columnspan = 2)
        self.length_entry.bind("<Key>", command= lambda event: self.convert(self.current_unit.get(), self.conversion_unit.get(), event))
        self.warning_label = ctk.CTkLabel(self, text = "*", text_color="red")
        self.units = {
            "Milliliters":{
                "name":"Milliliters",
                "unit":"mm",
                "conversion":(1*(10**(-6)))
            },
            "Cubic Centimeters":{
                "name":"Cubic Centimeters",
                "unit":"cm³",
                "conversion":(1*(10**(-6)))
            },
            "Cubic Inches":{
                "name":"Cubic Inches",
                "unit":"Inches³",
                "conversion":(0.0254**3)
            },
            "Cubic Feet":{
                "name":"Cubic Feet",
                "unit":"Feet",
                "conversion":(0.3048000097536**3)
            },
            "Cubic Yards":{
                "name":"Cubic Yards",
                "unit":"Yards³",
                "conversion":(0.8361269999970039**2)
            },
            "Liters":{
                "name":"Liters",
                "unit":"l",
                "conversion":(1*(10**(-3)))
            },
            "Cubic Meters":{
                "name":"Cubic Meters",
                "unit":"m³",
                "conversion":(1)
            },
            "Cubic Miles":{
                "name":"Cubic Miles",
                "unit":"Miles³",
                "conversion":(2589986.9951907200739**2)
            }
        }
        self.unit_values = []
        for unit in self.units:
            self.unit_values.append(self.units[unit]["name"])
        self.current_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(my_value, self.conversion_unit.get(), None), width=210)
        self.current_unit.grid(column = 4, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.current_unit.set("Milliliters")
        self.convert_label = ctk.CTkLabel(self, text = "Convert to:", anchor="w")
        self.convert_label.grid(column = 0, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(self.current_unit.get(),my_value, None))
        self.conversion_unit.grid(column = 4, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit.set("Milliliters")
        self.answer_label = ctk.CTkLabel(self, text = "Answer", anchor="w")
        self.answer_label.grid(column = 0, row = 4, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.answer = ctk.CTkLabel(self, text = "", font = answer_font)
        self.answer.grid(column = 4, row = 4, pady = pady_m, padx = padx_m)

        self.bottom_frame = ctk.CTkFrame(self, fg_color = self._fg_color)
        self.bottom_frame.grid(column = 4, row = 5, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.bottom_label = ctk.CTkLabel(self.bottom_frame, text = "Input a number", text_color="red", anchor = "e")


    def convert(self, current_unit, convertion_unit, event):
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
                self.bottom_label.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)