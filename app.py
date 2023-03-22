import math
import customtkinter as ctk

pady_m = 5
padx_m = 5
 
class convertor(ctk.CTk):
    def __init__ (self):
        super().__init__()
        self.visible_frame = None
        ctk.set_appearance_mode("dark")

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(column = 0, row=0, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.help_button = ctk.CTkButton(self.top_frame, text="Help", command = lambda: self.switch_frame(length_frame))
        self.help_button.grid(column = 0, row = 0, pady = pady_m, padx = padx_m)
        self.options_button = ctk.CTkButton(self.top_frame, text="Options", command = lambda: self.switch_frame(length_frame))
        self.options_button.grid(column = 1, row = 0, pady = pady_m, padx = padx_m)

        self.tabs = ctk.CTkScrollableFrame(self.top_frame, orientation = "horizontal", height = 35)
        self.tabs.grid(column = 0, row = 1, pady = 0, padx = 0, sticky = "nsew", columnspan = 4)
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
    
    def switch_frame(self, new_frame):
        if self.visible_frame is not None:
            self.visible_frame.destroy()
        self.visible_frame = new_frame(self)
        self.visible_frame.grid(column = 0, row = 1, pady = pady_m, padx = padx_m)
    

class length_frame(ctk.CTkFrame):
    def __init__ (self,master):
        super().__init__(master)

        self.top_frame = ctk.CTkLabel(self, text = "Convert length")
        self.top_frame.grid(column = 0, row = 0, columnspan = 4, pady = pady_m, padx = padx_m)

        self.length_input = ctk.CTkEntry(self, placeholder_text = "180")
        self.length_input.grid(column = 0, row = 1, pady = pady_m, padx = padx_m)
        self.warning_label = ctk.CTkLabel(self, text = "*", text_color="red")
        self.unit_values = ["Plancks","Angstrom","Nanometers","Millimeters","Centimeters","Cubits","Rubu","Endazi","Paces","Meters","Rods","Kilometers","Inches","Feet", "Yards","Miles","Nautical Miles", "Astronomical unit","Light Year"]
        self.length_unit = ctk.CTkOptionMenu(self, values = self.unit_values)
        self.length_unit.grid(column = 2, row = 1, pady = pady_m, padx = padx_m)
        self.top_frame = ctk.CTkLabel(self, text = "Convert to:", justify="right")
        self.top_frame.grid(column = 0, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit = ctk.CTkOptionMenu(self, values = self.unit_values)
        self.conversion_unit.grid(column = 2, row = 3, pady = pady_m, padx = padx_m)
        self.answer_label = ctk.CTkLabel(self, text = "Answer")
        self.answer_label.grid(column = 0, row = 4, pady = pady_m, padx = padx_m)
        self.answer = ctk.CTkLabel(self, text = "")
        self.answer.grid(column = 2, row = 4, pady = pady_m, padx = padx_m)
        self.Convert_btn = ctk.CTkButton(self, text = "Convert", command = self.convert)
        self.Convert_btn.grid(column = 2, row = 5, pady = pady_m, padx = padx_m)

        self.bottom_label = ctk.CTkLabel(self, text = "Input a number", text_color="red")
    
    def convert(self):
        current_unit = self.length_unit.get()
        convertion_unit = self.conversion_unit.get()
        try:
            length = float(self.length_input.get())
            if current_unit != "meters":
                if current_unit == "Plancks":
                    length = length*(1.6*(10**(-35)))
                elif current_unit == "Angstrom":
                    length = length*0.0000000001
                elif current_unit == "Nanometers":
                    length = length/1000000000
                elif current_unit == "Millimeters":
                    length = length/1000
                elif current_unit == "Centimeters":
                    length = length/100
                elif current_unit == "Cubits":
                    length = length*0.4572
                elif current_unit == "Rubu":
                    length = length*0.0815625
                elif current_unit == "Endazi":
                    length = length*0.6525
                elif current_unit == "Pace":
                    length = length*0.75
                elif current_unit == "Rods":
                    length = length*5.0292
                elif current_unit == "Kilometers":
                    length = length*1000
                elif current_unit == "Inches":
                    length = length/39.37008
                elif current_unit == "Feet":
                    length = length/3.28084
                elif current_unit == "Yards":
                    length = length/1.093613
                elif current_unit == "Miles":
                    length = length/0.000621
                elif current_unit == "Nautical Miles":
                    length = length/0.00054
                elif current_unit == "Astronomical unit":
                    length = length*(1.496*(10**11))
                elif current_unit == "Light Year":
                    length = length*(9.461*(10**15))
            if convertion_unit == "Meters":
                convertion_unit = "m"
            elif convertion_unit == "Plancks":
                length = length/(1.6*(10**(-35)))
            elif convertion_unit == "Angstrom":
                convertion_unit = "Å"
                length = length/0.0000000001
            elif convertion_unit == "Nanometers":
                convertion_unit = "nm"
                length = length*1000000000
            elif convertion_unit == "Millimeters":
                convertion_unit = "mm"
                length = length*1000
            elif convertion_unit == "Centimeters":
                convertion_unit = "cm"
                length = length*100
            elif convertion_unit == "Cubits":
                length = length/0.4572
            elif convertion_unit == "Rubu":
                length = length/0.0815625
            elif convertion_unit == "Endazi":
                length = length/0.6525
            elif convertion_unit == "Paces":
                length = length/0.75
            elif convertion_unit == "Rods":
                length = length/5.0292
            elif convertion_unit == "Kilometers":
                convertion_unit = "km"
                length = length/1000
            elif convertion_unit == "Inches":
                length = length*39.37008
            elif convertion_unit == "Feet":
                length = length*3.28084
            elif convertion_unit == "Yards":
                length = length/1.093613
            elif convertion_unit == "Miles":
                length = length/0.000621
            elif convertion_unit == "Nautical Miles":
                length = length*0.00054
            elif convertion_unit == "Astronomical unit":
                convertion_unit = "AU"
                length = length/(1.496*(10**11))
            elif convertion_unit == "Light Year":
                convertion_unit = "ly"
                length = length/(9.461*(10**15))
                
            self.answer.configure(text = f'{float(length)} {convertion_unit}')#2dp or more
            self.warning_label.grid_remove()
            self.bottom_label.grid_remove()
        except:
            self.warning_label.grid(column = 1, row = 1)
            self.bottom_label.grid(column = 2, row = 6)
            


if __name__ == "__main__":
    app = convertor()
    app.title("Convertor")
    app.resizable(False,False)
    app.mainloop()
