# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:41:37 2021

@author: alexa
"""

from learntools.core import binder
binder.bind(globals())
from learntools.core import *

from learntools.python_tutorial.self_study import *
from learntools.python_tutorial.self_study import get_final_result
#from learntools.python_tutorial.self_study import get_last_printed_string



codon_dict = {
    'UCA' : 'Ser',
    'GCC' : 'Ala',
    'CGA' : 'Arg',
    'UUU' : 'Phe',
    'GGG' : 'Gly',
    'AAG' : 'Lys',
}

print('Codon UUU codes the amino acid ' + str(codon_dict['UUU']) + '.')

ex_4.check()