from tested_file import *
from itertools import product
from typing import Tuple
 
from pytest import mark
 
# from colors import Color, Yellow, Green
# from kinds import Kind, Smooth, Brain
# from peas import Peas
 
colors = [(Yellow(), "Жёлтый"), (Green(), "Зелёный")]
kinds = [(Smooth(), "гладкий"), (Brain(), "мозговой")]
peas_word = "горошек"

sets = list(product(colors, kinds))

test_names = [
  f"{params[0][0].__class__.__qualname__} - {params[1][0].__class__.__qualname__}" 
  for params in sets
]

def pytest_generate_tests(metafunc):
    args = []
    names = []
    for color_info, kind_info in product(colors, kinds):
        color, color_str = color_info
        kind, kind_str = kind_info
        args.append([color, color_str, kind, kind_str])
        names.append(f"{color.__class__.__qualname__} - {kind.__class__.__qualname__}")
    metafunc.parametrize("color,color_str,kind,kind_str", args, ids=names)
 
 
def test_peas_str(color: Color, color_str: str, kind: Kind, kind_str: str):
    peas = Peas(color, kind)
    assert str(peas) == f"{color_str} {kind_str} {peas_word}."