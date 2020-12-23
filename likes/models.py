

# Django
from django.db import models



class AbstractBaseLike(models.Model):

    user = models.ForeignKey('accounts.User' , on_delete=models.CASCADE)
    likeDateCreated = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        abstract=True


class LikePost(AbstractBaseLike):

    """
      Este modelo se encarga de administrar
      todos los likes de las publicaciones  
    """

    post = models.ForeignKey('post.Post' , on_delete=models.CASCADE)

    def __str__(self) -> (str):
      return '[  {nick}  ] like to [  {postId}  ]'.format(nick=self.user.nickName,postId=self.post.id)



class LikeComent(AbstractBaseLike):

  """
    Este modelo se encarga de administrar
    todos los likes de los comentarios 
  """

  coment = models.ForeignKey('coments.Coment',on_delete=models.CASCADE)


  def __str__(self) -> (str):
    return '[  {nick}  ] like to [  {postId}  ]'.format(nick=self.user.nickName,postId=self.coment.id)
