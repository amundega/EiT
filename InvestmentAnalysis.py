import matplotlib.pyplot as plt
import numpy as np

'''Calculating the capital cost'''

def cost(a, b, s, n):
    c = a + b*s**n
    return c

costTank = cost(5000, 1400, 1000, 0.7)
costFilter = cost(110000, 77000, 1.4, 0.5)
costPump = cost(6900, 206, 10.4, 0.9)
costMembrane = 0.9*10**6    # Kanskje???

eqCostUSD = costTank+costMembrane+costFilter+costPump  # Cost of equipment in USD
exRate = 11.36  # Corona
eqCost = eqCostUSD*exRate
installFactor = 1.5     # Installation factor
# materialFactor =
# locationFactor =
I = eqCost*installFactor # Initial investment
print('Initial investment: ', I, 'NOK')

'''Calculating the operating cost'''

salary = 250*40*52   # Yearly salary of a factory worker
salaryCost = salary*1.5 # Cost of worker with vacation pay and workers tax considered, 1.5 is not correct
workers = 2     # Number of workers needed
el = 0.43   # O.43 NOK/kwH
kwH = 1000*365   # Extra electricity used per year
elCost = el*kwH
opCost = salaryCost*workers + elCost    # Yearly operating cost
print('Operating cost: ', opCost)

'''Calculating the generated revenue'''

p = 5.71   # Price per kg
amount = 10*10**6   # Amount sold per year in kg
rev = p*amount
print('Revenue: ', rev)

t = 0.23    # Tax 23 percent
cf = (rev - opCost)*(1-t)     # Yearly cash flow after tax
r = 0.05    # Rate
y = []  # Cumulative cash flow
n = 21  # Number of years + 1

'''Creating a list of the cumulative cash flow after i years'''

for i in range(0, n):
    x = np.linspace(0, n-1, n)      # Years
    a = -I+cf*i/(1+r)**i
    y.append(a)

print('x =', x)
print('y =', y)

# pb = 1.5  # Payback time in number of years

plt.plot(x, y)
plt.xlabel('År')
plt.ylabel('Kumulativ kontantstrøm')
plt.title('Investeringsanalyse')
plt.xlim(0, n-1)
plt.ticklabel_format(style = 'sci')    # Can switch to plain
#plt.arrow(0, -I, pb, 0)
plt.arrow(0, 0, n-1, 0)
#plt.annotate('Tilbakebetalingstid', (1, -I))
plt.savefig('investmentAnalysis.eps', format='eps')
plt.show()