'''
#Mouse Controls
Key	Action
Arrow keys	Rotate view
+	Zoom in
-	Zoom out
Home	Reset view
Mouse left-click + drag	Rotate
Mouse scroll wheel	Zoom
Shift + left-click + drag	Pan

#First Test Plan

Perfect ✅ — here’s a ready-made test plan so you can immediately verify that your final assembled Calculator.py works for both 2D and 3D plotting.

Test Plan for Calculator.py
Test 1 — 2D Plotting
Steps:

Run the program in VS Code (python Calculator.py).
At the menu, enter:1

When prompted for functions of x, paste: sin(x), cos(x), x**2, jv(0, x)

You should see:

Blue sine wave
Red cosine wave
Green parabola
Purple Bessel function of order 0
All auto-scaled to fit the window
X and Y axes centered

Test 2 — 3D Plotting
Steps:

Run the program again.
At the menu, enter:2


When prompted for functions of x and y, paste:sin(sqrt(x**2 + y**2)) / sqrt(x**2 + y**2), cos(x) * sin(y), jv(0, sqrt(x**2 + y**2))

You should see:

Multiple colored 3D surfaces
Wireframe overlay for clarity
Legend showing each function
Auto-scaled Z-axis

Keyboard Controls in 3D
While the 3D plot window is active:

Arrow keys → Rotate view
+ → Zoom in
- → Zoom out
Home → Reset view to default

Test 3 — Error Handling
Steps:

Choose 2D mode.
Enter:sin(x), badfunc(x)

Expected:

sin(x) plots normally.
Error message for badfunc(x) appears in terminal.
Program continues without crashing.

Extra Functions You Can Try
You can use NumPy, math, and SciPy special functions:
exp(-x**2)
sqrt(abs(x))
tanh(x)
sech(x)
csch(x)
coth(x)
jv(1, x)

For 3D:
sqrt(x**2 + y**2)
sin(x) * cos(y)
exp(-(x**2 + y**2) / 10)

If you want, I can also give you a bonus Part 4 that adds automatic color cycling for unlimited functions instead of just 8 colors — so you can plot 20+ functions without repeating colors.
Do you want me to add that enhancement?

sin(x), cos(x), x**2, jv(0, x)

sin(sqrt(x**2 + y**2)) / sqrt(x**2 + y**2), cos(x) * sin(y), jv(0, sqrt(x**2 + y**2))

#Second Test Plan

Perfect ✅ — here’s a ready-made test plan for your final assembled Calculator.py so you can verify everything works: autoscaling, superscript legends, unlimited color cycling, and 3D navigation.

Test Plan for Final Calculator.py
Test 1 — 2D Plotting (Scaling & Legend Formatting)
Steps:

Run the program: Bashpython Calculator.py

At the menu, enter:1

When prompted for functions of x, paste:sin(x), cos(x), x**2, jv(0, x)

Expected:

Blue sine wave and red cosine wave with natural amplitude (not flattened).
Green parabola with correct curvature.
Purple Bessel function plotted correctly.
Legend shows:sin(x)
cos(x)
x²
jv(0, x)

(Note: x**2 is now x² in legend.)

Test 2 — 3D Plotting (Scaling, Legends, Colors)
Steps:

Run the program again.
At the menu, enter:2

When prompted for functions of x and y, paste:sin(sqrt(x**2 + y**2)) / sqrt(x**2 + y**2), cos(x) * sin(y), jv(0, sqrt(x**2 + y**2))

Expected:

Multiple colored surfaces, each with unique color from the color cycle.
Wireframe overlay for clarity.
Legend shows superscript formatting:sin(√(x² + y²)) / √(x² + y²)
cos(x) * sin(y)
jv(0, √(x² + y²))

Z-axis auto-scaled so surfaces aren’t squashed.

Test 3 — Unlimited Color Cycling
Steps:

Choose 2D mode.
Enter more than 20 functions:sin(x), cos(x), tan(x), x**2, x**3, x**4, exp(x), exp(-x), sqrt(abs(x)), log(abs(x)+1), sinh(x), cosh(x), tanh(x), sech(x), csch(x), coth(x), jv(0, x), jv(1, x), jv(2, x), jv(3, x), jv(4, x)

Expected:

All functions plotted with distinct colors (no obvious repeats).
Legends formatted with superscripts for powers.

Test 4 — Keyboard Controls in 3D
Steps:

Choose 3D mode.
Enter:cos(x) * sin(y)

While the plot window is active:

Arrow keys → Rotate view.
+ → Zoom in.
- → Zoom out.
Home → Reset view to default (elev=30°, azim=45°).

Test 5 — Error Handling
Steps:

Choose 2D mode.
Enter:sin(x), badfunc(x)

Expected:

sin(x) plots normally.
Error message for badfunc(x) appears in terminal.
Program continues without crashing.

Extra Functions You Can Try
You can use NumPy, math, and SciPy special functions:
exp(-x**2)
sqrt(abs(x))
tanh(x)
sech(x)
csch(x)
coth(x)
jv(1, x)

For 3D:
sqrt(x**2 + y**2)
sin(x) * cos(y)
exp(-(x**2 + y**2) / 10)

If you want, I can also give you a bonus “stress test” dataset that pushes the program with 50+ functions to prove the color cycling and autoscaling work even under heavy load.
Do you want me to prepare that stress test?

#Stress Test With Explanations For Updates To The Second Half
Got it ✅ —
We’ll fix two things before giving you the stress test dataset:

Menu wording — change "Plot" → "Graph" for both 2D and 3D options.
Superscript formatting in 3D legends — the issue is that in plot_3d() we were calling next(colors) twice (once for surface, once for legend patch), which meant the legend color didn’t match and the expression formatting wasn’t applied correctly. We’ll fix it so the same color and formatted expression are used for both surface and legend.

Fix for 3D Legend Formatting
In plot_3d() replace:
Pythoncol = next(colors)
ax.plot_surface(X, Y, Z, color=col, alpha=0.7, edgecolor='none', rstride=1, cstride=1)
ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.2, alpha=0.15)
legend_patches.append(Patch(color=col, label=format_expr(expr)))

✅ This ensures:

One color per function (no mismatch).
Superscript formatting applied to legend labels.

Updated Menu
Replace main() with:
Pythondef main():
    while True:
        print("\n--- Multiple Function Graphing Software ---")
        print("1. Graph 2D functions")
        print("2. Graph 3D functions")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            plot_2d()
        elif choice == '2':
            plot_3d()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

Stress Test Dataset
This will push color cycling and autoscaling to the limit.

2D Stress Test
sin(x), cos(x), tan(x), x**2, x**3, x**4, exp(x), exp(-x), sqrt(abs(x)), log(abs(x)+1), sinh(x), cosh(x), tanh(x), sech(x), csch(x), coth(x), jv(0, x), jv(1, x), jv(2, x), jv(3, x), jv(4, x), jv(5, x), jv(6, x), jv(7, x), jv(8, x), jv(9, x), jv(10, x), exp(-x**2), sin(x)/x, cos(x)/x, tanh(x)/x, sinh(x)/x, cosh(x)/x, sech(x)/x, csch(x)/x, coth(x)/x, sqrt(x**2+1), log(x**2+1), exp(-abs(x)), sin(x**2), cos(x**2), tan(x**2), exp(sin(x)), exp(cos(x)), exp(tan(x)), sin(exp(x)), cos(exp(x)), tan(exp(x))

3D Stress Test
sin(sqrt(x**2 + y**2)) / sqrt(x**2 + y**2), cos(x) * sin(y), jv(0, sqrt(x**2 + y**2)), jv(1, sqrt(x**2 + y**2)), jv(2, sqrt(x**2 + y**2)), exp(-(x**2 + y**2) / 10), sqrt(x**2 + y**2), sin(x) * cos(y), tan(x*y), exp(-abs(x*y)), sin(x**2 + y**2), cos(x**2 + y**2), tan(x**2 + y**2), exp(sin(x*y)), exp(cos(x*y)), exp(tan(x*y)), sin(exp(x*y)), cos(exp(x*y)), tan(exp(x*y)), sinh(x*y), cosh(x*y), tanh(x*y), sech(x*y), csch(x*y), coth(x*y)

Expected Results

2D: All curves visible, distinct colors, legends with superscripts for powers.
3D: All surfaces distinct colors, legends with superscripts, wireframe overlay, keyboard controls working.

If you want, I can now send you the fixed Part 3 and Part 4 so your 3D legends are correct and menu wording is updated — then you can run the stress test immediately.
Do you want me to send those updated parts?

Got it ✅ —
The flattened 2D graphing issue is because plt.autoscale(enable=True, axis='y') alone doesn’t always trigger proper scaling when multiple functions have vastly different ranges.
We’ll fix this by manually computing min/max Y values across all functions and setting plt.ylim() accordingly. This guarantees curves aren’t squashed.
We’ll also send the updated Part 3 (3D legend fix) and Part 4 (menu wording change) so everything is ready for your stress test.

With these fixes:

2D graphs will no longer be flattened — manual autoscaling ensures proper Y limits.
3D legends will now show superscripts correctly and match surface colors.
Menu wording now says "Graph" instead of "Plot".

If you run the stress test dataset now, you should see:

Distinct colors for all functions.
Correct scaling in 2D.
Superscript legends in both 2D and 3D.
'''
# =========================
# Part 1 — Imports & Helpers
# =========================
import numpy as np
import math
from scipy.special import jv
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import tkinter as tk
from tkinter import messagebox

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

# Allowed functions for safe eval
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
    import re
    expr = re.sub(r"x\*\*([0-9+\-]+)", lambda m: "x" + ''.join(SUPERSCRIPTS.get(ch, ch) for ch in m.group(1)), expr)
    expr = re.sub(r"([0-9+\-]+)\*\*x", lambda m: ''.join(SUPERSCRIPTS.get(ch, ch) for ch in m.group(1)) + "x", expr)
    return expr

# Parse function safely
def parse_function(expr, dims=2):
    try:
        if dims == 2:
            return eval(f"lambda x: {expr}", SAFE_FUNCS)
        elif dims == 3:
            return eval(f"lambda x, y: {expr}", SAFE_FUNCS)
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
        for i in range(cmap.N):
            yield cmap(i / (cmap.N - 1))
        idx += 1

# Safe call wrapper
def safe_call(func, *args):
    try:
        result = func(*args)
        result = np.nan_to_num(result, nan=np.nan, posinf=np.nan, neginf=np.nan)
        return result
    except Exception:
        return np.full_like(args[0], np.nan)

# Show invalid functions message
def show_invalid_functions_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Invalid Functions", INVALID_FUNCTIONS_MESSAGE)
    root.destroy()

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

    if not funcs:
        print("No valid functions entered.")
        return

    x_vals = np.linspace(-10, 10, 500)
    plt.figure(figsize=(10, 6))
    colors = color_cycle()

    all_y_vals = []
    MAX_Y = 1e3

    for func, expr in zip(funcs, valid_exprs):
        try:
            y_vals = safe_call(func, x_vals)
            mask = ~np.isnan(y_vals)
            if np.sum(mask) < 5:
                print(f"Skipping '{expr}' — too few valid points.")
                continue
            y_vals = np.clip(y_vals, -MAX_Y, MAX_Y)
            all_y_vals.extend(y_vals[mask])
            plt.plot(x_vals[mask], y_vals[mask], color=next(colors), label=format_expr(expr))
        except Exception as e:
            print(f"Error evaluating '{expr}': {e}")

    if all_y_vals:
        y_min, y_max = min(all_y_vals), max(all_y_vals)
        plt.ylim(y_min - abs(y_min)*0.)

    if all_y_vals:
        y_min, y_max = min(all_y_vals), max(all_y_vals)
        plt.ylim(y_min - abs(y_min)*0.1, y_max + abs(y_max)*0.1)

    plt.title("2D Multiple Function Graphing Software")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

    if all_y_vals:
        y_min, y_max = min(all_y_vals), max(all_y_vals)
        plt.ylim(y_min - abs(y_min)*0.1, y_max + abs(y_max)*0.1)

    plt.title("2D Multiple Function Graphing Software")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()



