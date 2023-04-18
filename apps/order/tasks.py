from django.core.mail import send_mail


def send_confirmation_mail(instance):
    message = f"""
    Zdravstvuite, {instance.user.username}!
    Podtverdite zakaz na adres {instance.address},

    http://localhost8000/order/{instance.pk}/confirm/

    Esli eto byli ne Vy, ignoriruite eto soobshenie 
    """
    send_mail(
        subject='Podtverjdenie zakaza',
        message=message,
        from_email='test@test.com',
        recipient_list=[instance.user.email],
        fail_silently=False
    )