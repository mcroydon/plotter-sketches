import itertools, random
import vsketch
from shapely.geometry import LineString

class HashableLineString(LineString):
    def __hash__(self) -> int:
        return hash(self.wkt)

# Construct a grid with all possible points from 0,0 to 2,2
grid = []
for x in range(0,3):
    for y in range(0,3):
        grid.append([x,y])
print(f"grid: {grid}")

# Create all possible lines between two points within the grid
# using combinations instead of permutations to avoid duplicating
# forwards and backwards lines. 
lines = set()
for thing in itertools.combinations(grid, 2):
    print(f"possible line: {thing}")
    line = HashableLineString(thing)
    print(f"{line}")
    lines.add(line)

# Brute force creating n lines that don't overlap.
def non_overlapping_lines(num_lines=3):
    returned_lines = []
    for x in range(0, num_lines):
        found = False
        while not found:
            line = random.sample(lines, 1)[0]
            for existing_line in returned_lines:
                if existing_line.intersects(line):
                    break
                if line in returned_lines:
                    break
            else:
                returned_lines.append(line)
                found = True
    return returned_lines

class NonOverlappingLinesSketch(vsketch.SketchClass):
    rows = vsketch.Param(12)
    cols = vsketch.Param(10)

    def color(self):
        choices = [0, 1, 2]
        return random.sample(choices, k=1)[0]

    def makeLine(self, vsk: vsketch.Vsketch) -> None:
        vsk.line(non_overlapping_lines())

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("11x14in", landscape=False)
        vsk.scale("cm")

        for y in range(1, self.rows):
            with vsk.pushMatrix():
                for x in range(1, self.cols):
                    with vsk.pushMatrix():
                        vsk.translate(x*3,y*3)
                        layer = 1
                        for line in non_overlapping_lines():
                            vsk.stroke(layer)
                            vsk.geometry(line)
                            layer += 1
        # Customize pen colors to roughly match the Microns.
        vsk.vpype("color --layer 1  #00008B") # Dark Blue
        vsk.vpype("color --layer 2  #006400") # Dark Green
        vsk.vpype("color --layer 3  #483248") # Aubergine

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")

if __name__ == "__main__":
    NonOverlappingLinesSketch.display()
