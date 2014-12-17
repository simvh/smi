from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
m = Basemap(projection='cyl',resolution='i',  llcrnrlat=44.30,urcrnrlat=60.5,\
            llcrnrlon=4.750,urcrnrlon=18.00)
m.drawcoastlines()
#m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,5), labels=[True, True, True, False])
m.drawmeridians(np.arange(-180.,181.,5), labels=[True, False, True, True])
#m.drawmapboundary(fill_color='aqua') 
x = np.linspace(5, 18, 10)
y=np.linspace(45, 60, 10)
X,Y = np.meshgrid(x, y)
U, V = 12*(X-11), 12*(Y-52)
#Default parameters, uniform grid
m.scatter(X, Y, 3, marker='o', color='r')
#plt.show()
plt.savefig('/home/s.von.hall/seminar/bspscatter.png')
