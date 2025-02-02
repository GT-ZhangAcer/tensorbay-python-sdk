#!/usr/bin/env python3
#
# Copyright 2021 Graviti. Licensed under MIT License.
#

# pylint: disable=wrong-import-position
# pylint: disable=wrong-import-order
# pylint: disable=import-error
# pylint: disable=pointless-string-statement


"""This file includes the python code of visualization.rst."""

"""Organize a Dataset"""
from tensorbay.opendataset import BSTLD

dataset = BSTLD("path/to/dataset")
""""""

"""Visualize The Dataset"""
from pharos import visualize

visualize(dataset)
""""""

"""Visualize The Dataset On Remote Server"""
visualize(dataset, host="0.0.0.0", port=5000)
""""""
