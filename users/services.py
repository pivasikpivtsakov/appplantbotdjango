from users.models import CustomUser


def get_user_data(user_id: int):
    return CustomUser.objects.get(id=user_id)
