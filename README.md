# plotter-sketches

A collection of sketches designed for pen plotters using the [vsketch](https://github.com/abey79/vsketch) framework. I plot mine on the [AxiDraw SE/A3](https://shop.evilmadscientist.com/productsmenu/908).

## Getting Started

The quickest way to get started is by cloning this repository and change to the directory:
```
$ git clone https://github.com/mcroydon/plotter-sketches.git
$ cd plotter-sketches
```

It's best to isolate this project in its own venv using Python 3:
```
$ python -m venv sketches_env
$ source sketches_env/bin/activate
```

You'll then want to install the prerequisites:
```
(sketches_env) $ pip install -r requirements.txt
```

From there, you can run any of the sketches interactively using the `vsk` command:
```
(sketches_env) $ vsk run pen_electrophoresis
```

## Sketches

  * [Pen Electrophoresis](https://github.com/mcroydon/plotter-sketches/blob/main/pen_electrophoresis): I really enjoy the devolving genre of plots, and this ended up reminding me a lot of [gel electrophoresis](https://en.wikipedia.org/wiki/Gel_electrophoresis).
  * [Rough Circles](https://github.com/mcroydon/plotter-sketches/blob/main/rough_circles): A first take on rough sketch-like circles. I'd like to revisit this with several Bézier curves for each circle for a more sketch-like look.
  * [Ellipses](https://github.com/mcroydon/plotter-sketches/blob/main/ellipses): A lot of very tiny ellipses stretched and rotated.
  * [Grid Random](https://github.com/mcroydon/plotter-sketches/blob/main/grid_random): Randomly generate lines on (an invisible) 3x3 grid. I'd love to explore more around imposing overlap rules and maybe generating all permutations, but it's neat on its own.
  * [Non Overlapping Lines](https://github.com/mcroydon/plotter-sketches/blob/main/non_overlapping_lines): 3 random lines on the same 3x3 grid, but no overlaps. My first multi-layer plot.
  * [NACA Airfoils](https://github.com/mcroydon/plotter-sketches/blob/main/naca_airfoils) A recreation of [a classic poster](https://www.nasa.gov/image-feature/langley/100/naca-airfoils) of 4 digit NACA airfoils.

## Creating your own sketches

The vsketch framework is a fantastic way for exploring and creating sketches. You can create your own in this repository or another using the `vsk` command:
```
(sketches_env) $ vsk init my_sketch
```

A great way to quickly iterate on your sketch is to run an interactive visualization that updates whenever you save. Here's an example using Visual Studio Code:
```
(sketches_env) $ vsk run --editor code my_sketch
```

## License

These sketches are released under the MIT License. They also include boilerplate code from [vsketch](https://github.com/abey79/vsketch), also licensed under the MIT license.