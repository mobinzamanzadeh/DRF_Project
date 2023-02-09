from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    # اگر کابر سوپر یوزر باشد، بتواند در staff یوزر تغییر ایجاد کند

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    # فقط staff و superuser بتواند در سایت تغییر ایجاد کند

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsَAuthorOrReadOnly(BasePermission):
    # هرکس فقط متن خودش را بتواند تغییر دهد
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            # get access to superusers
            request.user.is_superuser or
            # get access to author
            obj.author == request.user,
        )


class IsَSuperuserOrStaffReadOnly(BasePermission):
    # یوزر ها را فقط سوپر یوزر بتواند تغییر دهد و staff فقط بتواند ببیند

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_staff:
            return True
        return bool(
            # get access to author read only
            request.method in SAFE_METHODS and request.user and request.user.is_staff
            or
            # get access to superusers
            request.user and request.user.is_superuser
        )
