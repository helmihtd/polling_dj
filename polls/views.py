from django.shortcuts import render, get_object_or_404
from django. http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# import models table
from .models import Question, Choice

# fungsi dibawah utk menampilkan pertanyaan
# ambil model question, masukkan ke variabel dgn tanggal terbaru dan tampilkan 5 list
# masukkan variabel latest ke objek, lalu masukkan ke variabel utk passing data ke template
# request untuk tampilkan halaman dari data passing variabel context
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Munculkan pertanyaan dan pilihan ketika klik detail
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Pertanyaan tidak ditemukan")
    return render(request, 'polls/detail.html', { 'question': question })

# ambil pertanyaan dan tampilkan hasilnya
# get object masukkan ke question dgn nilainy yaitu models dan primary key
# return request dan passing ke template
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # print request post choice
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay form pertanyaan voting ketika selesai vote
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Kamu belum memilih",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))