from scipy import stats, polyval
from pylab import plot, title, show, legend
x= [3,4, 12, 5]
y =[11, 23, 11, 34]

slope, intercept, r, p, std = stats.linregress(x,y)
ry = polyval([slope, intercept], x)

print(slope, intercept, r, p, std)
print(ry)
plot(x,y, 'k.')
plot(x,ry, 'r.-')
title('regression')

legend(['original', 'regression'])

show()