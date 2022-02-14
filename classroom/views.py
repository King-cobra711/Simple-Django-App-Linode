from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm, CreateTeacherForm, UpdateTeacherForm
from django.urls import reverse, reverse_lazy
from classroom.models import Teacher
# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    # model_form.html
    model = Teacher
    form_class = CreateTeacherForm 
    template_name = 'classroom/teacher_form.html'
    success_url = reverse_lazy("classroom:teacher_list")

class TeacherListView(ListView):
    # model_list.html
    model = Teacher

    # override data thats sent back. Think of SQL WHERE statement (Filters)
    queryset = Teacher.objects.order_by('first_name')

    # Change the name of the object for the frontend
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    # RETURN ONLY 1 MODEL ENTRY PK
    # model_detail.html
    model = Teacher

class TeacherUpdateView(UpdateView):
    #only updating a single primary key
    model = Teacher
    form_class = UpdateTeacherForm 
    #remember that you can cusomize the fields to be used
    success_url = reverse_lazy('classroom:teacher_list')

class TeacherDeleteView(DeleteView):
    #Form --> Confirm Delete Button
    #Default template name:
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')

class ContactFormView(FormView):
    form_class = ContactForm 
    template_name = 'classroom/contact.html'

    # Success url
    success_url = reverse_lazy('classroom:thank_you')

    # What to do with the form
    def form_valid(self, form):
        self.request.session['sent_data'] = form.cleaned_data

    #Helpful link regarding cleaned data and how to use it on the success page.
    #https://stackoverflow.com/questions/12717054/send-form-data-from-views-to-template



        return super(ContactFormView, self).form_valid(form)
