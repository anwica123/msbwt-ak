#from distutils.core import setup
#from distutils.extension import Extension
#from distutils.command.sdist import sdist as _sdist

from setuptools import setup
from setuptools import Extension
from setuptools.command.sdist import sdist as _sdist
from Cython.Build import cythonize
from Cython.Distutils import build_ext as _build_ext
from setuptools.command.build_ext import build_ext as _build_ext

#borrowed from online code: http://stackoverflow.com/questions/4505747/how-should-i-structure-a-python-package-that-contains-cython-code


cmdClass = {}
extModules = [] 


extModules += [Extension('MUSCython.BasicBWT', ['MUSCython/BasicBWT.pyx'], include_dirs=['.']),
               Extension('MUSCython.AlignmentUtil', ['MUSCython/AlignmentUtil.pyx'], include_dirs=['.']),
               Extension('MUSCython.ByteBWTCython', ['MUSCython/ByteBWTCython.pyx'], include_dirs=['.']),
               Extension('MUSCython.CompressToRLE', ['MUSCython/CompressToRLE.pyx'], include_dirs=['.']),
               Extension('MUSCython.GenericMerge', ['MUSCython/GenericMerge.pyx'], include_dirs=['.']),
               Extension('MUSCython.LCPGen', ['MUSCython/LCPGen.pyx'], include_dirs=['.']),
               Extension('MUSCython.LZW_BWTCython', ['MUSCython/LZW_BWTCython.pyx'], include_dirs=['.']),
               Extension('MUSCython.MSBWTCompGenCython', ['MUSCython/MSBWTCompGenCython.pyx'], include_dirs=['.']),
               Extension('MUSCython.MSBWTGenCython', ['MUSCython/MSBWTGenCython.pyx'], include_dirs=['.']),
               Extension('MUSCython.MultimergeCython', ['MUSCython/MultimergeCython.pyx'], include_dirs=['.']),
               Extension('MUSCython.MultiStringBWTCython', ['MUSCython/MultiStringBWTCython.pyx'], include_dirs=['.']),
               Extension('MUSCython.RLE_BWTCython', ['MUSCython/RLE_BWTCython.pyx'], include_dirs=['.'])]
cmdClass.update({'build_ext':_build_ext})

for m in extModules:
    m.cython_directives = {'language_level': "2"}

#this is also from the stackoverflow link above, used to auto-compile when you do the sdist command
class sdist(_sdist):
    def run(self):
        # Make sure the compiled Cython files in the distribution are up-to-date
        from Cython.Build import cythonize
        import numpy as np
        cythonize(extModules)
        _sdist.run(self)
cmdClass['sdist'] = sdist
    

class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        try:
            __builtins__.__NUMPY_SETUP__ = False
        except AttributeError as e:
            pass
        import numpy as np
        self.include_dirs.append(np.get_include())
cmdClass['build_ext']=build_ext

setup(name='msbwt3',
      version='0.1.0',
      description='Allows for merging and querying of multi-string BWTs for genomic strings',
      url='http://code.google.com/p/msbwt',
      author='James Holt',
      author_email='holtjma@cs.unc.edu',
      license='MIT',
      packages=['MUSCython'],
      package_data={'MUSCython':['BasicBWT.pxd']},
      setup_requires=['numpy'],
      scripts=['bin/msbwt3'],
      zip_safe=False,
      ext_modules=extModules,
      cmdclass=cmdClass,
      )
