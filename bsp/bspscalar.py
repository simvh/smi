from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
m = Basemap(projection='cea',resolution='i',  llcrnrlat=44.30,urcrnrlat=60.5,\
            llcrnrlon=4.750,urcrnrlon=18.00)
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
#m.drawparallels(np.arange(-90.,91.,5))#, labels=[True, True, True, False])
#m.drawmeridians(np.arange(-180.,181.,5))#, labels=[True, False, True, True])
m.drawmapboundary(fill_color='aqua') 
x, y=7, 51
m.drawmapscale( x, y, x, y,500,  barstyle='fancy' )
#plt.title("Equidistant Cylindrical Projection")
#plt.show()
plt.savefig('/home/s.von.hall/seminar/bspscalar.png')
