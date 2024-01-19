# from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render, redirect
# from .models import Feedback

# @permission_required('feedback.can_view_feedback')
# def view_feedback(request):
#     feedback_list = Feedback.objects.all()
#     return render(request, 'feedback/view_feedback.html', {'feedback_list': feedback_list})

# @permission_required('feedback.can_add_feedback')
# def give_feedback(request):
#     if request.method == 'POST':
#         query = request.POST['query']
#         Feedback.objects.create(customer=request.user, query=query)
#         return redirect('give_feedback')
#     return render(request, 'feedback/give_feedback.html')