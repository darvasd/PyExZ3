# Copyright: see copyright.txt

from .symbolic_int import SymbolicInteger as SymInt
from .symbolic_dict import SymbolicDict as SymDict
from .symbolic_type import SymbolicType as SymType

SymType.wrap = lambda conc, sym : SymbolicInteger("se",conc,sym)
SymbolicInteger = SymInt
SymbolicDict = SymDict
SymbolicType = SymType

