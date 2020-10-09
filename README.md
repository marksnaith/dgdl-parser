<h1>DGDL Parser</h1>

The DGDL parser takes as input a DGDL description and outputs either a JSON
description of the game, or a list of syntax errors.

<h2>Getting started</h2>

The easiest way to get started is to install as a pip package. After cloning the
repository enter the directory and run:

```pip install "git+https://github.com/arg-tech/dgdl-parser.git#egg=dgdl&subdirectory=src"```

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
```

<h2>DGDL grammar</h2>

A build script is provided to allow for easy development of extensions to the core DGDL grammar.

<h3>Test mode</h3>

To test extensions, run:

```./build test -f <file>```

where <file> is a DGDL file.

<h3>Code generation</h3>

To generate python code that reflects the changes to the grammar, run:

```./build```

This will generate the python files and place them in the ../src/dgdl/antlr directory.

To use your new extensions, either:

<ol>
<li> Modify an existing file in src/dgdl/builders (e.g. if you add a new effect, modify rule_interaction_builder.py); or

<li> Create a new builder (in src/dgdl/builders) that inherits BaseDGDLBuilder. Then add your new builder to the list of builders in game_builder.py
</ol>
