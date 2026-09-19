from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
files = sorted(list((ROOT / "taxonomy").rglob("*.yaml")) + list((ROOT / "frameworks").rglob("*.yaml")))
errors = []
all_ids = set()

def walk(value, path):
    if isinstance(value, dict):
        if "id" in value:
            ident = value["id"]
            if not isinstance(ident, str) or not ident.startswith("AITRT-"):
                errors.append(f"{path}: invalid id {ident!r}")
            elif ident in all_ids:
                errors.append(f"{path}: duplicate id {ident}")
            else:
                all_ids.add(ident)
        for child in value.values():
            walk(child, path)
    elif isinstance(value, list):
        for child in value:
            walk(child, path)

for path in files:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: YAML parse error: {exc}")
        continue
    if not isinstance(data, dict):
        errors.append(f"{path}: root must be a mapping")
        continue
    walk(data, str(path.relative_to(ROOT)))

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"Validation passed: {len(all_ids)} unique AITRT identifiers.")
