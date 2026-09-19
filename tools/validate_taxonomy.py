from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "taxonomy"
FRAMEWORKS = ROOT / "frameworks"

errors = []
all_ids = set()

for path in sorted(list(TAXONOMY.rglob("*.yaml")) + list(FRAMEWORKS.rglob("*.yaml"))):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: YAML parse error: {exc}")
        continue
    if not isinstance(data, dict):
        errors.append(f"{path}: root must be a mapping")
        continue

    def walk(value):
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
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(data)

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"Validation passed: {len(all_ids)} unique AITRT identifiers.")
