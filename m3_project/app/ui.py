from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from django.contrib.auth.models import ContentType, Permission


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )

        self.field__last_login = ext.ExtDateField(
            label='last login',
            name='last_login',
            anchor='100%',
            format="d.m.Y"
        )

        self.field__superuser_status = ext.ExtCheckBox(
            label='superuser status',
            name='is_superuser',
            anchor='100%'
        )

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )

        self.field__first_name = ext.ExtStringField(
            label='first name',
            name='first_name',
            anchor='100%'
        )

        self.field__last_name = ext.ExtStringField(
            label='last name',
            name='last_name',
            anchor='100%'
        )

        self.field__email_address = ext.ExtStringField(
            label='email address',
            name='email',
            anchor='100%'
        )

        self.field__staff_status = ext.ExtCheckBox(
            label='staff status',
            name='is_staff',
            anchor='100%'
        )

        self.field__active_status = ext.ExtCheckBox(
            label='active status',
            name='is_active',
            anchor='100%'
        )

        self.field__date_joined = ext.ExtDateField(
            label='date joined',
            name='date_joined',
            anchor='100%',
            format="d.m.Y"
        )

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email_address,
            self.field__staff_status,
            self.field__active_status,
            self.field__date_joined,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='name',
            name='name',
            anchor='100%',
            allow_blank=False,
        )

        print(ContentType.objects.values_list("id", "model"))

        self.field__content_type = make_combo_box(
            label='content type',
            name='content_type_id',
            anchor='100%',
            allow_blank=False,
            data=ContentType.objects.values_list("id", "model")
        )

        self.field__codename = ext.ExtStringField(
            label='codename',
            name='codename',
            anchor='100%',
            allow_blank=False,
        )

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'
