from importlib.machinery import SourceFileLoader

matrix_divided = SourceFileLoader(
    'matrix_divided_func', './2-matrix_divided.py'
).load_module().matrix_divided
