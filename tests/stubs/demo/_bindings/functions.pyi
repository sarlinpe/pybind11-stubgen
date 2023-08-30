from __future__ import annotations

import typing

__all__ = [
    "add",
    "func_w_anon_args",
    "func_w_named_pos_args",
    "generic",
    "mul",
    "pos_kw_only_mix",
    "pos_kw_only_variadic_mix",
]

def add(arg0: int, arg1: int) -> int: ...
def func_w_anon_args(arg0: int, arg1: int, arg2: int) -> None: ...
def func_w_named_pos_args(x: int, y: int, z: int) -> None: ...
def generic(*args, **kwargs) -> None: ...
@typing.overload
def mul(x: int, y: int) -> int:
    """
    Multiply x and y (int)
    """

@typing.overload
def mul(p: float, q: float) -> float:
    """
    Multiply p and q (double)
    """

def pos_kw_only_mix(i: int, /, j: int, *, k: int) -> tuple: ...
def pos_kw_only_variadic_mix(i: int, /, j: int, *args, k: int, **kwargs) -> tuple: ...