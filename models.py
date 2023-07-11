from django.db import models

# Create your models here.

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nombres, apellidos, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener correo electronico")
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self, username, email, nombres, apellidos, password, **extra_fields):
        usuario = self._create_user(
            username,
            email,
            nombres,
            apellidos,
            password,
            False,
            False,
            **extra_fields
        )

    def create_superuser(self, username, email, nombres, apellidos, password, **extra_fields):
        usuario = self._create_user(
            username,
            email,
            nombres,
            apellidos,
            password,
            True,
            True,
            **extra_fields
        )
