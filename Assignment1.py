import matplotlib.pyplot as plt
import numpy as np

E_V = 0             # eV
E_C = 3.4           # eV
E_A = E_V + 0.16    # eV
E_D = E_C - 0.01    # eV

m0 = 9.11e-31       # kg
mc = 0.2 * m0       # kg
mv = 1.4 * m0       # kg

N_A = 1e18          # cm^-3
N_D = 1e14          # cm^-3

T = 300             # K

g_A = 4
g_D = 2

# easier to have the constants in good units instead of dealing with conversion later
h = 6.626e-30       # cm^2 kg / s
k_B = 1.381e-19     # cm^2 kg / (s^2 K)
k_B_eVK = 8.617e-5  # eV / K



N_C = 2 * (2 * np.pi * mc * k_B * T / (h**2))**1.5    # cm^-3
N_V = 2 * (2 * np.pi * mv * k_B * T / (h**2))**1.5    # cm^-3



def n(E_F):
    return N_C * np.exp(-(E_C - E_F) / (k_B_eVK * T))

def p(E_F):
    return N_V * np.exp(-(E_F - E_V) / (k_B_eVK * T))

def N_A_minus(E_F):
    return N_A / (1 + g_A * np.exp((E_A - E_F) / (k_B_eVK * T)))

def N_D_plus(E_F):
    return N_D / (1 + g_D * np.exp((E_F - E_D) / (k_B_eVK * T)))



E_F_plot = np.linspace(E_V - 0.4, E_C + 0.4, 10000)

n_plot = n(E_F_plot)
p_plot = p(E_F_plot)
N_A_minus_plot = N_A_minus(E_F_plot)
N_D_plus_plot = N_D_plus(E_F_plot)

negatives_plot = n_plot + N_A_minus_plot
positives_plot = p_plot + N_D_plus_plot

Fermi_true = E_F_plot[np.argmin(np.abs(negatives_plot - positives_plot))]
print(f"The true Fermi level is: {Fermi_true}")

log_n_plot = np.clip(np.log10(n_plot), 0, None)
log_p_plot = np.clip(np.log10(p_plot), 0, None)
log_N_A_minus_plot = np.log10(N_A_minus_plot)
log_N_D_plus_plot = np.log10(N_D_plus_plot)
log_negatives_plot = np.log10(negatives_plot)
log_positives_plot = np.log10(positives_plot)


#plt.yscale('log')
# maybe set y limits, this stuff is going super far from where it should
plt.plot(E_F_plot, log_n_plot, c='#0000FF', label=r'$log_{10}(n)$')
plt.plot(E_F_plot, log_N_A_minus_plot, c="#00A1A1", label=r'$log_{10}(N_A^-)$')
plt.plot(E_F_plot, log_negatives_plot, c="#00007d", label=r'$log_{10}(n + N_A^-)$')
plt.plot(E_F_plot, log_p_plot, c='#ff0000', label='$log_{10}(p)$')
plt.plot(E_F_plot, log_N_D_plus_plot, c="#c9c91e", label=r'$log_{10}(N_D^+)$')
plt.plot(E_F_plot, log_positives_plot, c="#7d0000", label=r'$log_{10}(p + N_D^+)$')
plt.axvline(Fermi_true, color='magenta', linestyle='--', label=r'The true $E_F$')
plt.legend()
plt.xlabel("Fermi Level (eV)")
plt.ylabel("Carrier Concentration (cm^-3)")
plt.title("Jena 15.1 b)")

plt.savefig('Jena-15-1-b.png', dpi=500, bbox_inches='tight', pad_inches=0.4)