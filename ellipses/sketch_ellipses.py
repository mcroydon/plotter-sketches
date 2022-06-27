import vsketch


class EllipsesSketch(vsketch.SketchClass):
    rows = vsketch.Param(40)
    cols = vsketch.Param(25)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("11x14in", landscape=False)
        vsk.scale("cm")

        for y in range(1, self.rows):
            with vsk.pushMatrix():
                for x in range(1, self.cols):
                    with vsk.pushMatrix():
                        random = vsk.random(-x, x) + vsk.random(-y, y) + vsk.random(-5, 5)
                        vsk.rotate(random, degrees=True)
                        vsk.ellipse(vsk.random(.3, .7), vsk.random(.3, .7), vsk.random(.2, .9), vsk.random(.1, .5))
                    vsk.translate(1, 0)
            vsk.translate(0, 1)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    EllipsesSketch.display()
