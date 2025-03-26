"""Code for managing the state of env.yml."""
import pathlib

from conda.base.context import context, env_name
from conda.env.env import Environment
from conda.history import History


def update_state(_command: str):
    prefix = context.active_prefix
    env_yml = str(pathlib.Path(prefix) / "conda-meta" / "env.yml")

    packages = History(prefix=prefix).get_state()
    Environment(
        name=env_name(prefix),
        filename=env_yml,
        dependencies=list(packages),
        prefix=prefix,
    ).save()
