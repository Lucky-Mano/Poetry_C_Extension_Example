"""Build script."""
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError

from setuptools import Extension
from setuptools.command.build_ext import build_ext

extensions = [Extension("spam.ext", sources=["spam/_extension/spammodule.c"])]


class BuildFailed(Exception):
    pass


class ExtBuilder(build_ext):
    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            print("run error")
            pass

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            print("build error")
            pass


def build(setup_kwargs):
    print("build")
    setup_kwargs.update({"ext_modules": extensions, "cmdclass": {"build_ext": ExtBuilder}})
