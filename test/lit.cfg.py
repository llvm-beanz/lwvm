# -*- Python -*-

import os
import platform
import re
import subprocess
import locale

from lit.llvm import llvm_config
import lit.formats
import lit.util

# Configuration file for the 'lit' test runner.

# name: The name of this test suite.
config.name = 'lwvm'

# testFormat: The test format to use to interpret tests.
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)

config.suffixes = ['.yaml']

# excludes: A list of directories to exclude from the testsuite. The 'Inputs'
# subdirectories contain auxiliary inputs for various tests in their parent
# directories.
config.excludes = ['Inputs', 'CMakeLists.txt', 'README.txt', 'LICENSE.txt']

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.path.join(config.lwvm_obj_root, 'test')

# Tweak the PATH to include the tools dir and the scripts dir.
llvm_config.with_environment('PATH', config.llvm_tools_dir, append_path=True)

# Check that the object root is known.
if config.test_exec_root is None:
    lit_config.fatal('No site specific configuration available!')
    raise SystemExit

# Register substitutions
config.substitutions.append(('%python', config.python_executable))
