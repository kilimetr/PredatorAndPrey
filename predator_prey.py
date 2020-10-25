# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import scipy.integrate   as sc
import numpy             as np
import matplotlib.pyplot as plt
	


def fun(yvec, t, pars):
	r = pars[0]
	a = pars[1]
	b = pars[2]
	c = pars[3]
	
	x = yvec[0] # prey
	y = yvec[1] # predator
	
	dxdt = r*x   - a*x*y
	dydt = b*x*y - c*y
	
	diff = np.empty(len(yvec))
	diff = [dxdt, dydt]
	
	return diff

	
	
r = 2/3 # prey population increase rate
a = 4/3 # predation coeff
b = 1   # postproduction rate per 1 prey eaten
c = 1   # predator mortality rate


# PREY POPULATION
# for i in range(0, 9, 1):
	# pars = [r+i, a, b, c]
	# yini = [5, 5]
	# ts = np.linspace(0, 50, 50*1000)

	# result = sc.odeint(lambda y, t: fun(y, t, pars), yini, ts)

	# prey     = result[:, 0]
	# predator = result[:, 1]

	# cislo = str(r+i)
	# plt.figure("Jedna")
	# # plt.figure(cislo)
	# plt.subplot(2,1,1)
	# plt.plot(ts, prey, ts, predator)
	# plt.legend(["prey", "predator"])
	# plt.subplot(2,1,2)
	# plt.plot(prey, predator, yini[0], yini[1], "r-o" )
	# plt.pause(1)
	# # plt.show()
	
# plt.show()


# PREDATION COEFF
# for i in range(0, 9, 1):
	# pars = [r, a+i, b, c]
	# yini = [5, 5]
	# ts = np.linspace(0, 50, 50*1000)

	# result = sc.odeint(lambda y, t: fun(y, t, pars), yini, ts)

	# prey     = result[:, 0]
	# predator = result[:, 1]

	# cislo = str(r+i)
	# plt.figure("Jedna")
	# # plt.figure(cislo)
	# plt.subplot(2,1,1)
	# plt.plot(ts, prey, ts, predator)
	# plt.legend(["prey", "predator"])
	# plt.subplot(2,1,2)
	# plt.plot(prey, predator, yini[0], yini[1], "r-o" )
	# plt.pause(1)
	# plt.show()
	
# plt.show()


# POSTPRODUCTION RATE PER 1 PREY EATEN
# for i in range(0, 9, 1):
	# pars = [r, a, b+i, c]
	# yini = [5, 5]
	# ts = np.linspace(0, 50, 50*1000)

	# result = sc.odeint(lambda y, t: fun(y, t, pars), yini, ts)

	# prey     = result[:, 0]
	# predator = result[:, 1]

	# cislo = str(r+i)
	# plt.figure("Jedna")
	# # plt.figure(cislo)
	# plt.subplot(2,1,1)
	# plt.plot(ts, prey, ts, predator)
	# plt.legend(["prey", "predator"])
	# plt.subplot(2,1,2)
	# plt.plot(prey, predator, yini[0], yini[1], "r-o" )
	# plt.pause(1)
	# # plt.show()
	
# plt.show()


# PREDATOR MORTALITY RATE
for i in range(0, 9, 1):
	pars = [r, a, b, c+i]
	yini = [5, 5]
	ts = np.linspace(0, 50, 50*1000)

	result = sc.odeint(lambda y, t: fun(y, t, pars), yini, ts)

	prey     = result[:, 0]
	predator = result[:, 1]

	cislo = str(r+i)
	plt.figure("Jedna")
	# plt.figure(cislo)
	plt.subplot(2,1,1)
	plt.plot(ts, prey, ts, predator)
	plt.legend(["prey", "predator"])
	plt.subplot(2,1,2)
	plt.plot(prey, predator, yini[0], yini[1], "r-o" )
	plt.pause(1)
	plt.show()
	
plt.show()