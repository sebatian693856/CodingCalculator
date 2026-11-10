import Gullie.graphing as t  # Import your main program file

def run_all_tests():
    """Run one example for each menu option in Test.py."""

    # Option 1 — Plot 2D function
    print("\n[TEST] Option 1: Single 2D function")
    t.plot_2d("np.sin(x)")

    print("\n[TEST] Option 1: Multiple 2D functions")
    t.plot_2d_multi(["np.sin(x)", "np.cos(x)"])

    # Option 2 — Calabi–Yau 3D slice
    print("\n[TEST] Option 2: Calabi–Yau slice")
    t.plot_calabi_yau_3d("z1**2 + z2**3 - z3**2", grid_size=50, bounds=(-2, 2), isovalue=0)

    # Option 3 — Riemann sphere mapping
    print("\n[TEST] Option 3: Riemann sphere")
    t.plot_riemann_sphere("np.sin(x)")

    # Option 4 — 3D solid
    print("\n[TEST] Option 4: 3D solid")
    t.plot_3d_solid("x**2 + y**2 + z**2", grid_size=50, bounds=(-2, 2), isovalue=4)

    # Option 5 — Interactive 3D plot (solid)
    print("\n[TEST] Option 5: Interactive solid")
    t.plot_interactive_3d("x**2 + y**2 + z**2", mode="solid", grid_size=50, bounds=(-2, 2), isovalue=4)

    # Option 5 — Interactive 3D plot (sphere)
    print("\n[TEST] Option 5: Interactive sphere")
    t.plot_interactive_3d("np.sin(x)", mode="sphere", grid_size=50)

    # Option 6 — Complex 3D solid
    print("\n[TEST] Option 6: Complex 3D solid")
    t.plot_complex_3d_solid("x**2 + y**2 + z**2 + 1j*z", grid_size=50, bounds=(-2, 2), isovalue=4)

    # Option 7 — Complex 3D surface
    print("\n[TEST] Option 7: Complex 3D surface")
    t.plot_complex_3d_surface("x + 1j*y", x_min=-5, x_max=5, y_min=-5, y_max=5, resolution=200, z_mode="magnitude")

if __name__ == "__main__":
    run_all_tests()
