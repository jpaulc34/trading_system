from .import_serializers import *

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only= True)

    class Meta:
        model = Profile
        fields = "__all__"

class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['avatar']


class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    stock = serializers.StringRelatedField(read_only=True)
    user_profile = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Order
        fields = ('user_profile','stock','quantity','total_price','created_at','update_at')

class OrderAddSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        # fields = "__all__"
        exclude = ("update_at","id",)

class UserOrderSerializer(serializers.ModelSerializer):
    
    user_profile = serializers.StringRelatedField(read_only=True)
    orders = OrderAddSerializer(many=True,read_only=True)

    class Meta:
        model = ProfileStatus
        fields = ('user_profile','created_at','orders')