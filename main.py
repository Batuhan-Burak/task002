import pandas as pd  #from stack overflow
import numpy as np

data = pd.read_csv("data/intermediate_data.csv")



print(data.head())  #for only first 5 data
print(data.columns)
data = data.sort_values("t")

#pd.set_option("display.max_rows", None)  #for print all columns
#print(df)

avgSpeed = data["speed"].mean()
print("Average speed:", avgSpeed)

maxSpeed = data["speed"].max()
print("Max speed:", maxSpeed)

totalDistance = np.trapezoid(data["speed"], data["t"])   #from stack overlflow to calculate total distance the vehicle goes
print("Total distance:", totalDistance)

hardBrakes = (data["brake"] > 70).sum()             #70 might be adjusted based on use case
print("Hard braking events:", hardBrakes)

steeringActivity = data["steer"].abs().mean()
print("Steering activity:", steeringActivity)

import matplotlib.pyplot as plt         #for graphs in the outputs

plt.figure()                                    #both these parts are from chatgpt
plt.plot(data["t"], data["speed"])          # X axis Time, Y axis speed
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed vs Time")
plt.savefig("output/speed_vs_time.png")
plt.close()

plt.figure()
plt.plot(data["t"], data["steer"])
plt.xlabel("Time (s)")
plt.ylabel("Steering Angle (deg)")
plt.title("Steering vs Time")
plt.savefig("output/steer_vs_time.png")
plt.close()
