import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1=pd.read_table(r"C:\Users\soumy\Documents\25EC01045_inv\LTSPICE SIMULATION\ltspice_simulation.txt")
df2=pd.read_table(r"C:\Users\soumy\Documents\25EC01045_inv\LTSPICE SIMULATION\ltspice_65nm")


x1=df1["gate"]
y1=df1["V(vout)"]

# print(df2.columns)
x2=df2["Vin"]
y2=df2["V(vout)"]


plt.plot(x1/5,y1/5,label="$V_{DD}$=5V")
plt.plot(x2/1.1,y2/1.1,label="Discrete 65 nm graph")

plt.xlabel("$V_{in}$/$V_{DD}$ ---->")
plt.ylabel("$V_{out}$/$V_{DD}$ ---->")
plt.title("Voltage Transfer Characteristics of CMOS Inverter(Normalized)")
plt.grid(True)
plt.legend()
plt.show()
plt.savefig("overlay.png",dpi=300)