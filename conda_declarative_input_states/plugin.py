"""Plugin which manages the state of env.yml when the environment changes."""
from collections.abc import Iterable

from conda import plugins

from .state import update_state


@plugins.hookimpl
def conda_post_commands() -> Iterable[plugins.CondaPostCommand]:
    """Plugin that updates the env state when conda install or create is called."""
    yield plugins.CondaPostCommand(
        name="declarative-input-states",
        action=update_state,
        run_for={
            "create",
            "install",
            "remove",
            "uninstall",
            "update",
            "upgrade",
            "env_create",
            "env_remove",
            "env_update",
        },
    )
