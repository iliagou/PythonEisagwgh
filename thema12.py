def in_hull(ax2, hull):
	    """
	    Test if points in `p` are in `hull`

	    `p` should be a `NxK` coordinates of `N` points in `K` dimensions
	    `hull` is either a scipy.spatial.Delaunay object or the `MxK` array of the 
	    coordinates of `M` points in `K`dimensions for which Delaunay triangulation
	    will be computed
	    """
	    from scipy.spatial import Delaunay
	    if not isinstance(hull,Delaunay):
		hull = Delaunay(hull)

	    if hull.find_simplex(p)>=0:
			return 1
	    else: 
			return 0



import numpy as np


import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, aspect='equal')
ax2.add_patch(
    patches.Rectangle(
        (0.0, 0.0),
        1.0,
        1.0,
        fill=False      # remove background
    )
)
#fig2.savefig('rect2.png', dpi=90, bbox_inches='tight')
#plt.show()



# Convex hull of a random set of points:

from scipy.spatial import ConvexHull
points = np.random.rand(30, 2)   # 30 random points in 2-D
hull = ConvexHull(points)

# Plot it:

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# We could also have directly used the vertices of the hull, which
# for 2-D are guaranteed to be in counterclockwise order:

plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')



#in_hull(ax2, hull)


print "OKokokokokok"


plt.show()
