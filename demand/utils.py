def user_show(request):
	query_all = False
    
	if request.user.role == 1:
		query_all = True

	return query_all