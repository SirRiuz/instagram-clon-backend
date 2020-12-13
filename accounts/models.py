
# Django
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    

    def create_user(self,**kwargs) -> object:
        """ 
        Crea un usuario sin permisos
        de administrador
        """
        user = self.model(
            email=kwargs['email'],
            name=kwargs['name'],
            nickName=kwargs['nickName']
        )
        user.set_password(kwargs['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self , **kwargs) -> object:
        """ 
        Crea un usuario con permisos
        de administrador
        """
        superuser = self.create_user(**kwargs)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser,PermissionsMixin):

    objects = CustomUserManager()

    imageProfile = models.ImageField(
        upload_to='img',
        blank=True,
        null=False
    )

    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50,unique=True)

    email = models.EmailField(unique=True)

    userPage = models.URLField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'name','nickName' ]


    def __str__(self) -> str:
        return self.nickName


