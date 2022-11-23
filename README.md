# Solar_System_using_OpenGL

This is a 3D simulation of the solar system, it calculates gravitational forces of each body in real time to find their positions and vector velocities.
I started out by using rudementary values for the planets initial starting positions and velocites simply based on their "speed" around the sun and their distance - lining them up along the z-axis.
However, this is incredibly innaccurate so I will transition to using NASA's JPL Horizon system to retrieve the exact information.

The project uses a PyOpenGL framework created from Lee Stemkoskis tutorial.

The framework itself here is somewhat incomplete (as I am yet to implement light tracing and textures) but is sufficient to run the simulation
