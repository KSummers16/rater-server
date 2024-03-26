from rest_framework import viewsets, status, serializers, permissions
from rest_framework.response import Response
from raterapi.models import Review, Game


class ReviewSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ["id", "game", "user", "content", "is_owner"]
        read_only_fields = ["user"]

    def get_is_owner(self, obj):
        # Check if the user is the owner of the review
        return self.context["request"].user == obj.user


class ReviewViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):

        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        content = request.data.get("content")
        game_id = request.data.get("game_id")
        if not game_id:
            return Response(
                {"error": "Game ID is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(
                {"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND
            )

        review = Review.objects.create(
            user_id=request.user.id, content=content, game=game
        )
        try:
            serializer = ReviewSerializer(review, context={"request": request})

            return Response(serializer.data, status.HTTP_201_CREATED)

        except Exception as ex:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        try:
            review = Review.objects.get(pk=pk)

            serialized = ReviewSerializer(review, context={"request": request})

            return Response(serialized.data, status=status.HTTP_200_OK)

        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        try:
            review = Review.objects.get(pk=pk)

            if review.user.id != request.user.id:
                return Response(status=status.HTTP_403_FORBIDDEN)

            review.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
