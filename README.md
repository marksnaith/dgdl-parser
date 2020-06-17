<h1>DGDL Parser</h1>

The DGDL parser takes as input a DGDL description and outputs either a JSON
description of the game, or a list of syntax errors.

<h2>Getting started</h2>

The easiest way to get started is to install as a pip package. After cloning the
repository enter the directory and run:

```pip install ./src```

Alternatively, you can place the ``./src/dgdl`` directory into any python project
and it will be available as a library in the usual way.

<h3>Usage</h3>

To parse a DGDL file whose path is provided as a command-line argument:

```
import dgdl
import sys

if name == '__main__':
  parser = dgdl.DGDLParser()
  game = parser.parser(sys.argv[1])
  print(game)
