from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
import os
import openpyxl
from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostWelcome, PostCCB, RegisterCCB, PostEFCC, RegisterEFCC, PostICPC, RegisterICPC
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q


def upload(request):
        return render(request, 'Assets/anti/upload.html')


class PostListWelcomeView(ListView):
    model = PostWelcome
    template_name = 'Assets/welcome.html'
    context_object_name = 'posts'
    paginate_by = 10


class SearchCCBView(View):
    def get(self, request, *args, **kwargs):
        querysetc = PostCCB.objects.all()
        queryc = request.GET.get('qsc')
        if queryc:
            querysetc = querysetc.filter(
                Q(surname__icontains=queryc) |
                Q(middle_name__icontains=queryc)
            ).distinct()
        context = {
            'querysetc': querysetc
        }
        return render(request, 'Assets/anti/CCBSearch_results.html', context)

class SearchCCBRegView(View):
    def get(self, request, *args, **kwargs):
        querysetcr = RegisterCCB.objects.all()
        querycr = request.GET.get('qscr')
        if querycr:
            querysetcr = querysetcr.filter(
                Q(name__icontains=querycr) |
                Q(rank__icontains=querycr)
            ).distinct()
        context = {
            'querysetcr': querysetcr
        }
        return render(request, 'Assets/anti/CCBregSearch_results.html', context)


class PostAntiCorruptView(ListView):
    model = PostWelcome
    template_name = 'Assets/anti/home_anti.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostCCBView(ListView):
    model = PostCCB
    template_name = 'Assets/anti/displayccb.html'
    context_object_name = 'postsccb'
    ordering = ['-date_posted']
    paginate_by = 10


class PostCCBCreateView(LoginRequiredMixin, CreateView):
    model = PostCCB
    template_name = 'Assets/anti/postccb_form.html'
    fields = ['file_number', 'declarant_id', 'surname', 'middle_name', 'other_names', 'qualification', 'cadre','curr_year',
              'rank_at_FAPPT', 'date_of_FAPPT','date_ob','date_of_confirmation','rank_at_LAPPT',
              'date_of_LAPPT', 'rank_at_PAPPT','date_of_PAPPT', 'year_of_1st_declaration', 'year_of_2nd_declaration',
              'year_of_3rd_declaration', 'year_of_4th_declaration', 'year_of_5th_declaration', 'year_of_6th_declaration',
              'year_of_7th_declaration', 'year_of_8th_declaration', 'year_of_9th_declaration',
              'action_taken', 'investigation_activities', 'envelop_number', 'box_number','front_img', 'particular_img',
              'banks_img', 'buildings_and_lands_img', 'farms_and_enter_img', 'vehicles_and_household_items_img', 'spouse_children_img',
              'bonds_shares_img', 'court_img', 'acknow_slip_img','add_img_1','add_img_2','add_img_3','add_img_4','add_img_5','add_img_6',
              'add_img_7','add_img_8','add_img_9','add_img_10','add_img_11','add_img_12','add_img_13','add_img_14','add_img_15','add_img_16',
              'add_img_17','add_img_18','add_img_19','add_img_20']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class PostCCBDetailView(DetailView):
        model = PostCCB
        context_object_name = 'postsccb'
        template_name = 'Assets/anti/ccbpost_detail.html'

class PostCCBRegView(ListView):
    model = RegisterCCB
    template_name = 'Assets/anti/displayregccb.html'
    context_object_name = 'postsccbreg'
    ordering = ['-date_posted']
    paginate_by = 10

class PostCCBCreateRegisterView(LoginRequiredMixin, CreateView):
    model = RegisterCCB
    template_name = 'Assets/anti/postccbreg_form.html'
    fields = ['declarant_ID','name','rank','date_issued','date_sworn_to','date_recieved']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)


class SearchEFCCView(View):
    def get(self, request, *args, **kwargs):
        querysetes = PostEFCC.objects.all()
        querye = request.GET.get('qes')
        if querye:
            querysetes = querysetes.filter(
                Q(surname__icontains=querye) |
                Q(middle_name__icontains=querye)
            ).distinct()
        context = {
            'querysetes': querysetes
        }
        return render(request, 'Assets/anti/EFCCSearch_results.html', context)

class SearchEFCCRegView(View):
    def get(self, request, *args, **kwargs):
        querysetesr = RegisterEFCC.objects.all()
        querysr = request.GET.get('qsr')
        if querysr:
            querysetesr = querysetesr.filter(
                Q(name__icontains=querysr) |
                Q(rank__icontains=querysr)
            ).distinct()
        context = {
            'querysetesr': querysetesr
        }
        return render(request, 'Assets/anti/EFCCregSearch_results.html', context)


class PostEFCCView(ListView):
    model = PostEFCC
    template_name = 'Assets/anti/displayefcc.html'
    context_object_name = 'postsefcc'
    ordering = ['-date_posted']
    paginate_by = 10

class PostEFCCCreateView(LoginRequiredMixin, CreateView):
    model = PostEFCC
    template_name = 'Assets/anti/postefcc_form.html'
    fields = ['file_number', 'declarant_id', 'surname', 'middle_name', 'other_names', 'qualification', 'cadre',
              'curr_year',
              'rank_at_FAPPT', 'date_of_FAPPT', 'date_ob', 'date_of_confirmation', 'rank_at_LAPPT',
              'date_of_LAPPT', 'rank_at_PAPPT', 'date_of_PAPPT', 'year_of_1st_declaration', 'year_of_2nd_declaration',
              'year_of_3rd_declaration', 'year_of_4th_declaration', 'year_of_5th_declaration',
              'year_of_6th_declaration',
              'year_of_7th_declaration', 'year_of_8th_declaration', 'year_of_9th_declaration',
              'action_taken', 'investigation_activities', 'envelop_number', 'box_number', 'front_img', 'particular_img',
              'banks_img', 'buildings_and_lands_img', 'farms_and_enter_img', 'vehicles_and_household_items_img',
              'spouse_children_img',
              'bonds_shares_img', 'court_img', 'acknow_slip_img', 'add_img_1', 'add_img_2', 'add_img_3', 'add_img_4',
              'add_img_5', 'add_img_6',
              'add_img_7', 'add_img_8', 'add_img_9', 'add_img_10', 'add_img_11', 'add_img_12', 'add_img_13',
              'add_img_14', 'add_img_15', 'add_img_16',
              'add_img_17', 'add_img_18', 'add_img_19', 'add_img_20']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class PostEFCCDetailView(DetailView):
        model = PostEFCC
        context_object_name = 'postsefcc'
        template_name = 'Assets/anti/efccpost_detail.html'

class PostEFCCRegView(ListView):
    model = RegisterEFCC
    template_name = 'Assets/anti/displayregefcc.html'
    context_object_name = 'postsefccreg'
    ordering = ['-date_posted']
    paginate_by = 10

class PostEFCCCreateRegisterView(LoginRequiredMixin, CreateView):
    model = RegisterEFCC
    template_name = 'Assets/anti/postefccreg_form.html'
    fields = ['declarant_ID','name','rank','date_issued','date_sworn_to','date_recieved']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class SearchICPCView(View):
    def get(self, request, *args, **kwargs):
        querysetis = PostICPC.objects.all()
        queryi = request.GET.get('qis')
        if queryi:
            querysetis = querysetis.filter(
                Q(surname__icontains=queryi) |
                Q(middle_name__icontains=queryi)
            ).distinct()
        context = {
            'querysetis': querysetis
        }
        return render(request, 'Assets/anti/ICPCSearch_results.html', context)

class SearchICPCRegView(View):
    def get(self, request, *args, **kwargs):
        querysetisr = RegisterICPC.objects.all()
        queryisr = request.GET.get('qisr')
        if queryisr:
            querysetisr = querysetisr.filter(
                Q(name__icontains=queryisr) |
                Q(rank__icontains=queryisr)
            ).distinct()
        context = {
            'querysetisr': querysetisr
        }
        return render(request, 'Assets/anti/ICPCregSearch_results.html', context)


class PostICPCView(ListView):
    model = PostICPC
    template_name = 'Assets/anti/displayicpc.html'
    context_object_name = 'postsicpc'
    ordering = ['-date_posted']
    paginate_by = 10

class PostICPCCreateView(LoginRequiredMixin, CreateView):
    model = PostICPC
    template_name = 'Assets/anti/posticpc_form.html'
    fields = ['file_number', 'declarant_id', 'surname', 'middle_name', 'other_names', 'qualification', 'cadre',
              'curr_year',
              'rank_at_FAPPT', 'date_of_FAPPT', 'date_ob', 'date_of_confirmation', 'rank_at_LAPPT',
              'date_of_LAPPT', 'rank_at_PAPPT', 'date_of_PAPPT', 'year_of_1st_declaration', 'year_of_2nd_declaration',
              'year_of_3rd_declaration', 'year_of_4th_declaration', 'year_of_5th_declaration',
              'year_of_6th_declaration',
              'year_of_7th_declaration', 'year_of_8th_declaration', 'year_of_9th_declaration',
              'action_taken', 'investigation_activities', 'envelop_number', 'box_number', 'front_img', 'particular_img',
              'banks_img', 'buildings_and_lands_img', 'farms_and_enter_img', 'vehicles_and_household_items_img',
              'spouse_children_img',
              'bonds_shares_img', 'court_img', 'acknow_slip_img', 'add_img_1', 'add_img_2', 'add_img_3', 'add_img_4',
              'add_img_5', 'add_img_6',
              'add_img_7', 'add_img_8', 'add_img_9', 'add_img_10', 'add_img_11', 'add_img_12', 'add_img_13',
              'add_img_14', 'add_img_15', 'add_img_16',
              'add_img_17', 'add_img_18', 'add_img_19', 'add_img_20']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)

class PostICPCDetailView(DetailView):
        model = PostICPC
        context_object_name = 'postsicpc'
        template_name = 'Assets/anti/icpcpost_detail.html'

class PostICPCRegView(ListView):
    model = RegisterICPC
    template_name = 'Assets/anti/displayregicpc.html'
    context_object_name = 'postsicpcreg'
    ordering = ['-date_posted']
    paginate_by = 10

class PostICPCCreateRegisterView(LoginRequiredMixin, CreateView):
    model = RegisterICPC
    template_name = 'Assets/anti/posticpcreg_form.html'
    fields = ['declarant_ID','name','rank','date_issued','date_sworn_to','date_recieved']

    def form_valid(self, form):
        form.instance.by = self.request.user
        return super().form_valid(form)








class PostPresidentView(ListView):
    model = PostWelcome
    template_name = 'Assets/pres/presidency.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostMinistriesView(ListView):
    model = PostWelcome
    template_name = 'Assets/min/ministries.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostPoliticalView(ListView):
    model = PostWelcome
    template_name = 'Assets/pol/political.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostUncategorizedView(ListView):
    model = PostWelcome
    template_name = 'Assets/uncat/uncategorized.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDepView(ListView):
    model = PostWelcome
    template_name = 'Assets/dep/departmentsAndAgencies.html'
    context_object_name = 'posts'
    paginate_by = 10


