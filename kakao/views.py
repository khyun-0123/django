import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def random(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        mymsg = body['userRequest']['utterance']
        response = '다시 말해줘'
        if '쿠우쿠우' in mymsg or '준현' in mymsg:
            response = "성공"

        response_data = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        'simpleText': {
                            'text': response
                        }
                    }
                ]
            }
        }
        return JsonResponse(response_data)
    elif request.method == 'GET':
        return JsonResponse({'message': 'GET 요청을 받아들일 수 없습니다.'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
