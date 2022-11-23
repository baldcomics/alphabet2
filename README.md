# This is Alphabet 2

Alphabet 2 comes to help mathematicians and whom are interested in the field of mathematics. It is a new collection of mathematical symbols and formulas.

This is a Bald Comics project.

We just want to help people to have more letters.

## How to use

Just download the latest version of the .sty package and put it in your LaTeX project folder.

Then, in your LaTeX file, add the following line:

```tex
    \usepackage{alphabet2}
```

The letters follow the same syntax as Greek letters. For example,

```tex
    \ulita % Lowercase letter
    \Ulita % Uppercase letter
```

They work with all special modifiers. such as `\hat{}`.

_It's important to be using XeLaTeX or LuaLaTeX to compile your pdf file._

## How to build

If you take a look, the file is kinda unreadable. It's because it's generated from Python in order to make it easier to maintain and distribute.

You'll be needing Inkscape (with all its extensions on Arch Linux) and Python 3.6+.

All you have to do is run the following command:

```bash
    python3 makepkg.py
```

Having both `/svg` and `/tex` folders on the same directory, it will generate the `.sty` file.


