def user_can_manage_event(user, event):
    """Check if a user has permission to manage a given event."""
    return (
        user.role == 'admin' or
        (user.role == 'coordinator' and event.coordinator == user)
    )