import sys
import os

# Add the project root directory to Python's module search path
# This allows tests to import modules from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 