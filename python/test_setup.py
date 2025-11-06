"""
Quick sanity check for the Python trading environment.

Imports the pinned dependencies and reports their versions. Exits with a
non-zero status if a dependency is missing so CI/scripts can pick it up.
"""

from __future__ import annotations

import importlib
import sys


def report(module_name: str, label: str) -> bool:
    """Attempt to import a module and print its status."""
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"[FAIL] {label}: not installed")
        return False

    version = getattr(module, "__version__", "unknown")
    print(f"[OK] {label} version: {version}")
    return True


def main() -> None:
    checks = [
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
    ]

    failures = 0
    for module_name, label in checks:
        if not report(module_name, label):
            failures += 1

    if failures:
        print("[FAIL] Environment not ready. Activate the venv and run "
              "`pip install -r requirements.txt`.")
        sys.exit(1)

    print("[OK] Environment ready!")


if __name__ == "__main__":
    main()
