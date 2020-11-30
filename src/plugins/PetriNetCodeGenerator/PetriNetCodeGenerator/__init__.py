"""
This is where the implementation of the plugin code goes.
The PetriNetCodeGenerator-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
import json
import os
import random
import shutil
from webgme_bindings import PluginBase
from mako.template import Template

# Setup a logger
logger = logging.getLogger('PetriNetCodeGenerator')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Prepare the templates
formula_code_template = Template(filename=os.path.join(os.path.dirname(__file__), 'formula_template.txt'))
formula_domain_template = Template(filename=os.path.join(os.path.dirname(__file__), 'formula_domain.txt'))

class PetriNetCodeGenerator(PluginBase):
    def main(self):
        core = self.core
        META = self.META
        root_node = self.root_node
        active_node = self.active_node
        path2node = {}

        #Collect Place, Transition, and Arc info