import kinematika  

F = float(input("Unesi silu (N): "))
m = float(input("Unesi masu (kg): "))
kinematika.jednoliko_gibanje(F, m)

v0 = float(input("Unesi početnu brzinu (m/s): "))
theta = float(input("Unesi kut otklona (stupnjevi): "))
kinematika.kosi_hitac(v0, theta)
