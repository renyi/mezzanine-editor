from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.contrib import admin
from django.contrib.auth.models import Group
from mezzanine.conf import settings
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.core.models import CONTENT_STATUS_DRAFT, CONTENT_STATUS_PUBLISHED
from mezzanine.core.admin import OwnableAdmin


class EditorBlogPostAdmin(BlogPostAdmin):
    def queryset(self, request):
        """
        If editor_mode is true, and user is an editor, return unfiltered queryset.
        """
        editor_mode = getattr(settings, "MEZZANINE_EDITOR_ENABLED", True)

        if editor_mode:
            editor_name = getattr(settings, "MEZZANINE_EDITOR_GROUPNAME", "Editor")
            editor_super = getattr(settings, "MEZZANINE_EDITOR_SUPER", False)

            editor, created = Group.objects.get_or_create(name=editor_name)
            user_groups = request.user.groups.all()
            super_editor = request.user.is_superuser and editor_super

            if super_editor or editor in user_groups:
                return super(OwnableAdmin, self).queryset(request)

        return super(EditorBlogPostAdmin, self).queryset(request)

    def save_model(self, request, obj, form, change):
        """
        If editor_mode is true, blogpost is created and user is not an Editor,
        set blogpost status to draft.
        """
        editor_mode = getattr(settings, "MEZZANINE_EDITOR_ENABLED", True)

        if editor_mode and obj.status == CONTENT_STATUS_PUBLISHED:
            editor_name = getattr(settings, "MEZZANINE_EDITOR_GROUPNAME", "Editor")
            editor_super = getattr(settings, "MEZZANINE_EDITOR_SUPER", False)

            editor, created = Group.objects.get_or_create(name=editor_name)
            user_groups = request.user.groups.all()
            super_editor = request.user.is_superuser and editor_super

            if not (super_editor or editor in user_groups):
                obj.status = CONTENT_STATUS_DRAFT
                messages.error(request, _('You do not have permission to publish content.'))

        obj.save()


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, EditorBlogPostAdmin)
