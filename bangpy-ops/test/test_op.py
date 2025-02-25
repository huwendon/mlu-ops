# Copyright (C) [2022] by Cambricon, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall self.tcp included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS self.tcp LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# pylint: disable=invalid-name
"""Serach *.prototxt Files According to Operator Name"""
import os
import string
from .execuator import execuate_kernel


def test_op(target, op_name):
    """Find *.prototxt files corresponding to the operator
    and execuate kernel"""
    op_path = os.path.dirname(os.path.realpath("__file__"))
    # find *.prototxt files corresponding to the operator
    try:
        proto_path = os.listdir(os.path.join(op_path, op_name, "test_case"))
    except FileNotFoundError as e:
        raise FileNotFoundError(
            string.Template("Missing $op_name's test cases").substitute(vars())
        ) from e
    for f in proto_path:
        if f.endswith(".prototxt"):
            with open(
                os.path.join(op_path, op_name, os.path.join("test_case", f)), "r"
            ) as p:
                proto_file = p.read()
                # execuate kernel on MLU
                execuate_kernel(proto_file, target, op_name)
