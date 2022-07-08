from django.shortcuts import render
import razorpay
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from streaming.models import video

def home(request, video_prize):
    # print(video_prize)
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_ZdN5nmxrw5sv50", "TyzdEJAXhfBUkK1G84LmyTGb"))
        # client = razorpay.Client(
        #     auth=("rzp_live_lvV805jzg26l3e", "DKjT8vDtWONNqZhlzl5IsjEN"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    #     try:
    #         video_obj = video.objects.get(id=video_id)
    #         if not request.user.is_authenticated:
    #             all_videos = video.objects.all().filter(video_price=0)
    #             params = {'all_videos': all_videos}
    #         else:
    #             all_videos = video.objects.all().order_by('-id')
    #             params = {'all_videos': all_videos}
    #     except ObjectDoesNotExist:
    #         return render(request, '404.html')


    # params = {'video': video_obj,
    #           'all_videos': all_videos}
    params = { 'prize' : video_prize,
            
            }
    return render(request, 'index.html', params)

@csrf_exempt
def success(request):
    return render(request, "success.html")