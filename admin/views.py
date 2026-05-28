from sqladmin import ModelView

from db.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.surname, User.email]
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "accounts"
    column_searchable_list = [User.name, User.email]
    column_sortable_list = [User.id]
    # column_details_exclude_list = []

