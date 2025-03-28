# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework import serializers
# from django.contrib.auth.models import User
#
# from users.models import Payment
#
#
# class PaymentSerializer(serializers.ModelSerializer):
#     product_type = serializers.ChoiceField(
#         choices=[("tabel", "Tabel")]
#     )
#     product_id = serializers.IntegerField()
#
#     class Meta:
#         model = Payment
#         fields = "__all__"
#
#
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Добавление пользовательских полей в токен
#         token["username"] = user.username
#         token["email"] = user.email
#
#         return token
