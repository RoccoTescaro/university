from django.contrib.auth.models import AnonymousUser

def usernameContext(request):
  user = request.user
  if not isinstance(user, AnonymousUser):
    username = user.username
  else:
    username = None
  return {'username': username}