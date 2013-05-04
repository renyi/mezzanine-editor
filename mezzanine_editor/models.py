from django.db import models
from django.db.models.signals import post_syncdb
from django.dispatch import receiver
from django.contrib.auth.models import Group
from mezzanine.conf import settings
from mezzanine.blog.models import BlogPost


@receiver(post_syncdb, sender=BlogPost)
def create_default_editor_group(sender, **kwargs):
    editor_name = getattr(settings, "MEZZANINE_EDITOR_GROUPNAME", "Editor")
    editor, created = Group.objects.get_or_create(name=editor_name)
