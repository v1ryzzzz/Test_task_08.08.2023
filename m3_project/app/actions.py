from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Permission, Group, ContentType
from objectpack.ui import ModelEditWindow

from app.ui import UserAddWindow, PermissionAddWindow


class UserPack(ObjectPack):

    model = User
    add_window = edit_window = UserAddWindow
    add_to_desktop = True


class GroupPack(ObjectPack):

    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_desktop = True


class ContentTypePack(ObjectPack):

    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_desktop = True


class PermissionPack(ObjectPack):

    model = Permission
    add_window = edit_window = PermissionAddWindow
    add_to_desktop = True
