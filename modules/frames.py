import customtkinter as ctk

pady_m = 5
padx_m = 5


class LayoutFrame(ctk.CTkFrame):
    def __init__ (self,master,units,title):
        super().__init__(master)
        answer_font = ctk.CTkFont("Arial",12,"bold")

        self.top_frame = ctk.CTkLabel(self, text = f'Convert {title}')
        self.top_frame.grid(column = 0, row = 0, columnspan = 5, pady = pady_m, padx = padx_m, sticky = "nsew")

        self.entry = ctk.CTkEntry(self, placeholder_text = "180", width=230)
        self.entry.grid(column = 0, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew", columnspan = 2)
        self.entry.bind("<Key>", command= lambda event: self.convert(self.current_unit.get(), self.conversion_unit.get(), event))
        self.warning_label = ctk.CTkLabel(self, text = "*", text_color="red")
        self.units = units
        self.unit_values = []
        for unit in self.units:
            self.unit_values.append(unit["name"])
        self.current_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(my_value, self.conversion_unit.get(), None), width=210)
        self.current_unit.grid(column = 4, row = 1, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.current_unit.set(str(units[0]["name"]))
        self.convert_label = ctk.CTkLabel(self, text = "Convert to:", anchor="w")
        self.convert_label.grid(column = 0, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit = ctk.CTkOptionMenu(self, values = self.unit_values, command= lambda my_value: self.convert(self.current_unit.get(),my_value, None))
        self.conversion_unit.grid(column = 4, row = 3, pady = pady_m, padx = padx_m, sticky = "nsew")
        self.conversion_unit.set(str(units[0]["name"]))
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
                value = float(f'{self.entry.get()}{event.char}')
            except:
                value = float(self.entry.get())
            
            for curnt_unit in self.units:
                if curnt_unit["name"] == current_unit:
                    for conv_unit in self.units:
                        if conv_unit["name"] == convertion_unit:
                            value = (value*curnt_unit["conversion"])/conv_unit["conversion"]
                            self.answer.configure(text = f'{float(value)} {conv_unit["unit"]}')#2dp or more
                            continue

            self.warning_label.grid_remove()
            self.bottom_label.grid_remove()
        except:
            if self.entry.get() == "":
                pass
            else:
                self.warning_label.grid(column = 2, row = 1)
                self.bottom_label.pack(fill = ctk.X, expand = 1, pady = pady_m, padx = padx_m)


class EnergyFrame(LayoutFrame):
    def __init__(self,
                master, 
                units=[
                    {
                        "name":"joules",
                        "unit":"j",
                        "conversion":1
                    }
                ], 
                 title="energy"):
        super().__init__(master, units, title)

class LengthFrame(LayoutFrame):
    def __init__(self, 
                master,
                units = [
                    {
                        "name":"Plancks",
                        "unit":"Planck",
                        "conversion":(1.6*(10**(-35)))
                    },
                    {
                        "name":"Angstrom",
                        "unit":"Å",
                        "conversion":(1*(10**(-10)))
                    },
                    {
                        "name":"Nanometers",
                        "unit":"nm",
                        "conversion":(10**(-9))
                    },
                    {
                        "name":"Millimeters",
                        "unit":"mm",
                        "conversion":(1*(10**(-3)))
                    },
                    {
                        "name":"Centimeters",
                        "unit":"cm",
                        "conversion":(1*(10**(-2)))
                    },
                    {
                        "name":"Inches",
                        "unit":"Inches",
                        "conversion":(0.0254)
                    },
                    {
                        "name":"Feet",
                        "unit":"Feet",
                        "conversion":(0.3048000097536)
                    },
                    {
                        "name":"Cubits",
                        "unit":"Cubits",
                        "conversion":(0.5334)
                    },
                    {
                        "name":"Rubu",
                        "unit":"Rubu",
                        "conversion":(8.15625*(10**(-2)))
                    },
                    {
                        "name":"Endaze",
                        "unit":"Endaze",
                        "conversion":(6.525*(10**(-1)))
                    },
                    {
                        "name":"Paces",
                        "unit":"Paces",
                        "conversion":(7.5*(10**(-1)))
                    },
                    {
                        "name":"Yards",
                        "unit":"Yards",
                        "conversion":(0.9144)
                    },
                    {
                        "name":"Meters",
                        "unit":"m",
                        "conversion":(1)
                    },
                    {
                        "name":"Rods",
                        "unit":"Rods",
                        "conversion":(5.0292)
                    },
                    {
                        "name":"Kilometers",
                        "unit":"km",
                        "conversion":(1*(10**3))
                    },
                    {
                        "name":"Miles",
                        "unit":"Miles",
                        "conversion":(1609.34)
                    },
                    {
                        "name":"Nautical Miles",
                        "unit":"Nm",
                        "conversion":(1852)
                    },
                    {
                        "name":"Astronomical unit",
                        "unit":"AU",
                        "conversion":(1.496*(10**11))
                    },
                    {
                        "name":"Light Year",
                        "unit":"ly",
                        "conversion":(9.461*(10**15))
                    },
                    {
                        "name":"Parsec",
                        "unit":"pc",
                        "conversion":(3.086*(10**16))
                    }
                        ], 
                title = "value"
                ):
        super().__init__(master, units, title)

class AreaFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Square Millimeters",
                        "unit":"mm²",
                        "conversion":(1*(10**(-6)))
                    },
                    {
                        "name":"Square Centimeters",
                        "unit":"cm²",
                        "conversion":(1*(10**(-4)))
                    },
                    {
                        "name":"Square Inches",
                        "unit":"Inches²",
                        "conversion":(0.0254**2)
                    },
                    {
                        "name":"Square Feet",
                        "unit":"sq.ft",
                        "conversion":(0.3048000097536**2)
                    },
                    {
                        "name":"Square Yards",
                        "unit":"sq.yd",
                        "conversion":(0.8361269999970039)
                    },
                    {
                        "name":"Square Meters",
                        "unit":"m²",
                        "conversion":(1)
                    },
                    {
                        "name":"Hectare",
                        "unit":"Ha",
                        "conversion":(10**4)
                    },
                    {
                        "name":"Square Kilometers",
                        "unit":"km²",
                        "conversion":((1*(10**3))**2)
                    },
                    {
                        "name":"Square Miles",
                        "unit":"mi²",
                        "conversion":(2589986.9951907200739)
                    },
                    {
                        "name":"Acre",
                        "unit":"ac",
                        "conversion":(4046.856)
                    }
                        ], 
                title="Area"
                ):
        super().__init__(master, units, title)

class VolumeFrame(LayoutFrame):
    def __init__(self,
                 master,
                 units=[
                    {
                        "name":"Milliliters",
                        "unit":"mm",
                        "conversion":(1*(10**(-6)))
                    },
                    {
                        "name":"Cubic Centimeters",
                        "unit":"cm³",
                        "conversion":(1*(10**(-6)))
                    },
                    {
                        "name":"Cubic Inches",
                        "unit":"Inches³",
                        "conversion":(0.0254**3)
                    },
                    {
                        "name":"Cubic Feet",
                        "unit":"Feet³",
                        "conversion":(0.3048000097536**3)
                    },
                    {
                        "name":"Cubic Yards",
                        "unit":"Yards³",
                        "conversion":(0.8361269999970039**2)
                    },
                    {
                        "name":"Liters",
                        "unit":"l",
                        "conversion":(1*(10**(-3)))
                    },
                    {
                        "name":"Cubic Meters",
                        "unit":"m³",
                        "conversion":(1)
                    },
                    {
                        "name":"Cubic Miles",
                        "unit":"Miles³",
                        "conversion":(2589986.9951907200739**2)
                    }
                        ],
                 title="volume"
                 ):
        super().__init__(master, units, title)

class TimeFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Microseconds",
                        "unit":"ms",
                        "conversion":(0.000001)
                    },
                    {
                        "name":"Milliseconds",
                        "unit":"ms",
                        "conversion":(0.001)
                    },
                    {
                        "name":"Seconds",
                        "unit":"s",
                        "conversion":(1)
                    },
                    {
                        "name":"Minutes",
                        "unit":"min",
                        "conversion":(60)
                    },
                    {
                        "name":"Hours",
                        "unit":"hr",
                        "conversion":(3600)
                    },
                    {
                        "name":"Days",
                        "unit":"day(s)",
                        "conversion":(86400)
                    },
                    {
                        "name":"Weeks",
                        "unit":"wks",
                        "conversion":(604800)
                    },
                    {
                        "name":"Years",
                        "unit":"yrs",
                        "conversion":(31557300)
                    }
                        ],
                title="time"
                ):
        super().__init__(master, units, title)
   
class TemperatureFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Kelvin",
                        "unit":"k",
                        "conversion":(0.000001)
                    },
                    {
                        "name":"Farenheit",
                        "unit":"F",
                        "conversion":(0.001)
                    },
                    {
                        "name":"Degrees Celcius",
                        "unit":"⁰C",
                        "conversion":(1)
                    },
                        ],
                title="temperature"
                ):
        super().__init__(master, units, title)

class AnglesFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Gradians",
                        "unit":"ᵍ",
                        "conversion":(0.9)
                    },
                    {
                        "name":"Degrees",
                        "unit":"⁰",
                        "conversion":(1)
                    },
                    {
                        "name":"Radians",
                        "unit":"ᶜ",
                        "conversion":(57.29578)
                    },
                        ],
                title="angles"
                ):
        super().__init__(master, units, title)

class SpeedFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Centimeters per second",
                        "unit":"cm⁻¹",
                        "conversion":(0.01)
                    },
                    {
                        "name":"Kilometers per hour",
                        "unit":"Kmhr⁻¹",
                        "conversion":(0.277778)
                    },
                    {
                        "name":"Meters per second",
                        "unit":"ms⁻¹",
                        "conversion":(1)
                    },
                    {
                        "name":"Feet per second",
                        "unit":"Fs⁻¹",
                        "conversion":(0.3048)
                    },
                    {
                        "name":"Knots",
                        "unit":"knots",
                        "conversion":(0.5144)
                    },
                    {
                        "name":"Miles per hour",
                        "unit":"mhr⁻¹",
                        "conversion":(0.447)
                    },
                    {
                        "name":"Kilometers per second",
                        "unit":"Kms⁻¹",
                        "conversion":(1000)
                    },
                    {
                        "name":"Mach",
                        "unit":"Mach",
                        "conversion":(340.3)
                    }
                        ],
                title="speed"
                ):
        super().__init__(master, units, title)

class PressureFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Pascal",
                        "unit":"P",
                        "conversion":(0.00001)
                    },
                    {
                        "name":"Mercury Millimeters",
                        "unit":"mmhg",
                        "conversion":(0.001316)
                    },
                    {
                        "name":"Kilopascal",
                        "unit":"⁰",
                        "conversion":(0.009869)
                    },
                    {
                        "name":"Bars",
                        "unit":"Bars",
                        "conversion":(0.986923)
                    },
                    {
                        "name":"Pounds per inch²",
                        "unit":"psi",
                        "conversion":(0.068046)
                    },
                    {
                        "name":"Atmospheres",
                        "unit":"Atmosphers",
                        "conversion":(1)
                    },
                    
                        ],
                title="pressure"
                ):
        super().__init__(master, units, title)

class PowerFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Foot-pound/min",
                        "unit":"ft⋅lbf",
                        "conversion":(0.022597)
                    },
                    {
                        "name":"Watts",
                        "unit":"Watts",
                        "conversion":(1)
                    },
                    {
                        "name":"Kilowatts",
                        "unit":"Kilowatts",
                        "conversion":(1000)
                    },
                    {
                        "name":"Horsepower",
                        "unit":"Hp",
                        "conversion":(745.6999)
                    },
                    {
                        "name":"BTUs/min",
                        "unit":"Bmin⁻¹",
                        "conversion":(17.58427)
                    },
                        ],
                title="power"
                ):
        super().__init__(master, units, title)

class EnergyFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Electron Volts",
                        "unit":"Ev",
                        "conversion":(1.602177e-19)
                    },
                    {
                        "name":"Joules",
                        "unit":"Joules",
                        "conversion":(1)
                    },
                    {
                        "name":"Kilojoules",
                        "unit":"kj",
                        "conversion":(1000)
                    },
                    {
                        "name":"Thermal calories",
                        "unit":"°C calorie",
                        "conversion":(4.184)
                    },
                    {
                        "name":"Food Calories",
                        "unit":"kcal",
                        "conversion":(4184)
                    },
                    {
                        "name":"Foot Pounds",
                        "unit":"ft⋅lbf",
                        "conversion":(1.355818)
                    },
                    {
                        "name":"British thermal units",
                        "unit":"Btu",
                        "conversion":(1,055.056)
                    },
                        ],
                title="power"
                ):
        super().__init__(master, units, title)

class DataFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Bits",
                        "unit":"bits",
                        "conversion":(0.000000125)
                    },
                    {
                        "name":"Bytes",
                        "unit":"Bytes",
                        "conversion":(0.000001)
                    },
                    {
                        "name":"Kilobits",
                        "unit":"Kbit",
                        "conversion":(0.000125)
                    },
                    {
                        "name":"Kibibits",
                        "unit":"Kb",
                        "conversion":(0.000128)
                    },
                    {
                        "name":"Kilobyte",
                        "unit":"KB",
                        "conversion":(0.001)
                    },
                    {
                        "name":"Kibibytes",
                        "unit":"KiB",
                        "conversion":(0.001024)
                    },
                    {
                        "name":"Megabits",
                        "unit":"Mbit",
                        "conversion":(0.125)
                    },
                    {
                        "name":"Mebibits",
                        "unit":"mb",
                        "conversion":(0.131072)
                    },
                    {
                        "name":"Megabytes",
                        "unit":"MB",
                        "conversion":(1)
                    },
                    {
                        "name":"Mebibytes",
                        "unit":"MiB",
                        "conversion":(0.131072)
                    },
                    {
                        "name":"Gigabits",
                        "unit":"Gbit",
                        "conversion":(125)
                    },
                    {
                        "name":"Gibibits",
                        "unit":"Gb",
                        "conversion":(134.2177)
                    },
                    {
                        "name":"Gigabytes",
                        "unit":"GB",
                        "conversion":(1000)
                    },
                    {
                        "name":"Gibibytes",
                        "unit":"GiB",
                        "conversion":(1073.742)
                    },
                    {
                        "name":"Terabits",
                        "unit":"TBit",
                        "conversion":(125000)
                    },
                    {
                        "name":"Tebibits",
                        "unit":"Tb",
                        "conversion":(137439)
                    },
                    {
                        "name":"Terabytes",
                        "unit":"TB",
                        "conversion":(1000000)
                    },
                    {
                        "name":"Tebibytes",
                        "unit":"TiB",
                        "conversion":(1000000)
                    },
                    {
                        "name":"Petabits",
                        "unit":"Pbit",
                        "conversion":(125000000)
                    },
                    {
                        "name":"Pebibits",
                        "unit":"Pb",
                        "conversion":(140737488)
                    },
                    {
                        "name":"Petabytes",
                        "unit":"PB",
                        "conversion":(1000000000)
                    },
                    {
                        "name":"Pebibytes",
                        "unit":"PiB",
                        "conversion":(1125899907)
                    },
                    {
                        "name":"Exabits",
                        "unit":"Ebit",
                        "conversion":(125000000000)
                    },
                    {
                        "name":"Exbibits",
                        "unit":"Eb",
                        "conversion":(144115188076)
                    },
                    {
                        "name":"Exabytes",
                        "unit":"EB",
                        "conversion":(1000000000000)
                    },
                    {
                        "name":"Exbibytes",
                        "unit":"EiB",
                        "conversion":(1152921504607)
                    },
                    {
                        "name":"Zetabits",
                        "unit":"Zbit",
                        "conversion":(125000000000000)
                    },
                    {
                        "name":"Zebibits",
                        "unit":"Zb",
                        "conversion":(147573952589676)
                    },
                    {
                        "name":"Zetabytes",
                        "unit":"ZB",
                        "conversion":(1.000000e+15)
                    },
                    {
                        "name":"Zebibytes",
                        "unit":"ZiB",
                        "conversion":(1.180592e+15)
                    },
                    {
                        "name":"Yottabits",
                        "unit":"Ybit",
                        "conversion":(1.250000e+17)
                    },
                    {
                        "name":"Yobibits",
                        "unit":"Yb",
                        "conversion":(1.511157e+17)
                    },
                    {
                        "name":"Yottabytes",
                        "unit":"YB",
                        "conversion":(1.000000e+18)
                    },
                    {
                        "name":"Yobibytes",
                        "unit":"YiB",
                        "conversion":(1.000000e+18)
                    }
                        ],
                title="data"
                ):
        super().__init__(master, units, title)

class MassFrame(LayoutFrame):
    def __init__(self,
                master,
                units = [
                    {
                        "name":"Carats",
                        "unit":"ct",
                        "conversion":(0.0002)
                    },
                    {
                        "name":"Milligrams",
                        "unit":"mg",
                        "conversion":(0.000001)
                    },
                    {
                        "name":"Centigrams",
                        "unit":"cg",
                        "conversion":(0.00001)
                    },
                    {
                        "name":"Decigrams",
                        "unit":"dc",
                        "conversion":(0.0001)
                    },
                    {
                        "name":"Grams",
                        "unit":"g",
                        "conversion":(0.001)
                    },
                    {
                        "name":"Dekagrams",
                        "unit":"Dg",
                        "conversion":(0.01)
                    },
                    {
                        "name":"Ounces",
                        "unit":"oz",
                        "conversion":(0.02835)
                    },
                    {
                        "name":"Hectograms",
                        "unit":"Hg",
                        "conversion":(0.1)
                    },
                    {
                        "name":"Pounds",
                        "unit":"lb",
                        "conversion":(0.453592)
                    },
                    {
                        "name":"Kilograms",
                        "unit":"Kg",
                        "conversion":(1)
                    },
                    {
                        "name":"Metrice Tonnes",
                        "unit":"t Mg",
                        "conversion":(1000)
                    },
                    {
                        "name":"Stone",
                        "unit":"st",
                        "conversion":(6.350293)
                    },
                    {
                        "name":"Short tons (US)",
                        "unit":"ST",
                        "conversion":(907.1847)
                    },
                    {
                        "name":"Long tons (UK)",
                        "unit":"LT",
                        "conversion":(1016.047)
                    }
                        ],
                title="mass"
                ):
        super().__init__(master, units, title)