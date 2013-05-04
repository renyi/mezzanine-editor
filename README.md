Overview
---
A simple editor/moderation workflow for Mezzanine CMS.


Requirements
---
[Mezzanine CMS] [1]


Installation
---
1. Add "mezzanine_editor" to INSTALLED_APPS:

```
    INSTALLED_APPS = (
        "...",
        "mezzanine_editor",    
    )
```

Settings (Optional)
---
MEZZANINE_EDITOR_ENABLED

```python
Default: True
Description: Toggles editor workflow.
```


MEZZANINE_EDITOR_SUPER

```python
   Default: False
   Description: Treat superuser as an editor.
```


MEZZANINE_EDITOR_GROUPNAME

```python
   Default: "Editor"
   Description: Name for editor group.
```


[1]: http://mezzanine.jupo.org "Mezzanine CMS"
