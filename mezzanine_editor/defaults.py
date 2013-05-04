from django.utils.translation import ugettext as _
from mezzanine.conf import register_setting


register_setting(
    name="MEZZANINE_EDITOR_ENABLED",
    description=_("Toggles editor workflow."),
    editable=True,
    default=True,
)


register_setting(
    name="MEZZANINE_EDITOR_GROUPNAME",
    description=_("Name for editor group."),
    editable=True,
    default="Editor",
)


register_setting(
    name="MEZZANINE_EDITOR_SUPER",
    description=_("Treat superuser as an editor."),
    editable=True,
    default=False,
)
