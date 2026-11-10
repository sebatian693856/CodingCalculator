'''
Section 3 — Imports & Safe Function Setup
Section 1 — Safe Function Parser
Section 2 — Complex to RGB Mapping
Section 4 — Plot Functions
Section 5 — Calabi–Yau Manifold Graphing with Conformal Mapping
Section 6 — Riemann Sphere Graphing with Conformal Mapping
Section 7 — Enhanced Marching Cubes (For 3D Surfaces & Solids)
Section 8 — Interactive Rotation & Zoom for 3D Surfaces & Solids
Section 9 — Menu
Section 10 — Final Entry Point

def plot_2d(expr, x_min=-10, x_max=10, resolution=1000):
    """Plots a single 2D function."""
    import numpy as np
    import matplotlib.pyplot as plt
    safe_globals = {"__builtins__": None, "np": np}
    x = np.linspace(x_min, x_max, resolution)
    try:
        y = eval(expr, safe_globals, {"x": x})
    except Exception as e:
        print(f"Error plotting 2D function: {e}")
        return
    plt.plot(x, y)
    plt.title(f"2D Plot: {expr}")
    plt.show()

def plot_2d_multi(expr_list, x_min=-10, x_max=10, resolution=1000):
    """Plots multiple 2D functions on the same axes."""
    import numpy as np
    import matplotlib.pyplot as plt
    safe_globals = {"__builtins__": None, "np": np}
    x = np.linspace(x_min, x_max, resolution)
    for expr in expr_list:
        try:
            y = eval(expr, safe_globals, {"x": x})
            plt.plot(x, y, label=expr)
        except Exception as e:
            print(f"Error plotting {expr}: {e}")
    plt.legend()
    plt.title("Multi-function 2D Plot")
    plt.show()

def plot_calabi_yau_3d(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """Plots a Calabi–Yau slice using Marching Cubes."""
    import numpy as np, math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    z1_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z2_vals = np.linspace(bounds[0], bounds[1], grid_size)
    Z1, Z2 = np.meshgrid(z1_vals, z2_vals)
    try:
        values = eval(expr, safe_globals, {"z1": Z1, "z2": Z2})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    spacing = (z1_vals[1] - z1_vals[0], z2_vals[1] - z2_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(np.abs(values), level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"Calabi–Yau Slice: {expr}")
    plt.show()

def plot_riemann_sphere(expr):
    """Plots a function mapped onto a Riemann sphere."""
    import numpy as np
    import matplotlib.pyplot as plt
    safe_globals = {"__builtins__": None, "np": np}
    theta = np.linspace(0, np.pi, 200)
    phi = np.linspace(0, 2*np.pi, 200)
    THETA, PHI = np.meshgrid(theta, phi)
    X = np.sin(THETA) * np.cos(PHI)
    Y = np.sin(THETA) * np.sin(PHI)
    Z = np.cos(THETA)
    try:
        values = eval(expr, safe_globals, {"x": X})
    except Exception as e:
        print(f"Error plotting Riemann sphere: {e}")
        return
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(values))
    ax.set_title(f"Riemann Sphere Mapping: {expr}")
    plt.show()

def plot_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """Plots a basic 3D solid using Marching Cubes."""
    import numpy as np, math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
    try:
        values = eval(expr, safe_globals, {"x": X, "y": Y, "z": Z})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(np.abs(values), level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"3D Solid: {expr}")
    plt.show()

def interactive_3d_plot(expr, mode="solid", **kwargs):
    """Interactive plot for solid or sphere."""
    if mode == "solid":
        plot_3d_solid(expr, **kwargs)
    elif mode == "sphere":
        plot_riemann_sphere(expr)
    else:
        print("Invalid mode for interactive 3D plot.")

def plot_complex_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """Plots a complex-valued 3D solid."""
    import numpy as np, math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
    try:
        values = eval(expr, safe_globals, {"x": X, "y":

def plot_2d(expr, x_min=-10, x_max=10, resolution=1000):
    """
    Plots a single 2D function using matplotlib.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    safe_globals = {"__builtins__": None, "np": np}
    x = np.linspace(x_min, x_max, resolution)
    try:
        y = eval(expr, safe_globals, {"x": x})
    except Exception as e:
        print(f"Error plotting 2D function: {e}")
        return
    plt.plot(x, y)
    plt.title(f"2D Plot: {expr}")
    plt.show()

def plot_2d_multi(expr_list, x_min=-10, x_max=10, resolution=1000):
    """
    Plots multiple 2D functions on the same axes.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    safe_globals = {"__builtins__": None, "np": np}
    x = np.linspace(x_min, x_max, resolution)
    for expr in expr_list:
        try:
            y = eval(expr, safe_globals, {"x": x})
            plt.plot(x, y, label=expr)
        except Exception as e:
            print(f"Error plotting {expr}: {e}")
    plt.legend()
    plt.title("Multi-function 2D Plot")
    plt.show()

    def plot_calabi_yau_3d(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """
    Plots a Calabi–Yau slice using Marching Cubes.
    """
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    z1_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z2_vals = np.linspace(bounds[0], bounds[1], grid_size)
    Z1, Z2 = np.meshgrid(z1_vals, z2_vals)
    try:
        values = eval(expr, safe_globals, {"z1": Z1, "z2": Z2})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    spacing = (z1_vals[1] - z1_vals[0], z2_vals[1] - z2_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(np.abs(values), level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"Calabi–Yau Slice: {expr}")
    plt.show()

    def plot_riemann_sphere(expr):
    """
    Plots a function mapped onto a Riemann sphere.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    safe_globals = {"__builtins__": None, "np": np}
    theta = np.linspace(0, np.pi, 200)
    phi = np.linspace(0, 2*np.pi, 200)
    THETA, PHI = np.meshgrid(theta, phi)
    X = np.sin(THETA) * np.cos(PHI)
    Y = np.sin(THETA) * np.sin(PHI)
    Z = np.cos(THETA)
    try:
        values = eval(expr, safe_globals, {"x": X})
    except Exception as e:
        print(f"Error plotting Riemann sphere: {e}")
        return
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(values))
    ax.set_title(f"Riemann Sphere Mapping: {expr}")
    plt.show()

def plot_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """
    Plots a basic 3D solid using Marching Cubes.
    """
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
    try:
        values = eval(expr, safe_globals, {"x": X, "y": Y, "z": Z})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(np.abs(values), level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"3D Solid: {expr}")
    plt.show()

def interactive_3d_plot(expr, mode="solid", **kwargs):
    """
    Interactive plot for solid or sphere.
    """
    if mode == "solid":
        plot_3d_solid(expr, **kwargs)
    elif mode == "sphere":
        plot_riemann_sphere(expr)
    else:
        print("Invalid mode for interactive 3D plot.")

def plot_complex_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """
    Plots a complex-valued 3D solid using Marching Cubes.
    The magnitude of the complex value is used for surface extraction.
    """
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals

    """
    Total Programme Test Script

    def plot_complex_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """
    Plots a complex-valued 3D solid using Marching Cubes.
    The magnitude of the complex value is used for surface extraction.
    """
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    from skimage import measure
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals

    """
Test script for full plotting menu functions.
Runs each plotting function with a simple example expression.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import measure

# ---------------------------
# Plotting Functions
# ---------------------------

def plot_2d(expr, x_min=-10, x_max=10, resolution=1000):
    """Plots a single 2D function using matplotlib."""
    safe_globals = {"__builtins__": None, "np": np}
    x_vals = np.linspace(x_min, x_max, resolution)
    try:
        y_vals = eval(expr, safe_globals, {"x": x_vals})
    except Exception as e:
        print(f"Error plotting 2D function: {e}")
        return
    plt.plot(x_vals, y_vals)
    plt.title(f"2D Plot: {expr}")
    plt.show()

def plot_2d_multi(expr_list, x_min=-10, x_max=10, resolution=1000):
    """Plots multiple 2D functions on the same axes."""
    safe_globals = {"__builtins__": None, "np": np}
    x_vals = np.linspace(x_min, x_max, resolution)
    for expr in expr_list:
        try:
            y_vals = eval(expr, safe_globals, {"x": x_vals})
            plt.plot(x_vals, y_vals, label=expr)
        except Exception as e:
            print(f"Error plotting {expr}: {e}")
    plt.legend()
    plt.title("Multi-function 2D Plot")
    plt.show()

def plot_calabi_yau_3d(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """Plots a Calabi–Yau slice using Marching Cubes."""
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    z1_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z2_vals = np.linspace(bounds[0], bounds[1], grid_size)
    Z1, Z2 = np.meshgrid(z1_vals, z2_vals)
    try:
        values = eval(expr, safe_globals, {"z1": Z1, "z2": Z2})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    spacing = (z1_vals[1] - z1_vals[0], z2_vals[1] - z2_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(np.abs(values), level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"Calabi–Yau Slice: {expr}")
    plt.show()

def plot_riemann_sphere(expr):
    """Plots a function mapped onto a Riemann sphere."""
    safe_globals = {"__builtins__": None, "np": np}
    theta = np.linspace(0, np.pi, 200)
    phi = np.linspace(0, 2*np.pi, 200)
    THETA, PHI = np.meshgrid(theta, phi)
    X = np.sin(THETA) * np.cos(PHI)
    Y = np.sin(THETA) * np.sin(PHI)
    Z = np.cos(THETA)
    try:
        values = eval(expr, safe_globals, {"x": X})
    except Exception as e:
        print(f"Error plotting Riemann sphere: {e}")
        return
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(values))
    ax.set_title(f"Riemann Sphere Mapping: {expr}")
    plt.show()

def plot_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """Plots a basic 3D solid using Marching Cubes."""
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
    try:
        values = eval(expr, safe_globals, {"x": X, "y": Y, "z": Z})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(np.abs(values), level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"3D Solid: {expr}")
    plt.show()

def plot_complex_3d_solid(expr, grid_size=50, bounds=(-2, 2), isovalue=0):
    """Plots a complex-valued 3D solid using Marching Cubes."""
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
    try:
        values = eval(expr, safe_globals, {"x": X, "y": Y, "z": Z})
    except Exception as e:
        print(f"Error parsing complex 3D solid function: {e}")
        return
    magnitude = np.abs(values)
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])
    verts, faces, normals, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"Complex 3D Solid:
'''

# =========================
# Section 1 — Imports & Safe Function Setup
# =========================

import math
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

# Safe globals for eval() — prevents arbitrary code execution
SAFE_GLOBALS = {
    "__builtins__": None,
    "np": np,
    "math": math,
    # Vectorized math functions for NumPy arrays
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "exp": np.exp, "sqrt": np.sqrt,
    "log": np.log, "abs": np.abs
}

# =========================
# Section 2 — Safe Function Parser
# =========================

def safe_eval(expr: str, variables: dict):
    """
    Safely evaluates a mathematical expression using restricted globals.
    
    Parameters:
        expr (str): The mathematical expression to evaluate.
        variables (dict): Dictionary of variable names and their NumPy arrays/scalars.
    
    Returns:
        result (np.ndarray or float): The evaluated result.
    
    Raises:
        ValueError: If the expression cannot be evaluated safely.
    """
    try:
        return eval(expr, SAFE_GLOBALS, variables)
    except Exception as e:
        raise ValueError(f"Error evaluating expression '{expr}': {e}")

# =========================
# Section 3 — Complex to RGB Mapping
# =========================

def complex_to_rgb(Z: np.ndarray) -> np.ndarray:
    """
    Converts a complex-valued NumPy array into RGB colors.
    
    Parameters:
        Z (np.ndarray): Complex-valued array.
    
    Returns:
        rgb (np.ndarray): Array of shape (H, W, 3) with RGB values in [0, 1].
    """
    # Phase → Hue (0 to 1)
    phase = (np.angle(Z) + np.pi) / (2 * np.pi)
    
    # Magnitude → Saturation/Brightness
    magnitude = np.abs(Z)
    magnitude_norm = magnitude / (np.max(magnitude) + 1e-9)  # Avoid division by zero
    
    # HSV to RGB conversion
    rgb = np.zeros(Z.shape + (3,), dtype=float)
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            h = phase[i, j]
            s = 1.0
            v = magnitude_norm[i, j]
            rgb[i, j] = hsv_to_rgb(h, s, v)
    
    return rgb


def hsv_to_rgb(h: float, s: float, v: float) -> tuple:
    """
    Converts HSV color to RGB.
    
    Parameters:
        h (float): Hue in [0, 1]
        s (float): Saturation in [0, 1]
        v (float): Value/Brightness in [0, 1]
    
    Returns:
        (r, g, b) tuple in [0, 1]
    """
    if s == 0.0:
        return (v, v, v)
    
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i %= 6
    
    if i == 0:
        return (v, t, p)
    elif i == 1:
        return (q, v, p)
    elif i == 2:
        return (p, v, t)
    elif i == 3:
        return (p, q, v)
    elif i == 4:
        return (t, p, v)
    elif i == 5:
        return (v, p, q)

# =========================
# Section 4 — Plot Functions
# =========================

def plot_2d_function(expr: str, x_min: float = -10.0, x_max: float = 10.0, resolution: int = 500):
    """
    Plots a 2D function y = f(x).
    """
    x_vals = np.linspace(x_min, x_max, resolution)
    try:
        y_vals = safe_eval(expr, {"x": x_vals})
    except ValueError as e:
        print(e)
        return
    
    plt.figure()
    plt.plot(x_vals, y_vals, label=expr)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"2D Plot: {expr}")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_complex_map(expr: str, bounds: tuple[float, float] = (-2.0, 2.0), resolution: int = 500):
    """
    Plots a complex-valued function as a color map.
    """
    re_vals = np.linspace(bounds[0], bounds[1], resolution)
    im_vals = np.linspace(bounds[0], bounds[1], resolution)
    RE, IM = np.meshgrid(re_vals, im_vals)
    Z = RE + 1j * IM
    
    try:
        W = safe_eval(expr, {"z": Z})
    except ValueError as e:
        print(e)
        return
    
    rgb_image = complex_to_rgb(W)
    plt.figure()
    plt.imshow(rgb_image, extent=(bounds[0], bounds[1], bounds[0], bounds[1]))
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.title(f"Complex Map: {expr}")
    plt.show()


def plot_trisurf_example(verts: np.ndarray, faces: np.ndarray):
    """
    Plots a triangulated surface from Marching Cubes output.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                    cmap='viridis', lw=1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

# =========================
# Section 5 — Calabi–Yau Manifold Graphing with Conformal Mapping
# =========================

def plot_calabi_yau(expr: str, grid_size: int = 50,
                    bounds: tuple[float, float] = (-2.0, 2.0),
                    isovalue: float = 0.0):
    """
    Plots a Calabi–Yau slice using Marching Cubes and complex color mapping.
    
    Parameters:
        expr (str): Function in terms of z1, z2, z3 (complex variables allowed).
        grid_size (int): Resolution of the grid.
        bounds (tuple): Min/max for each axis.
        isovalue (float): Surface level to extract.
    """
    # Create 3D grid
    z1_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z2_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z3_vals = np.linspace(bounds[0], bounds[1], grid_size)
    Z1, Z2, Z3 = np.meshgrid(z1_vals, z2_vals, z3_vals)

    # Evaluate expression safely
    try:
        values = safe_eval(expr, {"z1": Z1, "z2": Z2, "z3": Z3})
    except ValueError as e:
        print(e)
        return

    # Prepare for Marching Cubes
    magnitude = np.abs(values)
    spacing = (
        z1_vals[1] - z1_vals[0],
        z2_vals[1] - z2_vals[0],
        z3_vals[1] - z3_vals[0]
    )

    try:
        verts, faces, _, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
    except Exception as e:
        print(f"Marching Cubes failed: {e}")
        return

    # Color mapping based on complex values
    colors = complex_to_rgb(values.reshape(-1))  # Flatten for vertex coloring

    # Plot surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                    facecolors=colors[:len(verts)], lw=0.5)
    ax.set_xlabel("Z1")
    ax.set_ylabel("Z2")
    ax.set_zlabel("Z3")
    ax.set_title(f"Calabi–Yau Slice: {expr}")
    plt.show()

# =========================
# Section 6 — Riemann Sphere Graphing with Conformal Mapping
# =========================

def plot_riemann_sphere(expr: str, grid_size: int = 200,
                        bounds: tuple[float, float] = (-2.0, 2.0)):
    """
    Plots a complex function on the Riemann sphere using stereographic projection.
    
    Parameters:
        expr (str): Complex function in terms of z.
        grid_size (int): Resolution of the complex plane grid.
        bounds (tuple): Min/max for real and imaginary parts.
    """
    # Create complex grid
    re_vals = np.linspace(bounds[0], bounds[1], grid_size)
    im_vals = np.linspace(bounds[0], bounds[1], grid_size)
    RE, IM = np.meshgrid(re_vals, im_vals)
    Z_complex = RE + 1j * IM

    # Evaluate complex function safely
    try:
        W = safe_eval(expr, {"z": Z_complex})
    except ValueError as e:
        print(e)
        return

    # Stereographic projection
    abs_w_sq = np.abs(W)**2
    X = 2 * np.real(W) / (abs_w_sq + 1)
    Y = 2 * np.imag(W) / (abs_w_sq + 1)
    Z = (abs_w_sq - 1) / (abs_w_sq + 1)

    # Color mapping
    colors = complex_to_rgb(W)

    # Plot sphere
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Riemann Sphere Mapping: {expr}")
    plt.show()

# =========================
# Section 7 — Enhanced Marching Cubes (For 3D Surfaces & Solids)
# =========================

def plot_3d_solid(expr: str, grid_size: int = 50,
                  bounds: tuple[float, float] = (-2.0, 2.0),
                  isovalue: float = 0.0,
                  color_by_complex: bool = False):
    """
    Plots a 3D surface/solid using Marching Cubes.
    
    Parameters:
        expr (str): Function in terms of x, y, z (can be complex if color_by_complex=True).
        grid_size (int): Resolution of the grid.
        bounds (tuple): Min/max for each axis.
        isovalue (float): Surface level to extract.
        color_by_complex (bool): If True, color vertices using complex-to-RGB mapping.
    """
    # Create 3D grid
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)

    # Evaluate expression safely
    try:
        values = safe_eval(expr, {"x": X, "y": Y, "z": Z})
    except ValueError as e:
        print(e)
        return

    # Prepare magnitude for Marching Cubes
    magnitude = np.abs(values) if np.iscomplexobj(values) else values
    spacing = (
        x_vals[1] - x_vals[0],
        y_vals[1] - y_vals[0],
        z_vals[1] - z_vals[0]
    )

    try:
        verts, faces, _, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
    except Exception as e:
        print(f"Marching Cubes failed: {e}")
        return

    # Optional coloring
    if color_by_complex and np.iscomplexobj(values):
        colors = complex_to_rgb(values.reshape(-1))
    else:
        colors = None

    # Plot surface
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if colors is not None:
        ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                        facecolors=colors[:len(verts)], lw=0.5)
    else:
        ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                        cmap='viridis', lw=0.5)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"3D Solid: {expr}")
    plt.show()

# =========================
# Section 8 — Interactive Rotation & Zoom for 3D Surfaces & Solids
# =========================

def interactive_3d_plot(verts: np.ndarray, faces: np.ndarray,
                        colors: np.ndarray = None,
                        title: str = "Interactive 3D Plot"):
    """
    Displays an interactive 3D plot with rotation and zoom enabled.
    
    Parameters:
        verts (np.ndarray): Vertex coordinates from Marching Cubes.
        faces (np.ndarray): Face indices from Marching Cubes.
        colors (np.ndarray): Optional RGB colors for vertices.
        title (str): Plot title.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot surface with optional colors
    if colors is not None:
        ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                        facecolors=colors[:len(verts)], lw=0.5)
    else:
        ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                        cmap='viridis', lw=0.5)

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Enable interactive rotation and zoom
    plt.ion()  # Interactive mode
    plt.show()

    print("\n💡 Controls:")
    print(" - Left mouse button: Rotate")
    print(" - Right mouse button or scroll: Zoom")
    print(" - Middle mouse button: Pan")

# =========================
# Section 9 — Complex 3D Surface Graphing
# =========================

def plot_complex_3d_surface(expr: str = "np.sin(x) + 1j*np.cos(y)",
                            grid_size: int = 50,
                            bounds: tuple[float, float] = (-5.0, 5.0)):
    """
    Plots a complex-valued 3D surface using Marching Cubes and complex-to-RGB coloring.
    """
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)

    try:
        values = safe_eval(expr, {"x": X, "y": Y, "z": Z})
    except ValueError as e:
        print(e)
        return

    magnitude = np.abs(values)
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])

    verts, faces, _, _ = measure.marching_cubes(magnitude, level=0.5, spacing=spacing)
    colors = complex_to_rgb(values.reshape(-1))

    interactive_3d_plot(verts, faces, colors, title=f"Complex 3D Surface: {expr}")

# =========================
# Section 10 — Complex 3D Solid Graphing
# =========================

def plot_complex_3d_solid(expr: str = "x**2 + y**2 + z**2 - 4 + 1j*(x*y*z)",
                          grid_size: int = 40,
                          bounds: tuple[float, float] = (-3.0, 3.0)):
    """
    Plots a complex-valued 3D solid using Marching Cubes and complex-to-RGB coloring.
    """
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)

    try:
        values = safe_eval(expr, {"x": X, "y": Y, "z": Z})
    except ValueError as e:
        print(e)
        return

    magnitude = np.abs(values)
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])

    verts, faces, _, _ = measure.marching_cubes(magnitude, level=4.0, spacing=spacing)
    colors = complex_to_rgb(values.reshape(-1))

    interactive_3d_plot(verts, faces, colors, title=f"Complex 3D Solid: {expr}")

# =========================
# Section 11 — Complex Manifold Graphing
# =========================

def plot_complex_manifold(expr: str = "z1**2 + z2**2 - 1",
                          grid_size: int = 30,
                          bounds: tuple[float, float] = (-2.0, 2.0)):
    """
    Plots a complex manifold defined by a function in terms of z1, z2.
    """
    z1_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z2_vals = np.linspace(bounds[0], bounds[1], grid_size)
    Z1, Z2 = np.meshgrid(z1_vals, z2_vals)

    try:
        values = safe_eval(expr, {"z1": Z1, "z2": Z2})
    except ValueError as e:
        print(e)
        return

    rgb_image = complex_to_rgb(values)
    plt.imshow(rgb_image, extent=(bounds[0], bounds[1], bounds[0], bounds[1]))
    plt.xlabel("Re(z1)")
    plt.ylabel("Re(z2)")
    plt.title(f"Complex Manifold: {expr}")
    plt.show()

# =========================
# Section 12 — Riemannian Manifold Graphing
# =========================

def plot_riemannian_manifold(expr: str = "np.sin(x) * np.cos(y)",
                             grid_size: int = 50,
                             bounds: tuple[float, float] = (-5.0, 5.0)):
    """
    Plots a Riemannian manifold surface from a scalar function.
    """
    x_vals = np.linspace(bounds[0], bounds[1], grid_size)
    y_vals = np.linspace(bounds[0], bounds[1], grid_size)
    X, Y = np.meshgrid(x_vals, y_vals)

    try:
        Z = safe_eval(expr, {"x": X, "y": Y})
    except ValueError as e:
        print(e)
        return

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(f"Riemannian Manifold: {expr}")
    plt.show()

# =========================
# Section 13 — Symplectic Manifold Graphing
# =========================

def plot_symplectic_manifold(expr: str = "np.sin(p) + np.cos(q)",
                             grid_size: int = 50,
                             bounds: tuple[float, float] = (-5.0, 5.0)):
    """
    Plots a symplectic manifold from a function in terms of p, q (canonical coordinates).
    """
    p_vals = np.linspace(bounds[0], bounds[1], grid_size)
    q_vals = np.linspace(bounds[0], bounds[1], grid_size)
    P, Q = np.meshgrid(p_vals, q_vals)

    try:
        Z = safe_eval(expr, {"p": P, "q": Q})
    except ValueError as e:
        print(e)
        return

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(P, Q, Z, cmap='plasma')
    ax.set_title(f"Symplectic Manifold: {expr}")
    plt.show()


# =========================
# Section 14 — Menu
# =========================

def main_menu():
    """
    Updated menu: each option runs with a default example function.
    """
    while True:
        print("\n=== Function Plotting Menu ===")
        print("1. Plot 2D Function y=f(x)")
        print("2. Plot Complex Map f(z)")
        print("3. Plot Calabi–Yau Slice")
        print("4. Plot Riemann Sphere Mapping")
        print("5. Plot 3D Solid/Surface")
        print("6. Complex 3D Surface Graphing")
        print("7. Complex 3D Solid Graphing")
        print("8. Complex Manifold Graphing")
        print("9. Riemannian Manifold Graphing")
        print("10. Symplectic Manifold Graphing")
        print("11. Exit")
        print("12. Run All Default Examples")

        choice = input("Enter choice (1-12): ").strip()

        if choice == "1":
            expr = input("Enter function in terms of x (default: 0.5*x + 3): ").strip() or "0.5*x + 3"
            plot_2d_function(expr)

        elif choice == "2":
            expr = input("Enter complex function in terms of z (default: math.sin(z)): ").strip() or "math.sin(z)"
            plot_complex_map(expr)

        elif choice == "3":
            expr = input("Enter Calabi–Yau function (default: z1**2 + z2**2 + z3**2 - 1): ").strip() or "z1**2 + z2**2 + z3**2 - 1"
            plot_calabi_yau(expr)

        elif choice == "4":
            expr = input("Enter complex function in terms of z (default: z**2): ").strip() or "z**2"
            plot_riemann_sphere(expr)

        elif choice == "5":
            expr = input("Enter function in terms of x, y, z (default: x**2 + y**2 + z**2 - 4): ").strip() or "x**2 + y**2 + z**2 - 4"
            color_choice = input("Color by complex mapping? (y/n, default: n): ").strip().lower() or "n"
            plot_3d_solid(expr, color_by_complex=(color_choice == "y"))

        elif choice == "6":
            expr = input("Enter complex 3D surface function (default: np.sin(x) + 1j*np.cos(y)): ").strip() or "np.sin(x) + 1j*np.cos(y)"
            plot_complex_3d_surface(expr)

        elif choice == "7":
            expr = input("Enter complex 3D solid function (default: x**2 + y**2 + z**2 - 4 + 1j*(x*y*z)): ").strip() or "x**2 + y**2 + z**2 - 4 + 1j*(x*y*z)"
            plot_complex_3d_solid(expr)

        elif choice == "8":
            expr = input("Enter complex manifold function (default: z1**2 + z2**2 - 1): ").strip() or "z1**2 + z2**2 - 1"
            plot_complex_manifold(expr)

        elif choice == "9":
            expr = input("Enter Riemannian manifold function (default: np.sin(x) * np.cos(y)): ").strip() or "np.sin(x) * np.cos(y)"
            plot_riemannian_manifold(expr)

        elif choice == "10":
            expr = input("Enter symplectic manifold function (default: np.sin(p) + np.cos(q)): ").strip() or "np.sin(p) + np.cos(q"
            plot_symplectic_manifold(expr)

        elif choice == "11":
            print("Exiting programme.")
            break

        elif choice == "12":
            print("\nRunning all default examples...")
            plot_2d_function("0.5*x + 3")
            plot_complex_map("math.sin(z)")
            plot_calabi_yau("z1**2 + z2**2 + z3**2 - 1")
            plot_riemann_sphere("z**2")
            plot_3d_solid("x**2 + y**2 + z**2 - 4", color_by_complex=False)
            plot_complex_3d_surface("np.sin(x) + 1j*np.cos(y)")
            plot_complex_3d_solid("x**2 + y**2 + z**2 - 4 + 1j*(x*y*z)")
            plot_complex_manifold("z1**2 + z2**2 - 1")
            plot_riemannian_manifold("np.sin(x) * np.cos(y)")
            plot_symplectic_manifold("np.sin(p) + np.cos(q)")
            print("\n✅ All default examples completed.")

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

# =========================
# Section 15 — Programme Entry Point
# =========================

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import measure

    # Ensure all sections are loaded before running
    print("📊 Advanced Function Plotting System Loaded")
    print("Modules: Safe Eval, Complex Mapping, Plot Functions, Calabi–Yau, Riemann Sphere, Marching Cubes, Interactive 3D, Menu")

    # Start menu
    main_menu()
