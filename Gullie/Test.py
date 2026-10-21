import numpy as np
import math
from scipy.special import jv
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import tkinter as tk
from tkinter import messagebox
import re

# =========================
# User-editable help message for invalid functions
# =========================
INVALID_FUNCTIONS_MESSAGE = """
Why did this happen?
Some functions you entered could not be plotted correctly because their values became too large, too small, or undefined for most of the graphing range.

This can occur when:
- The function grows extremely fast (e.g., exp(x) for large x).
- The function has vertical asymptotes (e.g., tan(x) near ±π/2).
- The function is undefined for certain inputs (e.g., sqrt(x) for negative x, log(x) for non-positive x).
- The function produces NaN (Not a Number) or Inf (Infinity) values during calculation.

To prevent the graph from becoming unreadable or freezing, the program:
1. Clips extreme values to a safe range.
2. Skips functions that have too few valid points to display meaningfully.

These skipped or heavily clipped functions are listed in the "Invalid Functions" legend with their assigned colors.

If you want them to plot correctly:
- Restrict the input range to avoid undefined regions.
- Use functions that grow more slowly.
- Apply transformations to keep values within a reasonable range.
"""

# Extra hyperbolic functions
def sech(x): return 1 / np.cosh(x)
def csch(x): return 1 / np.sinh(x)
def coth(x): return np.cosh(x) / np.sinh(x)

# Allowed functions for safe eval (used as locals in eval)
SAFE_FUNCS = {
    "math": math,
    "np": np,
    "jv": jv,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "sqrt": np.sqrt,
    "log": np.log,
    "exp": np.exp,
    "asin": np.arcsin,
    "acos": np.arccos,
    "atan": np.arctan,
    "sinh": np.sinh,
    "cosh": np.cosh,
    "tanh": np.tanh,
    "sech": sech,
    "csch": csch,
    "coth": coth
}

# Superscript mapping for digits and signs
SUPERSCRIPTS = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '+': '⁺', '-': '⁻'
}

def format_expr(expr):
    """Format expressions for legend with superscripts."""
    expr = re.sub(r"x\*\*([0-9+\-]+)", lambda m: "x" + ''.join(SUPERSCRIPTS.get(ch, ch) for ch in m.group(1)), expr)
    expr = re.sub(r"([0-9+\-]+)\*\*x", lambda m: ''.join(SUPERSCRIPTS.get(ch, ch) for ch in m.group(1)) + "x", expr)
    return expr

# Parse function safely
def parse_function(expr, dims=2):
    expr = expr.strip()
    try:
        # Use very restricted globals and SAFE_FUNCS for locals
        if dims == 2:
            return eval(f"lambda x: {expr}", {"__builtins__": None}, SAFE_FUNCS)
        elif dims == 3:
            return eval(f"lambda x, y: {expr}", {"__builtins__": None}, SAFE_FUNCS)
    except Exception as e:
        print(f"Invalid function '{expr}': {e}")
        return None

# Improved function splitter (handles commas inside parentheses)
def split_functions(expr_input):
    parts = []
    bracket_level = 0
    current = []
    for char in expr_input:
        if char == ',' and bracket_level == 0:
            parts.append(''.join(current).strip())
            current = []
        else:
            if char in '([{':
                bracket_level += 1
            elif char in ')]}':
                bracket_level -= 1
            current.append(char)
    if current:
        parts.append(''.join(current).strip())
    return [p for p in parts if p]

# Unlimited color cycling
def color_cycle():
    colormaps = [
        plt.cm.tab20, plt.cm.Set3, plt.cm.Paired,
        plt.cm.Accent, plt.cm.Dark2, plt.cm.tab10
    ]
    idx = 0
    while True:
        cmap = colormaps[idx % len(colormaps)]
        n = getattr(cmap, "N", 10)
        for i in range(n):
            yield cmap(i / max(1, n - 1))
        idx += 1

# Safe call wrapper
def safe_call(func, *args):
    try:
        result = func(*args)
        result = np.asarray(result, dtype=float)
        # Replace infinities and NaNs with np.nan for consistent masking
        result[~np.isfinite(result)] = np.nan
        return result
    except Exception:
        # If an error occurs, return an array of NaNs matching the first arg shape
        if args:
            try:
                shape_template = np.asarray(args[0])
                return np.full(shape_template.shape, np.nan, dtype=float)
            except Exception:
                return np.array([np.nan], dtype=float)
        return np.array([np.nan], dtype=float)

# Show invalid functions message
def show_invalid_functions_message():
    try:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Invalid Functions", INVALID_FUNCTIONS_MESSAGE)
        root.destroy()
    except Exception:
        # If tkinter not available or no display, just print
        print(INVALID_FUNCTIONS_MESSAGE)

# =========================
# Part 2 — 2D Graphing
# =========================
def plot_2d():
    expr_input = input("Enter functions of x (comma-separated): ").strip()
    expr_list = split_functions(expr_input)

    funcs = []
    valid_exprs = []
    for expr in expr_list:
        func = parse_function(expr, dims=2)
        if func:
            funcs.append(func)
            valid_exprs.append(expr)
        else:
            print(f"Could not parse: {expr}")

    if not funcs:
        print("No valid functions entered.")
        return

    x_vals = np.linspace(-10, 10, 500)
    plt.figure(figsize=(10, 6))
    colors = color_cycle()

    all_y_vals = []
    MAX_Y = 1e3
    skipped_any = False

    for func, expr in zip(funcs, valid_exprs):
        y_vals = safe_call(func, x_vals)
        mask = np.isfinite(y_vals)
        if np.sum(mask) < 5:
            print(f"Skipping '{expr}' — too few valid points.")
            skipped_any = True
            continue
        # clip extreme values to avoid plotting crazy spikes
        y_vals_clipped = np.clip(y_vals, -MAX_Y, MAX_Y)
        all_y_vals.extend(y_vals_clipped[mask])
        plt.plot(x_vals[mask], y_vals_clipped[mask], color=next(colors), label=format_expr(expr))

    if not all_y_vals:
        print("No valid y-values to display after evaluation.")
        return

    y_min, y_max = min(all_y_vals), max(all_y_vals)
    # Provide small padding; handle constant functions
    if np.isclose(y_min, y_max):
        padding = 1.0 if y_min == 0 else abs(y_min) * 0.1
        plt.ylim(y_min - padding, y_max + padding)
    else:
        plt.ylim(y_min - abs(y_min) * 0.1, y_max + abs(y_max) * 0.1)

    plt.title("2D Multiple Function Graphing Software")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

    if skipped_any:
        # Offer user information about skipped/invalid functions
        show_invalid_functions_message()

# Example entry point
if __name__ == "__main__":
    plot_2d()