from django.conf.urls import url
from objectpack import desktop

from .actions import UserPack, GroupPack, PermissionPack, ContentTypePack
from .controller import controller


def register_urlpatterns():
    return [url(*controller.urlpattern)]


def register_actions():
    return controller.packs.extend([
        UserPack(),
        GroupPack(),
        PermissionPack(),
        ContentTypePack()
    ])


def register_desktop_menu():
    desktop.uificate_the_controller(
        controller
    )
