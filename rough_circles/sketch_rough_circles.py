import numpy as np
import vsketch


class RoughCirclesSketch(vsketch.SketchClass):
    rows = vsketch.Param(8)
    cols = vsketch.Param(6)
    min_strokes = vsketch.Param(3)
    max_strokes = vsketch.Param(5)


    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("9inx12in", landscape=False)
        vsk.scale("cm")

        for y in range(1, self.rows):
            with vsk.pushMatrix():
                for x in range(1, self.cols):
                    with vsk.pushMatrix():
                        vsk.translate(x*3,y*3)
                        strokes = int(vsk.random(self.min_strokes, self.max_strokes))
                        general_rotation = vsk.random(-2.5, 2.5)
                        for stroke in range(0,strokes):
                            vsk.rotate(general_rotation + vsk.random(-2, 2),degrees=True)
                            # Create an ellipse with slightly random center, width, with a little more variance in height.
                            # Playing with these various ranges will alter the look of the final sketch.
                            vsk.ellipse(1+vsk.random(-.1,.1), 1+vsk.random(-.1,.1), 2+vsk.random(-.1,.1), 2+vsk.random(-.2,.5))

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    RoughCirclesSketch.display()
