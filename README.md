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
(sketches_env) $ vsk run 
```

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