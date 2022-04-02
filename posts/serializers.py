from rest_framework import serializers
from posts.models import Post, Comment, Upvotes


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]
        read_only_fields = ["id", "creation_date", "amount_of_upvotes"]
        depth = 0

    def create(self, validated_data):
        validated_data["author_name"] = self.context["request"].user
        return super(PostSerializer, self).create(validated_data)

    # def get_is_fan(self, obj) -> bool:
    #     """Check if a `request.user` has liked this tweet (`obj`).
    #     """
    #     user = self.context.get('request').user
    #     return likes_services.is_fan(obj, user)


class UpvotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvotes
        fields = ["post", "user"]

    def validate(self, data):
        """
        Check that start is before finish.
        """
        upvote = Upvotes.objects.filter(post=data["post"], user=data["user"])
        if upvote:
            raise serializers.ValidationError("The post is already" " upvoted by you")
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author_name", "content", "parent_post", "creation_date"]
        read_only_fields = ["author_name", "creation_date", "parent_post"]
        depth = 0

    def create(self, validated_data):
        validated_data["author_name"] = self.context["request"].user
        if validated_data["author_name"].is_anonymous:
            validation_error = serializers.ValidationError(
                "You should be logged in to post " "comments ", code=401
            )
            raise validation_error
        return super(CommentSerializer, self).create(validated_data)
