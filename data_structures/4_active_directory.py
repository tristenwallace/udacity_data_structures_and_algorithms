class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    
    if len(group.get_groups()):
        for subGroup in group.get_groups():
            if is_user_in_group(user, subGroup):
                return True
    
    return False

###--- TESTING ---###
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# Test Case 1: Basic Membership Check
print("\nTest Case 1: Basic Membership Check")
print("Is sub_child_user in parent group?", is_user_in_group(sub_child_user, parent))  # Expected: True
print("Is sub_child_user in child group?", is_user_in_group(sub_child_user, child))  # Expected: True
print("Is sub_child_user in sub_child group?", is_user_in_group(sub_child_user, sub_child))  # Expected: True

# Test Case 2: User Not Found
print("\nTest Case 2: User Not Found")
nonexistent_user = "ghost"
print("Is 'ghost' in parent group?", is_user_in_group(nonexistent_user, parent))  # Expected: False

# Test Case 3: Empty Group
print("\nTest Case 3: Empty Group")
empty_group = Group("empty")
print("Is any user in empty group?", is_user_in_group("any_user", empty_group))  # Expected: False

# Test Case 4: Large Group Hierarchy
print("\nTest Case 4: Large Group Hierarchy")
root_group = Group("root")
current_group = root_group
for i in range(300):  # Creating a deep hierarchy
    new_group = Group(f"level_{i}")
    current_group.add_group(new_group)
    current_group = new_group

deep_user = "deep_user"
current_group.add_user(deep_user)
print("Is 'deep_user' in root group?", is_user_in_group(deep_user, root_group))  # Expected: True