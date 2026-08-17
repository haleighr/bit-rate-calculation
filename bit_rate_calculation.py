import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

noise_floor_dbm = -92

bandwidth_khz = 50

bandwidth = bandwidth_khz * 1000

df = pd.read_csv("dbm_measurements.csv")


print(df.columns)
# Calculate SNR in dBs

df["snr_db"] = df["dbm_measurement"] - noise_floor_dbm

# Calculate SNR power ratios

df["snr_power_ratio"] = 10 ** (df["snr_db"]/10)

# Calculate max bit rate

df["max_bit_rate"] = bandwidth * np.log2(1 + df["snr_power_ratio"])


df = df.sort_values(by="angle")

df.to_csv("output.csv", index=False)
print(df)


# plot of angle and max bit rate
fig,[[ax,ax2], [ax3,ax4]] = plt.subplots(2,2,layout="tight", figsize=(10,8))
fig.suptitle("matplotlib is dumb")


ax.plot(df['angle'], df['max_bit_rate'], color = '#FF0000', marker=".", label="my plot")
ax.set_ylim(0, None)
ax.axhline(400000, color="#0000FF", linestyle="--", label="threshold")
ax.set_title("awesome graph")
ax.set_xlabel("angle")
ax.set_ylabel("bit rate")
ax.axhspan(300000, 400000, color="#FFFF00", label="da butta zone", alpha=0.5)
ax.text(0,350000,"da butta zone", color="#000000", ha='center', va='center')



ax.grid()
ax.legend()

fig.savefig('output2.png', dpi=300)

plt.show()
