def user_can_access_event(user, event):
    """
    Check if a user is authorized to access a specific event.
    """
    return (
        user.role == 'admin' or
        event in user.authorized_events.all()   
    )