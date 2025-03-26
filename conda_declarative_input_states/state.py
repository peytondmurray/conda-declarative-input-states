"""Code for managing the state of env.yml."""
import pathlib

from conda.base.context import context, env_name
from conda.env.env import Environment
from conda.history import History



def update_state(command: str):
    breakpoint()

    prefix = context.active_prefix
    env_yml = pathlib.Path(prefix) / "conda-meta" / "env.yml"

    # Parse the command to get the spec file
    packages = History(prefix=prefix).get_state()
    dependencies: list[str | dict[str, list[str]]] = []

    Environment(
        name=env_name(prefix),
        filename=str(env_yml),
        dependencies=dependencies,
        prefix=prefix,
    ).save()
