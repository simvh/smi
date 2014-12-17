from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
m = Basemap(projection='cyl',resolution='i',  llcrnrlat=44.30,urcrnrlat=60.5,\
            llcrnrlon=4.750,urcrnrlon=18.00)
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,5), labels=[True, True, True, False])
m.drawmeridians(np.arange(-180.,181.,5), labels=[True, False, True, True])
m.drawmapboundary(fill_color='aqua') 
#plt.title("Equidistant Cylindrical Projection")
#plt.show()
lon, lat = 13.2437, 52.3127 # Location of Berlin
# convert to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
xpt,ypt = m(lon,lat)
# convert back to lat/lon
lonpt, latpt = m(xpt,ypt,inverse=True)
m.plot(xpt,ypt,'bo')  # plot a blue dot there
# put some text next to the dot, offset a little bit
# (the offset is in map projection coordinates)
plt.text(xpt+0.1,ypt+0.1,'Berlin (%5.1fW,%3.1fN)' % (lonpt,latpt))
plt.savefig('/home/s.von.hall/seminar/bspconvert.png')
