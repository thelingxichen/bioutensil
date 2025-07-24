#!/usr/bin/env python
"""
A VCFv4.0 and 4.1 parser for Python.

Online version of PyVCF documentation is available at http://pyvcf.rtfd.org/
"""


from svplex.vcf.parser import Reader, Writer
from svplex.vcf.parser import VCFReader, VCFWriter
from svplex.vcf.filters import Base as Filter
from svplex.vcf.parser import RESERVED_INFO, RESERVED_FORMAT
from svplex.vcf.sample_filter import SampleFilter

VERSION = '0.6.8'
