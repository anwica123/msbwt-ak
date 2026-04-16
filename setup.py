from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy as np

extensions = [
    "MUSCython.BasicBWT",
    "MUSCython.AlignmentUtil",
    "MUSCython.ByteBWTCython",
    "MUSCython.CompressToRLE",
    "MUSCython.GenericMerge",
    "MUSCython.LCPGen",
    "MUSCython.LZW_BWTCython",
    "MUSCython.MSBWTCompGenCython",
    "MUSCython.MSBWTGenCython",
    "MUSCython.MultimergeCython",
    "MUSCython.MultiStringBWTCython",
    "MUSCython.RLE_BWTCython",
]

ext_modules = [
    Extension(name, [name.replace(".", "/") + ".pyx"], include_dirs=[np.get_include()])
    for name in extensions
]

setup(
    name="msbwt-ak",
    packages=["MUS", "MUSCython"],
    ext_modules=cythonize(ext_modules, language_level=3),
    zip_safe=False,
)
