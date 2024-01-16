
def detectUser(user):
    if user.role == 1:
        rediredtUrl = 'vendorDashboard'
        return rediredtUrl
    elif user.role == 2:
        rediredtUrl = 'custDashboard'
        return rediredtUrl
    elif user.role == None and user.is_superadmin:
        rediredtUrl = '/admin'
        return rediredtUrl

