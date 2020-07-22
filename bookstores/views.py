from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.db.models import Q

# 로그인 인증 decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Bookstore
from .forms import BookstoreCreateForm

# 서점 목록
class BookstoreListView(ListView):
    model = Bookstore
    template_name = 'bookstores/list.html'
    context_object_name = 'bookstore_list'
    paginate_by = 5
    queryset = Bookstore.objects.all().order_by('-pk')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        
        paginator = context['paginator']
        page_number_range = 5
        current_page = int(self.request.GET.get('page', 1)) 

        start_index = int((current_page-1)/page_number_range)*page_number_range 
        end_index = start_index + page_number_range 

        current_page_group_range = paginator.page_range[start_index:end_index]

        start_page = paginator.page(current_page_group_range[0]) 
        end_page = paginator.page(current_page_group_range[-1])

        has_previous_page = start_page.has_previous()
        has_next_page = end_page.has_next()

        context['current_page_group_range'] = current_page_group_range
        if has_previous_page: 
            context['has_previous_page'] = has_previous_page
            context['previous_page'] = start_page.previous_page_number
        
        if has_next_page:
            context['has_next_page'] = has_next_page
            context['next_page'] = end_page.next_page_number
        
        return context

# 서점 상세보기
class BookstoreDetailView(DetailView):
    model = Bookstore
    template_name = 'bookstores/detail.html'
    context_object_name = 'bookstore_detail'

# 서점 등록
# @method_decorator(login_required, name='dispatch')
class BookstoreCreateView(CreateView):
    form_class = BookstoreCreateForm
    template_name = 'bookstores/create.html'

    def get_success_url(self):
        return reverse('bookstores:detail', args=[self.object.pk])

# 서점 수정
# @method_decorator(login_required, name='dispatch')
class BookstoreUpdateView(UpdateView):
    form_class = BookstoreCreateForm
    template_name = 'bookstores/update.html'
    model = Bookstore

    def get_success_url(self):
        return reverse('bookstores:detail', args=[self.object.pk])

# 서점 삭제
# @login_required
def bookstore_delete(request, pk):
    bookstore = Bookstore.objects.get(pk=pk)
    bookstore.delete()
    return redirect('bookstores:list')

# 검색 기능
class BookstoreSearchView(ListView):
    model = Bookstore
    template_name = 'bookstores/search.html'
    context_object_name = 'search'
    queryset = Bookstore.objects.all().order_by('-pk')

    def get_queryset(self):
        result = super(BookstoreSearchView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(Q(bookstoreName__icontains=query))
        return result

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_number_range = 5   # 페이지 그룹에 속한 페이지 수
        current_page = int(self.request.GET.get('page',1))
        # 시작/끝 index 조회
        start_index = int((current_page-1)/page_number_range)*page_number_range
        end_index = start_index + page_number_range
        # 현재 페이지가 속한 페이지 그룹의 범위
        current_page_group_range = paginator.page_range[start_index : end_index]
        start_page = paginator.page(current_page_group_range[0])
        end_page = paginator.page(current_page_group_range[-1])
        has_previous_page = start_page.has_previous()
        has_next_page = end_page.has_next()
        context['current_page_group_range'] = current_page_group_range
        if has_previous_page:
            context['has_previous_page'] = has_previous_page
            context['previous_page'] = start_page.previous_page_number
        if has_next_page:
            context['has_next_page'] = has_next_page
            context['next_page'] = end_page.next_page_number
        return context