class User:
    def __init__(self, username, groups=[]):
        self.username = username
        self.groups = groups
        self.permissions = {}

    def add_permission(self, resource, access_level):
        self.permissions[resource] = access_level

    def has_permission(self, resource, access_level):
        if resource in self.permissions:
            return self.permissions[resource] == access_level
        return False


class Group:
    def __init__(self, group_name):
        self.group_name = group_name


# Create users
user1 = User("user1", ["admins"])
user2 = User("user2", ["users"])
user3 = User("user3", ["users"])

# Create groups
admins_group = Group("admins")
users_group = Group("users")

# Define permissions
admins_group.add_permission("create", "full")
admins_group.add_permission("read", "full")
users_group.add_permission("read", "limited")

# Assign users to groups
user1.groups.append("admins")
user2.groups.append("users")
user3.groups.append("users")

# Check permissions
def check_permissions(user, resource, access_level):
    if user.has_permission(resource, access_level):
        print(f"{user.username} has {access_level} access to {resource}.")
    else:
        print(f"{user.username} does not have {access_level} access to {resource}.")

# Check user permissions
check_permissions(user1, "create", "full")
check_permissions(user1, "read", "full")
check_permissions(user2, "read", "limited")
check_permissions(user3, "read", "limited")
