import vsketch


class PenElectrophoresisSketch(vsketch.SketchClass):
    rows = vsketch.Param(250)
    cols = vsketch.Param(25)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")
        vsk.penWidth('.3mm') # Sharpie Ultra Fine

        for y in range(1, self.rows):
            with vsk.pushMatrix():
                for x in range(1, self.cols):
                    with vsk.pushMatrix():
                        random = vsk.random(.0001 * (x * y))
                        vsk.line(.5,random,0,random)
                    vsk.translate(.75, 0)
            vsk.translate(0, .1)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    PenElectrophoresisSketch.display()
