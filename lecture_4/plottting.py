import matplotlib.pyplot as plt

mysamples = []
mylinear = []
myquad = []
mycubic = []
myexponential = []

for i in range(20):
    mysamples.append(i)
    mylinear.append(2*i)
    myquad.append(i**2)
    mycubic.append(i**3)
    myexponential.append(1.5**i)

plt.plot(mysamples, mylinear)
plt.plot(mysamples, myquad)
plt.plot(mysamples, mycubic)
plt.plot(mysamples, myexponential)

plt.show()


plt.figure('Linear')
plt.clf()
plt.xlabel('Sample Points')
plt.ylabel('Linear Function')
plt.plot(mysamples, mylinear, label='Linear')
plt.legend()

plt.figure('Quadratic')
plt.clf()
plt.xlabel('Sample Points')
plt.ylabel('Quadratic Function')
plt.plot(mysamples, myquad, label='Quadratic')
plt.legend()

plt.figure('Cubic')
plt.clf()
plt.xlabel('Sample Points')
plt.ylabel('Cubic Function')
plt.plot(mysamples, mycubic, label='Cubic')
plt.legend()

plt.figure('Expo')
plt.clf()
plt.xlabel('Sample Points')
plt.ylabel('Exponential Function')
plt.plot(mysamples, myexponential, label='Exponential')
plt.legend()

plt.show()


plt.figure('Linear vs Quad')
plt.clf()
plt.subplot(211)
plt.yscale('log')
plt.xlabel('Sample Points')
plt.ylabel('Linear Function')
plt.plot(mysamples, mylinear, 'b-', label='Linear')
plt.legend()
plt.subplot(212)
plt.yscale('log')
plt.plot(mysamples, myquad,'g^', label='Quadratic')
plt.legend()

plt.show()


