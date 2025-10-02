# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250929
# VERSION: 1.0
# FILE: mydigifarm,1.0,views.py
# DESCRIPTION: Sets up view for user accounts.
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

from django.shortcuts import render
from django.core import serializers as core_serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# OpenAI
from openai import OpenAI
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Hostname endpoint
import socket

from apps.UserAccount.api.serializers import UserAccountSerializer, UserAccountForVaultSerializer
import uuid
import shortuuid

from apps.UserAccount.models import UserAccount

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from utilities.vault.index import upsert_secret, read_secret

from django.http import QueryDict

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

@api_view(['POST',])
def user_account_registration_view(request):
    if request.method == 'POST':
        # assigning username here so that we can use onwards
        request.data._mutable = True
        # uuid that will be used Id for secrets and in database as well
        user_id = shortuuid.uuid()
        request.data['id'] = user_id
        request.data["username"] = f"{request.data['first_name']} {request.data['last_name']}"
        request.data._mutable = False

        user_account_request_data = request.data.dict()
        query_dict_request_data = QueryDict('', mutable=True)
        query_dict_request_data.update(user_account_request_data)
        # removing this password so that it will not be saved to database inside useraccount's table
        del query_dict_request_data['password']
        query_dict_request_data._mutable = False

        # As, we need to check password as well
        serializer_vault = UserAccountForVaultSerializer(data=request.data)
        serializer = UserAccountSerializer(data=query_dict_request_data)

        data = {}

        if serializer_vault.is_valid():
            if serializer.is_valid() == False:
                if 'already exists' in serializer.errors['email'][0]:
                    return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
                else:
                    return Response(serializer.errors)
            else:
                user_account = serializer.save()

                secret_dict = {'username': request.data['username'], 'first_name': request.data['first_name'],
                               'last_name': request.data['last_name'], 'password': request.data['password'], 'id': user_id}
                upsert_secret(f'users/{user_id}', secret_dict)

                data['message'] = "Successfully registered a new user."

                # get only because on signal token is being created already in models.py
                token = Token.objects.get(user=user_account).key
                data['token'] = token

                data['id'] = user_id
                data['username'] = user_account.username
                data['first_name'] = user_account.first_name
                data['last_name'] = user_account.last_name
                data['email'] = user_account.email
        else:
            if 'already exists' in serializer_vault.errors['email'][0]:
                return Response(serializer_vault.errors, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer_vault.errors)

        return Response(data)


@api_view(['POST',])
def user_account_login_view(request):
    if request.method == 'POST':
        data = {}

        email = request.data["email"]
        password = request.data["password"]

        if not email and not password:
            data['message'] = "Email or password is missing."
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_account = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            data['message'] = "Account does not exists for this Email."
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        if user_account:
            serializer = UserAccountSerializer(user_account)

            user_id = serializer.data['id']

            user_from_vault = read_secret(f'users/{user_id}')

            vault_user_data = user_from_vault['data']

            if vault_user_data['password'] == password:
                data['message'] = "Successfully logged in."

                token, created = Token.objects.get_or_create(user=user_account)
                # user_token = core_serializers.serialize('json', [token,])
                data['token'] = token.key

                data['id'] = user_id
                data['username'] = serializer.data['username']
                data['first_name'] = serializer.data['first_name']
                data['last_name'] = serializer.data['last_name']
                data['email'] = serializer.data['email']

                return Response(data)

            data['message'] = "Password is wrong."
            return Response(data, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
def user_account_auth_view(request):
    if request.method == 'GET':
        data = {}
        user_account = request.user

        if user_account:
            serializer = UserAccountSerializer(user_account)

            data['message'] = "User is Authenticated"

            token, created = Token.objects.get_or_create(user=user_account)

            data['token'] = token.key

            data['id'] = serializer.data['id']
            data['username'] = serializer.data['username']
            data['first_name'] = serializer.data['first_name']
            data['last_name'] = serializer.data['last_name']
            data['email'] = serializer.data['email']

            return Response(data)

        else:
            data['message'] = "User is not Authorized"
            return Response(data, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
def user_account_logout_view(request):
    if request.method == 'GET':
        data = {}
        print(request.user.auth_token)
        print('shamsail ramzan')
        request.user.auth_token.delete()

        data['message'] = "User is successfully logged out."

        return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser])
def openai_prompt_view(request):
    # Get the Authorization header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return Response({'error': 'Missing or invalid Authorization header.'}, status=status.HTTP_401_UNAUTHORIZED)

    # Get the prompt from request body
    prompt = request.data.get('prompt')
    if not prompt:
        return Response({'error': 'Missing "prompt" in request body.'}, status=status.HTTP_400_BAD_REQUEST)

    # Set the OpenAI API key for this request
    client = OpenAI(api_key=auth_header)
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {
                "role": "developer",
                "content": "You are a helpful gardening assistant. Talk like shakespeare. Answer in 5 sentences or less."
                },
                {"role": "user", "content": prompt}
            ]
        )
        reply = completion.choices[0].message.content
        return Response({'response': reply}, status=status.HTTP_200_OK)

    except OpenAI.error.AuthenticationError:
        return Response({'error': 'Invalid OpenAI API token.'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET',])
def get_hostname_view(request):
    try:
        hostname = socket.gethostname()
    except:
        hostname = 'localhost'
    return Response({"hostname" : hostname}, status=status.HTTP_200_OK)

## *|*|*|*|* End Section 2 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
