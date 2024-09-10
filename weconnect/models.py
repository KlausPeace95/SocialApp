from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # One user gets exactly one profile and profile is deleted if user gets deleted.
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False, # Users can follow someone without being followed back
        blank=True  # Users don't need to follow anyone
    )

    def __str__(self):
        return self.user.username

# This Method Creates a Profile for each new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Users automatically follow their own profiles
        # user_profile.follows.add([instance.profile.id])
        user_profile.follows.add(instance.profile)
        user_profile.save()
# post_save.connect(create_profile, sender=User)

class Posts(models.Model):
    objects = None
    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M} "
            f"{self.body[:30]}..."
        )



# Create your models here.
