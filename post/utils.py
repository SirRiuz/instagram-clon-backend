



def isPosteador(user,post) -> bool:

    """
      Esta pequeña funcion comprueba
      si el usuario es el posteador
      de un video
    """

    if user == post.user:
        return True
    else:
        return False
    


