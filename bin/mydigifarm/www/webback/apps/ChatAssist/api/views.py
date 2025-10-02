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
# DESCRIPTION: Handles payloads from chat gpt.
# LASTMODIFIED: 20250929

#! .py

# views.py
from openai import OpenAI
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

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

## *|*|*|*|* End Section 1 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
