import vsketch
import random
import numpy as np
from scipy import interpolate


class AmoebaSketch(vsketch.SketchClass):
    rows = vsketch.Param(12)
    cols = vsketch.Param(8)
    min_radius = vsketch.Param(0.5, 0.1, 1.0)
    max_radius = vsketch.Param(1.5, 1.0, 3.0)
    min_points = vsketch.Param(7, 3, 15)
    max_points = vsketch.Param(15, 3, 30)
    
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a3", landscape=False)
        vsk.scale("cm")

        for y in range(0, self.rows):
            with vsk.pushMatrix():
                for x in range(0, self.cols):
                    with vsk.pushMatrix():
                        vsk.translate(x*3, y*3)
                        self.draw_amoeba(vsk)

    def draw_amoeba(self, vsk: vsketch.Vsketch) -> None:
        num_points = random.randint(self.min_points, self.max_points)
        angles = np.linspace(0, 2*np.pi, num_points, endpoint=False)
        
        # Generate base radii
        base_radii = np.random.uniform(self.min_radius, self.max_radius, num_points)
        
        # Modify radii based on angle to create bulbous effect
        bulb_factor = .75  # Adjust this value to control the bulbousness
        radii = base_radii * (1 + np.sin(angles * 2) * bulb_factor)
        
        # Ensure radii are within the specified range
        radii = np.clip(radii, self.min_radius, self.max_radius)
        
        points = []
        for angle, radius in zip(angles, radii):
            x = np.cos(angle) * radius
            y = np.sin(angle) * radius
            points.append((x, y))
        
        points = np.array(points)
        
        if len(points) < 4:
            # If there are less than 4 points, directly draw a polygon
            vsk.polygon(points)
        else:
            # If there are 4 or more points, perform spline interpolation
            tck, _ = interpolate.splprep([points[:,0], points[:,1]], s=0, per=True)
            smooth_points = interpolate.splev(np.linspace(0, 1, 100), tck)
            vsk.polygon(zip(smooth_points[0], smooth_points[1]))

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    AmoebaSketch.display()
