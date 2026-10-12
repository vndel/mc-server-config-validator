#!/usr/bin/env python3
"""Parse YAML configuration and reject obvious unsafe deployment defaults."""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("Install dependency: python -m pip install PyYAML")


def main() -> int:
    roots = [Path(arg) for arg in sys.argv[1:]] or [Path("config")]
    files = sorted(p for root in roots for p in (root.rglob("*.yml") if root.is_dir() else [root]))
    errors = []
    for path in files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, (dict, list, type(None))):
                errors.append(f"{path}: top-level YAML must be a mapping or list")
            text = path.read_text(encoding="utf-8").lower()
            if "change-me" in text or "changeme" in text:
                errors.append(f"{path}: replace placeholder secret before deployment")
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{path}: {exc}")
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Validated {len(files)} YAML file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
