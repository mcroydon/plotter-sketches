import vsketch, random


class GridRandomSketch(vsketch.SketchClass):
    rows = vsketch.Param(12)
    cols = vsketch.Param(10)
    lines = vsketch.Param(3)

    def sample(self):
        choices = [0, 1, 2] 
        return random.sample(choices, k=1)[0]

    def makeLine(self, vsk: vsketch.Vsketch) -> None:
        vsk.line(self.sample(), self.sample(), self.sample(), self.sample())

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("11x14in", landscape=False)
        vsk.scale("cm")

        for y in range(1, self.rows):
            with vsk.pushMatrix():
                for x in range(1, self.cols):
                    with vsk.pushMatrix():
                        vsk.translate(x*3,y*3)
                        for n in range(self.lines):
                            self.makeLine(vsk)
    
    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    GridRandomSketch.display()
