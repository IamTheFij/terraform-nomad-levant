#! /usr/bin/env python3
import json
import sys
from subprocess import check_output
from typing import Optional
from typing import overload
from typing import TypeVar


T = TypeVar("T")


@overload
def get_json(d: dict[str, str], key: str, default: None = None) -> None:
    ...


@overload
def get_json(d: dict[str, str], key: str, default: T = None) -> T:
    ...


def get_json(d: dict[str, str], key: str, default: Optional[T] = None) -> Optional[T]:
    if key not in d:
        return default

    return json.loads(d[key])


query = json.load(sys.stdin)

# Required
template_path = query["template_path"]

# Optional
consul_address = query.get("consul_address")
if consul_address is not None:
    consul_address = f"-consul-address={consul_address}"

# Need to parse JSON back
variables = [
    f'--var={key}={value}' for key, value in get_json(query, "variables", {}).items()
]
variable_files = [
    f'--var-file={value}' for value in get_json(query, "var_files", [])
]

args: list[str] = list(
    filter(
        None,
        ["levant", "render", consul_address]
        + variables
        + variable_files
        + [template_path],
    )
)

# print(" ".join(args), file=sys.stderr)
# exit(1)

template = check_output(args, stderr=sys.stderr)

print(json.dumps({"template": template.decode()}))
