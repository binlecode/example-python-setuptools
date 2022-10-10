import sys

# import os

# add project root to sys path to resolve package modules
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append("..")

from my_pkg import my_module as mm

mm.echo("hello pkg")
