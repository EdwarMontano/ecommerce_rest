from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.api.serializers import (
    UserSerializer,
    TestUserSerializer,
    UserListSerializer,
)
from apps.users.models import User


@api_view(["GET", "POST"])
def user_api_view(request):
    """user_api_view _summary_

    create and list users

    Args
    ----------
    request (HttpRequest): The HTTP request received by the view.

    Returns
    -------
    response: Un objeto Response que contiene listado de usuarios

    Example:
        GET /users/listAll/"""
    if request.method == "GET":
        users = User.objects.all()
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        print(request.data)
        if user_serializer.is_valid():
            # print(user_serializer.data)
            print("valido")
            user_serializer.save()
            print("guardado")
            response_data = {
                "message": "El objeto ha sido creado exitosamente",
                # 'data': user_serializer.data  # Aquí obtienes los datos serializados del objeto creado
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     user_serializer = UserSerializer(data=request.data)
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    #         return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(request, pk=None):
    """user_detail_api_view _summary_

    Esta vista maneja las solicitudes GET, PUT y DELETE para ver, actualizar y eliminar
    un usuario específico.

    Args:
        request (HttpRequest): La solicitud HTTP recibida por la vista.
        pk (int, optional): La clave primaria (ID) del usuario que se desea ver o modificar.

    Returns:
        Response: Un objeto Response que contiene los datos del usuario solicitado o un mensaje de éxito/fracaso.

    PermissionDenied: Si el usuario no tiene permisos para acceder a esta vista.

    Examples:
        Para ver un usuario existente:
        GET /api/users/1/

        Para actualizar un usuario existente:
        PUT /api/users/1/

        Para eliminar un usuario existente:
        DELETE /api/users/1/
    """
    # validation
    if not (user := User.objects.filter(id=pk).first()):
        return Response(
            {"messsage": "USER NOT FOUND"}, status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == "GET":
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        user.delete()
        return Response(
            {"messsage": "Usuario eliminado correctamente"}, status=status.HTTP_200_OK
        )
