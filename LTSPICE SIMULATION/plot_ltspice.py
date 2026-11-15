import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1=pd.read_table(r"C:\Users\soumy\Documents\25EC01045_inv\LTSPICE SIMULATION\ltspice_simulation.txt")
df2=pd.read_table(r"C:\Users\soumy\Documents\25EC01045_inv\LTSPICE SIMULATION\ltspice_simulation_9V.txt")

x1=df1["gate"]
x2=df2["gate"]
y1=df1["V(vout)"]
y2=df2["V(vout)"]

plt.plot(x1,y1,label="$V_{DD}$=5V")
plt.plot(x2,y2,label="$V_{DD}$=9V")
plt.xlabel("$V_{in}$ ---->")
plt.ylabel("$V_{out}$ ---->")
plt.title("Voltage Transfer Characteristics of CMOS Inverter")
plt.grid(True)
vm1=np.interp(2.5,y1[::-1],x1[::-1])
vm2=np.interp(4.5,y2[::-1],x2[::-1])
print(vm2)
print(vm1)
plt.text(4,4,"$V_m$ when $V_{DD}$=5V is"+str(vm1))
plt.text(4,6,"$V_m$ when $V_{DD}$=9V is"+str(vm2))
plt.legend()
plt.show()
plt.savefig("inverter_plot.png",dpi=300)