#!/usr/bin/env python3
"""Validate D Research Ultra release metadata and worker lifecycle policy."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXPECTED_DISPATCH_ORDER = [
    "ephemeral-parallel",
    "ephemeral-sequential",
    "manual-checklist",
]


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return value


def _pyproject_version(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"(?ms)^\[project\]\s+.*?^version\s*=\s*\"([^\"]+)\"",
        text,
    )
    if match is None:
        raise ValueError("pyproject.toml is missing [project].version")
    return match.group(1)


def main() -> int:
    errors: list[str] = []

    try:
        package = _load_json(ROOT / "package.json")
        package_lock = _load_json(ROOT / "package-lock.json")
        manifest = _load_json(ROOT / "agents" / "manifest.json")
        pyproject_version = _pyproject_version(ROOT / "pyproject.toml")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    package_version = package.get("version")
    lock_version = package_lock.get("version")
    lock_root = package_lock.get("packages", {}).get("", {})
    lock_root_version = lock_root.get("version")
    manifest_version = manifest.get("version")

    versions = {
        "package.json": package_version,
        "package-lock.json": lock_version,
        "package-lock.json root package": lock_root_version,
        "pyproject.toml": pyproject_version,
        "agents/manifest.json": manifest_version,
    }
    if len(set(versions.values())) != 1:
        rendered = ", ".join(f"{name}={value!r}" for name, value in versions.items())
        errors.append(f"release versions do not match: {rendered}")

    lifecycle = manifest.get("worker_lifecycle")
    if not isinstance(lifecycle, dict):
        errors.append("agents/manifest.json is missing worker_lifecycle")
    else:
        if lifecycle.get("default") != "ephemeral":
            errors.append("worker_lifecycle.default must be 'ephemeral'")
        if lifecycle.get("dispatch_order") != EXPECTED_DISPATCH_ORDER:
            errors.append(
                "worker_lifecycle.dispatch_order must be "
                f"{EXPECTED_DISPATCH_ORDER!r}"
            )
        if lifecycle.get("persistent_registration") != "explicit-user-opt-in":
            errors.append(
                "worker_lifecycle.persistent_registration must be "
                "'explicit-user-opt-in'"
            )
        expected_model_policy = "inherit-host-default-unless-explicitly-configured"
        if lifecycle.get("model_policy") != expected_model_policy:
            errors.append(
                "worker_lifecycle.model_policy must be "
                f"{expected_model_policy!r}"
            )

    roles = manifest.get("roles")
    if not isinstance(roles, list) or len(roles) != 6:
        errors.append("agents/manifest.json must define exactly six roles")
    else:
        role_ids = [role.get("id") for role in roles if isinstance(role, dict)]
        if any(not isinstance(role_id, str) or not role_id for role_id in role_ids):
            errors.append("every manifest role must have a non-empty string ID")
        if len(role_ids) != len(set(role_ids)):
            errors.append("agents/manifest.json role IDs must be unique")
        for role in roles:
            if not isinstance(role, dict):
                errors.append("every manifest role must be a JSON object")
                continue
            role_file = role.get("file")
            if not isinstance(role_file, str) or not (ROOT / role_file).is_file():
                errors.append(f"missing role file for {role.get('id')!r}: {role_file!r}")

    orchestrator = manifest.get("orchestrator")
    orchestrator_file = (
        orchestrator.get("file") if isinstance(orchestrator, dict) else None
    )
    if (
        not isinstance(orchestrator_file, str)
        or not (ROOT / orchestrator_file).is_file()
    ):
        errors.append(f"missing orchestrator file: {orchestrator_file!r}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(
        "OK: Ultra contract valid "
        f"(version {package_version}, 6 roles, ephemeral-first lifecycle)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
