'''
Section 3 — Imports & Safe Function Setup
Section 1 — Safe Function Parser
Section 2 — Complex to RGB Mapping
Section 4 — Plot Functions
Section 5 — Calabi–Yau Manifold Graphing with Conformal Mapping
Section 6 — Riemann Sphere Graphing with Conformal Mapping
Section 7 — Enhanced Marching Cubes
Section 8 — Interactive Rotation & Zoom for 3D Surfaces & Solids
Section 9 — Updated Menu
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
# Imports
# =========================
import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import measure

# =========================
# Option 1: Plot 2D function(s)
# =========================
def plot_2d(expr: str, x_min: float = -10.0, x_max: float = 10.0, resolution: int = 1000) -> None:
    """Plots a single 2D function using matplotlib."""
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(x_min, x_max, resolution)
    try:
        y_vals = eval(expr, safe_globals, {"x": x_vals})
    except Exception as e:
        print(f"Error plotting 2D function: {e}")
        return
    plt.plot(x_vals, y_vals)
    plt.title(f"2D Plot: {expr}")
    plt.show()

def plot_2d_multi(expr_list: list[str], x_min: float = -10.0, x_max: float = 10.0, resolution: int = 1000) -> None:
    """Plots multiple 2D functions on the same axes."""
    safe_globals = {"__builtins__": None, "np": np, "math": math}
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

# =========================
# Option 2: Calabi–Yau 3D slice (with auto isovalue fix)
# =========================
def plot_calabi_yau_3d(expr: str, grid_size: int = 50, bounds: tuple[float, float] = (-2.0, 2.0), isovalue: float = 0.0) -> None:
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    z1_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z2_vals = np.linspace(bounds[0], bounds[1], grid_size)
    z3_vals = np.linspace(bounds[0], bounds[1], grid_size)
    Z1, Z2, Z3 = np.meshgrid(z1_vals, z2_vals, z3_vals)
    try:
        values = eval(expr, safe_globals, {"z1": Z1, "z2": Z2, "z3": Z3})
    except Exception as e:
        print(f"Error parsing function: {e}")
        return
    magnitude = np.abs(values)
    min_val, max_val = magnitude.min(), magnitude.max()
    if not (min_val <= isovalue <= max_val):
        print(f"⚠️ Adjusting isovalue from {isovalue} to midpoint of range ({min_val:.3f}, {max_val:.3f})")
        isovalue = (min_val + max_val) / 2
    spacing = (z1_vals[1] - z1_vals[0], z2_vals[1] - z2_vals[0], z3_vals[1] - z3_vals[0])
    verts, faces, _, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"Calabi–Yau Slice: {expr}")
    plt.show()

# =========================
# Option 4: 3D solid (with auto isovalue fix)
# =========================
def plot_3d_solid(expr: str, grid_size: int = 50, bounds: tuple[float, float] = (-2.0, 2.0), isovalue: float = 0.0) -> None:
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
    magnitude = np.abs(values)
    min_val, max_val = magnitude.min(), magnitude.max()
    if not (min_val <= isovalue <= max_val):
        print(f"⚠️ Adjusting isovalue from {isovalue} to midpoint of range ({min_val:.3f}, {max_val:.3f})")
        isovalue = (min_val + max_val) / 2
    spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])
    verts, faces, _, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"3D Solid: {expr}")
    plt.show()

# =========================
# Option 5: Interactive 3D plot (Solid mode with auto isovalue fix)
# =========================
def plot_interactive_3d(expr: str, mode: str = "solid", grid_size: int = 50,
                        bounds: tuple[float, float] = (-2.0, 2.0), isovalue: float = 0.0) -> None:
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if mode.lower() == "solid":
        x_vals = np.linspace(bounds[0], bounds[1], grid_size)
        y_vals = np.linspace(bounds[0], bounds[1], grid_size)
        z_vals = np.linspace(bounds[0], bounds[1], grid_size)
        X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
        try:
            values = eval(expr, safe_globals, {"x": X, "y": Y, "z": Z})
        except Exception as e:
            print(f"Error parsing solid function: {e}")
            return
        magnitude = np.abs(values)
        min_val, max_val = magnitude.min(), magnitude.max()
        if not (min_val <= isovalue <= max_val):
            print(f"⚠️ Adjusting isovalue from {isovalue} to midpoint of range ({min_val:.3f}, {max_val:.3f})")
            isovalue = (min_val + max_val) / 2
        spacing = (x_vals[1] - x_vals[0], y_vals[1] - y_vals[0], z_vals[1] - z_vals[0])
        verts, faces, _, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
        ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis

# =========================
# Option 6: Complex 3D solid graphing
# =========================
def plot_complex_3d_solid(expr: str, grid_size: int = 50,
                          bounds: tuple[float, float] = (-2.0, 2.0), isovalue: float = 0.0) -> None:
    """
    Plots a complex-valued 3D solid using Marching Cubes.

    Parameters:
        expr (str): Function in terms of x, y, z.
        grid_size (int): Number of points per axis.
        bounds (tuple): Min and max bounds for each axis.
        isovalue (float): Isosurface value for Marching Cubes.
    """
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
    verts, faces, _, _ = measure.marching_cubes(magnitude, level=isovalue, spacing=spacing)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='viridis', alpha=1.0)
    ax.set_title(f"Complex 3D Solid: {expr}")
    plt.show()

# =========================
# Option 7: Complex 3D surface graphing
# =========================
def plot_complex_3d_surface(expr: str, x_min: float = -5.0, x_max: float = 5.0,
                            y_min: float = -5.0, y_max: float = 5.0,
                            resolution: int = 200, z_mode: str = "real") -> None:
    """
    Plots a complex-valued 3D surface.

    Parameters:
        expr (str): Function in terms of x, y.
        x_min, x_max, y_min, y_max (float): Bounds for x and y axes.
        resolution (int): Number of points per axis.
        z_mode (str): 'real', 'imag', or 'magnitude'.
    """
    safe_globals = {"__builtins__": None, "np": np, "math": math}
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = np.linspace(y_min, y_max, resolution)
    X, Y = np.meshgrid(x_vals, y_vals)
    try:
        values = eval(expr, safe_globals, {"x": X, "y": Y})
    except Exception as e:
        print(f"Error parsing complex 3D surface function: {e}")
        return

    z_mode_lower = z_mode.lower()
    if z_mode_lower == "real":
        Z = np.real(values)
    elif z_mode_lower == "imag":
        Z = np.imag(values)
    elif z_mode_lower == "magnitude":
        Z = np.abs(values)
    else:
        print(f"⚠️ Invalid z_mode '{z_mode}'. Using real part.")
        Z = np.real(values)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title(f"Complex 3D Surface ({z_mode.capitalize()}): {expr}")
    plt.show()

# =========================
# Main Menu
# =========================
def main_menu() -> None:
    """
    Displays the Python Graphing Menu and routes user choices to plotting functions.
    """
    while True:
        print("\n=== Python Graphing Menu ===")
        print("1. Plot 2D function(s)")
        print("2. Plot Calabi–Yau 3D slice (Marching Cubes)")
        print("3. Plot Riemann sphere mapping")
        print("4. Plot 3D solid (Marching Cubes)")
        print("5. Interactive 3D plot (Solid or Sphere)")
        print("6. Complex 3D solid graphing")
        print("7. Complex 3D surface graphing")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            expr_input = input("Enter function in terms of x (default: np.sin(x)): ") or "np.sin(x)"
            multi = input("Plot multiple functions? (y/n): ").strip().lower()
            if multi == "y":
                expr_list = [expr.strip() for expr in expr_input.split(",")]
                plot_2d_multi(expr_list)
            else:
                plot_2d(expr_input)

        elif choice == "2":
            expr = input("Enter function in terms of z1, z2, z3 (default: z1**2 + z2**3 - z3**2): ") or "z1**2 + z2**3 - z3**2"
            grid_size = int(input("Grid size (default 50): ") or 50)
            bounds_input = input("Bounds min,max (default -2,2): ") or "-2,2"
            bounds = tuple(map(float, bounds_input.split(",")))
            isovalue = float(input("Isovalue (default 0): ") or 0)
            plot_calabi_yau_3d(expr, grid_size, bounds, isovalue)

        elif choice == "3":
            expr = input("Enter function in terms of x (default: np.sin(x)): ") or "np.sin(x)"
            plot_riemann_sphere(expr)

        elif choice == "4":
            expr = input("Enter function in terms of x, y, z (default: x**2 + y**2 + z**2): ") or "x**2 + y**2 + z**2"
            grid_size = int(input("Grid size (default 50): ") or 50)
            bounds_input = input("Bounds min,max (default -2,2): ") or "-2,2"
            bounds = tuple(map(float, bounds_input.split(",")))
            isovalue = float(input("Isovalue (default 0): ") or 0)
            plot_3d_solid(expr, grid_size, bounds, isovalue)

        elif choice == "5":
            expr = input("Enter function (default: x**2 + y**2 + z**2 for solid, np.sin(x) for sphere): ") or "x**2 + y**2 + z**2"
            mode = input("Mode (solid/sphere, default: solid): ") or "solid"
            grid_size = int(input("Grid size (default 50): ") or 50)
            bounds_input = input("Bounds min,max (default -2,2): ") or "-2,2"
            bounds = tuple(map(float, bounds_input.split(",")))
            isovalue = float(input("Isovalue (default 0): ") or 0)
            plot_interactive_3d(expr, mode, grid_size, bounds, isovalue)

        elif choice == "6":
            expr = input("Enter complex function in terms of x, y, z (default: x**2 + y**2 + z**2 + 1j*z): ") or "x**2 + y**2 + z**2 + 1j*z"
            grid_size = int(input("Grid size (default 50): ") or 50)
            bounds_input = input("Bounds min,max (default -2,2): ") or "-2,2"
            bounds = tuple(map(float, bounds_input.split(",")))
            isovalue = float(input("Isovalue (default 0): ") or 0)
            plot_complex_3d_solid(expr, grid_size, bounds, isovalue)

        elif choice == "7":
            expr = input("Enter complex function in terms of x, y (default: x + 1j*y): ") or "x + 1j*y"
            x_min = float(input("x_min (default -5): ") or -5)
            x_max = float(input("x_max (default 5): ") or 5)
            y_min = float(input("y_min (default -5): ") or -5)
            y_max = float(input("y_max (default 5): ") or 5)
            resolution = int(input("Resolution (default 200): ") or 200)
            z_mode = input("Z mode (real/imag/magnitude, default: magnitude): ") or "magnitude"
            plot_complex_3d_surface(expr, x_min, x_max, y_min, y_max, resolution, z_mode)

        elif choice == "0":
            print("Exiting programme.")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 0 and 7.")

# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    main_menu()
