# Third-party software notices

KatieCAD itself is released under the BSD 3-Clause License (see `LICENSE`).
It uses the following third-party software. Each component stays under its own licence; the
licence texts are listed below or - for the packages that are bundled into the installers - in the
folder `licenses/` that is delivered with the program (created by `tools/lizenzen_sammeln.py`
from the exact versions that were built in).

## Python packages (requirements.txt)

| Component | Used for | Licence | Copyright / author |
|---|---|---|---|
| [ezdxf](https://github.com/mozman/ezdxf) | Reading and writing DXF files | MIT | Manfred Moitzi and contributors |
| [ezdwg](https://github.com/monozukuri-ai/ezdwg) | Reading and writing DWG files (contains a compiled Rust core) | MIT | neka-nat and contributors |
| [Pillow](https://python-pillow.org) | Importing, scaling and embedding pictures | MIT-CMU (HPND) | Jeffrey 'Alex' Clark and contributors; Secret Labs AB; Fredrik Lundh |
| [pypdf](https://github.com/py-pdf/pypdf) | Importing PDF files | BSD-3-Clause | Mathieu Fenniak and contributors |

The packages above need further packages (for example numpy, fonttools, pyparsing,
typing_extensions). They are installed together with them and are listed with their licences in
the `licenses/` folder of the installed program. Binary wheels (for example Pillow or numpy) also
contain libraries of their own (for example libjpeg, libpng, FreeType, zlib); their licence
texts are part of the package's licence file and are copied into `licenses/` as well.

## Runtime and build tools

| Component | Role | Licence |
|---|---|---|
| [Python](https://www.python.org) | Interpreter, delivered inside the installers | PSF License 2.0 |
| [Tcl/Tk](https://www.tcl.tk) | Toolkit of the user interface (Tkinter), delivered inside the installers | Tcl/Tk License (BSD-style) |
| [PyInstaller](https://pyinstaller.org) | Builds the installers; its bootloader is part of the delivered program | GPL-2.0-or-later **with a special exception** that allows distributing the resulting program under any licence |
| [Inno Setup](https://jrsoftware.org/isinfo.php) | Builds the Windows installer | Inno Setup License (not part of the program) |
| [appimagetool](https://github.com/AppImage/appimagetool) | Builds the AppImage | MIT (not part of the program) |

## Optional external program

| Component | Role | Licence |
|---|---|---|
| [LibreDWG](https://www.gnu.org/software/libredwg/) (`dwg2dxf`) | Only if the user has installed it separately: fallback for reading DWG files. It is **not** delivered with KatieCAD and is only started as a separate program. | GPL-3.0-or-later |

## Own work

The single-stroke fonts "ISO" and "ISO kursiv" (`katiecad/model/normschrift.py`), the symbol
library, title blocks and report templates are own work and are covered by the KatieCAD licence.
The proportions of the fonts follow ISO 3098 / DIN 6776; no font data of third parties is
included. Fonts installed on the user's computer are read by KatieCAD when needed and are not
copied or delivered.

## Licence texts

### MIT License (ezdxf, ezdwg)

```
MIT License

Copyright (c) the authors named above

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

The exact copyright lines of ezdxf and ezdwg are in their own licence files in `licenses/`.

### Pillow (MIT-CMU)

```
The Python Imaging Library (PIL) is

    Copyright (c) 1997-2011 by Secret Labs AB
    Copyright (c) 1995-2011 by Fredrik Lundh and contributors

Pillow is the friendly PIL fork. It is

    Copyright (c) 2010 by Jeffrey 'Alex' Clark and contributors

Like PIL, Pillow is licensed under the open source MIT-CMU License:

By obtaining, using, and/or copying this software and/or its associated
documentation, you agree that you have read, understood, and will comply
with the following terms and conditions:

Permission to use, copy, modify and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appears in all copies, and that
both that copyright notice and this permission notice appear in supporting
documentation, and that the name of Secret Labs AB or the author not be
used in advertising or publicity pertaining to distribution of the software
without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
```

The licences of the libraries inside the Pillow wheel are in `licenses/Pillow-*`.

### pypdf (BSD-3-Clause)

Copyright (c) 2006-2008, Mathieu Fenniak, with contributions by other authors. The full text
(BSD 3-Clause) with all copyright lines is in `licenses/pypdf-*`.
