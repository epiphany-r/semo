from django.shortcuts import render,reverse,redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from writerblogs import models
from authors.models import Author
from .forms import writersblogCreateForm

class WriterBlogListView(ListView):
    model = models.WriterBlog
    paginate_by = 4
    template_name = "writersblog/writersblog.html"
    queryset = models.WriterBlog.objects.order_by("-pk")

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

class WriterBlogDetail(DetailView):
    model = models.WriterBlog
    template_name = "writersblog/detail.html"
    context_object_name = 'writersblog_detail'

# # 포스트 등록
# # @method_decorator(login_required, name='dispatch')
class WriterBlogCreateView(CreateView):
    form_class = writersblogCreateForm
    template_name = 'writersblog/create.html'

    def get_success_url(self):
        return reverse('writerblogs:detail', args=[self.object.pk])

# # 포스트 수정
# # @method_decorator(login_required, name='dispatch')
class WriterBlogUpdateView(UpdateView):
    form_class = writersblogCreateForm
    template_name = 'writersblog/update.html'
    model = models.WriterBlog

    def get_success_url(self):
        return reverse('writerblogs:detail', args=[self.object.pk])

def WriterBlog_delete(request, pk):
    writerblog = models.WriterBlog.objects.get(pk=pk)
    writerblog.delete()
    return redirect('writerblogs:writerblog')