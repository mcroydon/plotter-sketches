import vsketch
from airfoils import Airfoil
from shapely.geometry import LineString


airfoil_panel_rows = (
    (   # Top Row
        ('0006', '0009', '0012', '0015', '0018', '0021'),
        ('2308', '2309', '2312', '2315', '2318', '2321'),
        ('2408', '2409', '2412', '2415', '2418', '2421'),
        ('2508', '2509', '2512', '2515', '2518', '2521'),
        ('2608', '2609', '2612', '2615', '2618', '2621'),
        ('2708', '2709', '2712', '2715', '2718', '2721'),
    ),
    (   # Middle row
        [], # Blank panel
        ('4308', '4309', '4312', '4315', '4318', '4321'),
        ('4408', '4409', '4412', '4415', '4418', '4421'),
        ('4508', '4509', '4512', '4515', '4518', '4521'),
        ('4608', '4609', '4612', '4615', '4618', '4621'),
        ('4708', '4709', '4712', '4715', '4718', '4721'),
    ),
    (   # Borrom
        [], # Blank panel
        ('6308', '6309', '6312', '6315', '6318', '6321'),
        ('6408', '6409', '6412', '6415', '6418', '6421'),
        ('6508', '6509', '6512', '6515', '6518', '6521'),
        ('6608', '6609', '6612', '6615', '6618', '6621'),
        ('6708', '6709', '6712', '6715', '6718', '6721'),
    )
)

class NacaAirfoilsSketch(vsketch.SketchClass):

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("11x14in", landscape=True)
        vsk.scale("cm")

        row_count = 0
        for panel_row in airfoil_panel_rows:
            row_count += 1
            with vsk.pushMatrix():
                panel_count = 0
                for panel in panel_row:
                    panel_count += 1
                    with vsk.pushMatrix():
                        if len(panel) == 0:
                            vsk.scale(1.5)
                            vsk.text("NACA 0006-6121", 5, 9, size="12pt", mode="label", align="center", font="futural")
                            vsk.text("Family of Airfoils", 5, 9.4, size="16pt", mode="label", align="center", font="futural")
                            vsk.text("Variable Density Wind Tunnel", 5, 9.8, size="10pt", mode="label", align="center", font="futural")
                            vsk.text("August 22, 1929", 5, 10.2, size="12pt", mode="label", align="center", font="futural")
                            vsk.text("  Each airfoil is designated by a", 3, 11, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("number of of four digits:", 3, 11.3, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("  The first represents the maximum", 3, 11.6, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("mean camber in precent of chord", 3, 11.9, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("  The second, the positon of the", 3, 12.2, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("maximum mean camber in tenths", 3, 12.5, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("of chord from the leading edge", 3, 12.8, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("  The last two the maximum thick-", 3, 13.1, size="10pt", mode="label", align="left", font="futural")
                            vsk.text("ness in percent of the chord", 3, 13.4, size="10pt", mode="label", align="left", font="futural")

                        foil_count = 0
                        for foil_ident in panel:
                            foil_count += 1
                            with vsk.pushMatrix():
                                vsk.scale(1.5)
                                vsk.translate(panel_count * 4, (6 * row_count + foil_count) * .55)
                                foil = Airfoil.NACA4(foil_ident)
                                upper_coords = []
                                for c in range(0,len(foil._x_upper)):
                                    upper_coords.append([foil._x_upper[c], 1 - foil._y_upper[c]])
                                lower_coords = []
                                for c in range(0,len(foil._x_lower)):
                                    lower_coords.append([foil._x_lower[c], 1 - foil._y_lower[c]])
                                # Begin lower coordinates from the back for one continuous loop.
                                lower_coords.reverse()
                                line = LineString(upper_coords + lower_coords)
                                vsk.geometry(line)
                                vsk.text(foil_ident, .5, 1.25, size="8pt", mode="label", align="center", font="futural")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    NacaAirfoilsSketch.display()
