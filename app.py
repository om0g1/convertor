import os
import sqlite3
import customtkinter as ctk
import modules
import modules.frames as frames

pady_m = 5
padx_m = 5

#largest number
#99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

class convertor(ctk.CTk):
    def __init__ (self):
        super().__init__()
        self.ready()
        self.visible_frame = frames.LengthFrame(self)
        self.visible_window = None
        
        self.geometry("470x320")

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)

        self.header = ctk.CTkFrame(self.top_frame)
        self.header.pack(fill = ctk.X, expand = 1)
        self.options_button = ctk.CTkButton(self.header, text="Options", command = lambda: self.open_window(modules.Settings))
        self.options_button.grid(column = 0, row = 0, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.help_button = ctk.CTkButton(self.header, text="Help", command = lambda: self.open_window(modules.Help))
        self.help_button.grid(column = 1, row = 0, pady = pady_m, padx = padx_m, sticky = "nsew")
        #self.place_holder_label = ctk.CTkFrame(self.top_frame, height = 25, width = 145, fg_color=self.top_frame._fg_color)
        #self.place_holder_label.grid(column = 2, row = 0, sticky = "nsew", pady = pady_m, padx = padx_m)

        self.tabs = ctk.CTkScrollableFrame(self.top_frame, orientation = "horizontal", height = 35)
        self.tabs.pack(fill = ctk.BOTH, expand = 1)
        self.length_button = ctk.CTkButton(self.tabs, text="Length", command = lambda: self.switch_frame(frames.LengthFrame))
        self.length_button.grid(column = 1, row = 0, pady = pady_m, padx = padx_m)
        self.area_button = ctk.CTkButton(self.tabs, text="area", command = lambda: self.switch_frame(frames.AreaFrame))
        self.area_button.grid(column = 2, row = 0, pady = pady_m, padx = padx_m)
        self.volume_button = ctk.CTkButton(self.tabs, text="volume", command = lambda: self.switch_frame(frames.VolumeFrame))
        self.volume_button.grid(column = 3, row = 0, pady = pady_m, padx = padx_m)
        self.wm_button = ctk.CTkButton(self.tabs, text="mass", command = lambda: self.switch_frame(frames.MassFrame))
        self.wm_button.grid(column = 4, row = 0, pady = pady_m, padx = padx_m)
        self.temp_button = ctk.CTkButton(self.tabs, text="temperature", command = lambda: self.switch_frame(frames.TemperatureFrame))
        self.temp_button.grid(column = 5, row = 0, pady = pady_m, padx = padx_m)
        self.energy_button = ctk.CTkButton(self.tabs, text="energy", command = lambda: self.switch_frame(frames.EnergyFrame))
        self.energy_button.grid(column = 6, row = 0, pady = pady_m, padx = padx_m)
        self.speed_button = ctk.CTkButton(self.tabs, text="speed", command = lambda: self.switch_frame(frames.SpeedFrame))
        self.speed_button.grid(column = 7, row = 0, pady = pady_m, padx = padx_m)
        self.time_button = ctk.CTkButton(self.tabs, text="time", command = lambda: self.switch_frame(frames.TimeFrame))
        self.time_button.grid(column = 8, row = 0, pady = pady_m, padx = padx_m)
        self.power_button = ctk.CTkButton(self.tabs, text="power", command = lambda: self.switch_frame(frames.PowerFrame))
        self.power_button.grid(column = 9, row = 0, pady = pady_m, padx = padx_m)
        self.data_button = ctk.CTkButton(self.tabs, text="data", command = lambda: self.switch_frame(frames.DataFrame))
        self.data_button.grid(column = 10, row = 0, pady = pady_m, padx = padx_m)
        self.pressure_button = ctk.CTkButton(self.tabs, text="pressure", command = lambda: self.switch_frame(frames.PressureFrame))
        self.pressure_button.grid(column = 11, row = 0, pady = pady_m, padx = padx_m)
        self.angle_button = ctk.CTkButton(self.tabs, text="angle", command = lambda: self.switch_frame(frames.AnglesFrame))
        self.angle_button.grid(column = 12, row = 0, pady = pady_m, padx = padx_m)

        self.visible_frame.pack(fill = ctk.BOTH, expand = 1, pady = pady_m, padx = padx_m)
    
    def ready(self):
        if os.path.exists("data/data.db"):
            con = sqlite3.connect("data/data.db")
            cur = con.cursor()
            appearance_data = cur.execute('SELECT * FROM configs').fetchall()
            ctk.set_appearance_mode(appearance_data[0][0])
            ctk.set_default_color_theme(appearance_data[0][1])
        else:
            con = sqlite3.connect("data/data.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE configs(theme, themecolour)")
            cur.execute('INSERT INTO configs VALUES ("light","blue")')
            con.commit()
            self.ready()
        con.close()
        

    def switch_frame(self, new_frame):
        if self.visible_frame is not None:
            self.visible_frame.destroy()
        self.visible_frame = new_frame(self)
        self.visible_frame.pack(fill = ctk.BOTH, expand = 1, pady = pady_m, padx = padx_m)

    def open_window(self, window):
        if self.visible_window is not None:
            self.visible_window.destroy()
        self.visible_window = window(self)
            
if __name__ == "__main__":
    app = convertor()
    app.title("Convertor")
    app.resizable(False,False)
    app.mainloop()
