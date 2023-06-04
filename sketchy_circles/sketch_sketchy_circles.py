import vsketch
import numpy as np
import math


class SketchyCirclesSketch(vsketch.SketchClass):
    rows = vsketch.Param(8) # 8
    cols = vsketch.Param(6) # 6
    min_strokes = vsketch.Param(10)
    max_strokes = vsketch.Param(25)
    min_stroke_length = vsketch.Param(math.pi / 3)
    max_stroke_length = vsketch.Param(5 * math.pi / 6)
    center = vsketch.Param(2.0)
    min_rotation = vsketch.Param(-.1)
    max_rotation = vsketch.Param(.1)
    horizontal_skew = vsketch.Param(.1)
    vertical_skew = vsketch.Param(.1)
    width_skew = vsketch.Param(.1)
    height_skew = vsketch.Param(.1)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("11inx14in", landscape=False)
        vsk.scale("cm")
        for y in range(0, self.rows):
            with vsk.pushMatrix():
                for x in range(0, self.cols):
                    with vsk.pushMatrix():
                        vsk.translate(x*3,y*3)        
                        strokes = int(vsk.random(self.min_strokes, self.max_strokes))
                        print (y, x)
                        vsk.rotate(vsk.random(self.min_rotation, self.max_rotation))
                        for stroke in range(0,strokes):
                            start = vsk.random(-2 * math.pi, 2 * math.pi)
                            stop = start + vsk.random(self.min_stroke_length, self.max_stroke_length)
                            print("Start, Stop: ", start, stop)
                            vsk.arc(self.center+vsk.random(-self.horizontal_skew,self.horizontal_skew),
                                    self.center+vsk.random(-self.vertical_skew, self.vertical_skew),
                                    self.center+vsk.random(-self.width_skew,self.width_skew),
                                    self.center+vsk.random(-self.height_skew, self.height_skew),
                                    start,
                                    stop)
                    

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    SketchyCirclesSketch.display()
