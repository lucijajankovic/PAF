import matplotlib.pyplot as plt
import numpy as np
from harmonic_oscillator import HarmonicOscillator

m = 1.0
k = 1.0
x0 = 1.0
v0 = 0.0

osc = HarmonicOscillator(m, k, x0, v0)

t_max = 20
dt = 0.01
t_analit = np.linspace(0, t_max, int(t_max/dt)+1)
x_analit = osc.analiticko_rjesenje(t_analit)

dt_values = [0.1, 0.05, 0.01]
plt.figure(figsize=(15, 5))

for dt_val in dt_values:
    osc_test = HarmonicOscillator(m, k, x0, v0)
    t_num, x_num, v_num, a_num = osc_test.gibanje(t_max, dt_val)
    plt.plot(t_num, x_num, label=f'numeričko dt={dt_val}')

plt.plot(t_analit, x_analit, 'k--', label='analitičko rješenje')
plt.xlabel('vrijeme t')
plt.ylabel('položaj x')
plt.title('jednostavni harmonički oscilator - položaj')
plt.legend()
plt.grid()
plt.show()

print("period titranja (teor.):", 2 * np.pi * np.sqrt(m / k))

for dt_val in dt_values:
    osc_test = HarmonicOscillator(m, k, x0, v0)
    period = osc_test.period(100, dt_val)
    print(f"Numerički period za dt={dt_val}: {period}")

