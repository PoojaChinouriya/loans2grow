# from rest_framework import permissions

# # class IsLogin(permissions.BasePermission):


# class IsGuarantorRequired(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(request.user == obj)


# class IsDocumentVarification(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(request.user and request.user.is_authenticated and (request.user.role == 'Operational head'))
    
# class IsDisbursed(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(request.user and request.user.is_authenticated and (request.user.role == 'Account head'))
