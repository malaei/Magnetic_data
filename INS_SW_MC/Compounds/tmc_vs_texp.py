import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("T.dat", delim_whitespace=True)


texp=data["T_exp"]
tmc=data["T_MC"]
tmc_cor=data["T_MC*"]
xideal=data["T_exp"]
fig, ax = plt.subplots(figsize =(5, 5))
plt.plot(texp, tmc_cor,'o')
plt.plot(texp, tmc, 's', alpha=0.8,markerfacecolor='none')
plt.plot(texp, texp)


plt.show()
