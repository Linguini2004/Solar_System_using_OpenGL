# Solar_System_using_OpenGL

This is a 3D simulation of the solar system, it calculates the gravitational forces on each body in real time to find their positions and vector velocities.
I started out by using rudementary values for the planets initial starting positions and velocites simply based on their "speed" around the sun and their distance - lining them up along the z-axis.
However, I have now moved to using NASA's JPL Horizon system to receive exact starting positions, velocities, radii, and masses

The project uses a PyOpenGL framework created from Lee Stemkoskis tutorial.

The framework itself here is somewhat incomplete (as I am yet to implement light tracing and textures) but is sufficient to run the simulation
