"""
This file hosts the first code example that will later on be updated depending
on the stage
"""

import os
# Before Source Stage
print("This is the before stage")

# code below is used to find the correct paths
current_path = os.path.dirname(os.path.realpath(__file__))
concept_cicd_dir = os.path.abspath(os.path.join(current_path, os.pardir))
target_dir = os.path.join(concept_cicd_dir, "data", "Inputs", "text.txt")
