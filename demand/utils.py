def user_show(request):
    query_all = False
    
    for group in request.user.groups.all():
        if group.id == 1:
            query_all = True

    return query_all