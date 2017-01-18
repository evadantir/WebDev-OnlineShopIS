from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = "You have to login as customer first"
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.is_authenticated()

class IsReadOnly(permissions.BasePermission):
	my_safe_methods = ['GET']
	def has_permission(self,request,view):
		if request.method in self.my_safe_methods:
			return True
		return False

class OnlyCustomer(permissions.BasePermission):
    my_safe_methods = ['GET','POST']
    def has_permission(self,request,view):
        if request.user.is_authenticated():
            if request.method in SAFE_METHODS:
                return True
            else :
                return False
        else : #customer
            if request.method in self.my_safe_methods:
                return True
            else : return False

class CustomerPostPermission(permissions.BasePermission):
    my_safe_methods = ['POST']
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            if request.method in self.my_safe_methods:
                return True
            else :
                return False
        return request.method in SAFE_METHODS
