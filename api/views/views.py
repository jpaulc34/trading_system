from .import_views import *


class AvatarUpdateView(UpdateAPIView):
    serializer_class = ProfileAvatarSerializer

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

# class CommentGetCreateView(generics.CreateAPIView,generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     # serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#     # lookup_field = "profile_status"

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return CommentAddSerializer
#         return StatusCommentSerializer

#     def get_object(self):
#         profile_status_pk = self.kwargs.get("profile_status_pk")
#         obj = get_object_or_404(ProfileStatus, pk=profile_status_pk)
        
#         return obj

#     def perform_create(self,serializer):
#         profile_status_pk = self.kwargs.get("profile_status_pk")
#         profile_status = get_object_or_404(ProfileStatus, pk=profile_status_pk)
#         commenter = self.request.user.profile
#         serializer.save(profile_status=profile_status,profile_commenter=commenter)
    

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all().order_by('-id')
#     serializer_class = CommentSerializer

#     def perform_create(self,serializer):
#         profile_commenter = self.request.user.profile
#         serializer.save(profile_commenter=profile_commenter)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter]
    search_fields = ["city"]

# class ProfileStatusViewSet(viewsets.ModelViewSet):
#     serializer_class = ProfileStatusSerializer
#     permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
#     pagination_class = StandardResultsSetPagination

#     def get_queryset(self):
#         queryset = ProfileStatus.objects.all().order_by('-id')
#         username = self.request.query_params.get("username", None)
        
#         if username is not None:
#             queryset = ProfileStatus.objects.filter(user_profile__user__username=username).order_by('-id')

#         return queryset
    

#     def perform_create(self,serializer):
#         user_profile = self.request.user.profile
#         serializer.save(user_profile=user_profile)

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('-id')
    serializer_class = StockSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer

    def perform_create(self,serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class OrderGetCreateView(generics.CreateAPIView,generics.RetrieveAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderAddSerializer
        return OrderSerializer

    def get_object(self):
        user_profile_pk = self.kwargs.get("user_profile_pk")
        obj = get_object_or_404(ProfileStatus, pk=user_profile_pk)
        
        return obj

    def perform_create(self,serializer):
        user_profile_pk = self.kwargs.get("user_profile_pk")
        user_profile = get_object_or_404(Order, pk=user_profile_pk)
        commenter = self.request.user.profile
        serializer.save(user_profile=user_profile)
