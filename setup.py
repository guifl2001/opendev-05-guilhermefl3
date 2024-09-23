
#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_guilhermefl3',
      version='0.1',
      packages=['dev_aberto'],
      author="Guilherme Fontana",
      platforms=["Linux", "MacOS", "Windows"],
      install_requires=["requests", "Babel"],
      scripts=["scripts/hello.py"],
      )