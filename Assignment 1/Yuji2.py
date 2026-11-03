import matplotlib.pyplot as plt
import numpy as np

def R_total(n, A, B=2e-11):
    return B * n**2 / ((A * n) + (B * n**2))

n_plot = np.linspace(1, 1e19, 10000) # dividing by zero is bad, 1 is nearly zero

Aseven = R_total(n_plot, 1e7)
Aeight = R_total(n_plot, 1e8)
Anine = R_total(n_plot, 1e9)

plt.plot(n_plot, Aseven, c='#0000FF', label=r'$A=10^7 s^{-1}$')
plt.plot(n_plot, Aeight, c="#FF00C8", label=r'$A=10^8 s^{-1}$')
plt.plot(n_plot, Anine, c="#FF0000", label=r'$A=10^9 s^{-1}$')
plt.legend()
plt.xlabel("Carrier Concentration (cm^-3)")
plt.ylabel("IQE")
plt.title("Yuji #2 c): Varying SRH Coefficient")

plt.savefig('Yuji-2-c.png', dpi=500, bbox_inches='tight', pad_inches=0.4)



plt.clf()

# part d) below

def R_total_bimolecular(n, A=1e7):
    B = (7e-11) / (1 + (n / 5e18))
    return B * n**2 / ((A * n) + (B * n**2))

Bten = R_total(n_plot, 1e7, B=1e-10)
Beleven = R_total(n_plot, 1e7, B=1e-11)
Bbi = R_total_bimolecular(n_plot)

plt.plot(n_plot, Bten, c='#0000FF', label=r'$B=10^{-10} cm^3 s^{-1}$')
plt.plot(n_plot, Beleven, c="#FF00C8", label=r'$B=10^{-11} cm^3 s^{-1}$')
plt.plot(n_plot, Bbi, c="#FF0000", label=r'$B=B(n)$')
plt.legend()
plt.xlabel("Carrier Concentration (cm^-3)")
plt.ylabel("IQE")
plt.title("Yuji #2 d): Varying Radiative Coefficient")

plt.savefig('Yuji-2-d.png', dpi=500, bbox_inches='tight', pad_inches=0.4)



plt.clf()

# part e below

def R_total_Auger(n, C, A=1e7, B=2e-11):
    return B * n**2 / ((A * n) + (B * n**2) + (C * n**3))

C32 = R_total_Auger(n_plot, 1e-32)
C31 = R_total_Auger(n_plot, 1e-31)
C30 = R_total_Auger(n_plot, 1e-30)

plt.plot(n_plot, C32, c='#0000FF', label=r'$C=10^{-32} cm^6 s^{-1}$')
plt.plot(n_plot, C31, c="#FF00C8", label=r'$C=10^{-31} cm^6 s^{-1}$')
plt.plot(n_plot, C30, c="#FF0000", label=r'$C=10^{-30} cm^6 s^{-1}$')
plt.legend()
plt.xlabel("Carrier Concentration (cm^-3)")
plt.ylabel("IQE")
plt.title("Yuji #2 e): Varying Auger Coefficient")

plt.savefig('Yuji-2-e.png', dpi=500, bbox_inches='tight', pad_inches=0.4)