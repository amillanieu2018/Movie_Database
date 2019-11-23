# Most common library to visualise data is pylab
# For its use: Add matplotlib library = From matplotlib import pylab as plt
# Pylab refered to as plt.<procedure name>
# Basic thing is to plot 2 lists. One on X and other on Y axis. Both need same number of elements.

from matplotlib import pylab as plt

series1 = []
series2 = []
series3 = []

for i in range(0, 30):
    series1.append(i) #normal progression
    series2 +=[i*i]  #squared progression
    series3 +=[i**3]    #cubic progression

#plt.plot(list(range(0,30)), series1)
#plt.plot(list(range(0,30)), series2)
#plt.plot(list(range(0,30)), series3)
#plt.show()

# Can separate these graphs via figure(). Calling it gives a new figure and
plt.figure("first")
plt.plot(list(range(0,30)), series1, "r+", label="Linear", linewidth=2, ms=10)
plt.figure("second")
plt.plot(list(range(0,30)), series2, "k^:", label="Quadratic", linewidth=0.5)
plt.legend(loc="upper left")
plt.figure("third")
plt.plot(list(range(0,30)), series3)

plt.figure("first")
plt.title("Linear")
plt.ylim(0, 1000)
plt.xlabel("Series")
plt.ylabel("Linear Progression")
plt.figure("second")
plt.title("Quadratic")
plt.figure("third")
plt.title("Cubic")
plt.ylabel("Cubic progression")
plt.show()

# xlabel() and ylabel() give names for these axis.
# title() sets a title. xlim() and ylim() change limits of each access to properly see the graphs.
# Labels are used to distinguish series of a same figure. label = "string"
# To display the label we use legend().
plt.legend(loc="upper right")

# Colors, markers & lines can be changed. Colours (r,g,b), Style("-",",","--") and Marker("o", "x")



