from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
from datetime import datetime
from django.views.generic import ListView


# 이달의 도서 
# 필요 요소: 도서 사진, 기사 제목, 기사 내용, 등록일자, 도서카테고리, 기사카테고리
# 기능 : 기사카테고리 드롭박스, 페이지네이션, 도서카테고리 박스 - 카테고리 별 filter, 등록일자 년 박스, 등록일자 월 박스
def ThisMonthBookView(request):
    # 연,월 카테고리 변수 선언
    book_info_date_year = []
    book_info_date_month = []
    page_year = None
    page_month = None
    page_book = None
    book_info = Article.objects.filter(articleCategory="book").order_by('-pk') #내림차순인 이유는 최신을 가장 먼저보여줘야하기 때문

    for i in book_info:
        year = i.articleDate.year
        month = i.articleDate.month
        book_info_date_year.append(year)
        book_info_date_month.append(month)

    #연월 카테고리 변수 완성
    book_info_date_year = set(book_info_date_year)
    book_info_date_month = set(book_info_date_month)

    #GET으로 오는 값에 따른 카테고리분류 
    if request.GET.get('cate_year'):
        page_year = request.GET.get('cate_year')
        book_info = Article.objects.filter(articleCategory="book",articleDate__year=page_year).order_by('-pk')

    elif request.GET.get('cate_month'):
        page_month = request.GET.get('cate_month')
        book_info = Article.objects.filter(articleCategory="book",articleDate__month=page_month).order_by('-pk')
    elif request.GET.get('cate_book'):
        page_book = request.GET.get('cate_book')
        book_info = Article.objects.filter(articleCategory="book",bookID__bookCategoryID__pk=page_book).order_by('-pk')
    
    #페이지네이션작업
    paginator = Paginator(book_info, 2) 
    page_number = request.GET.get('page')
    context = {}
    if paginator.num_pages > 1:
        context['is_paginated'] = True
    else:
        context['is_paginated'] = False
        
    context['page_obj'] = paginator.get_page(page_number)
    page_number_range = 5
    current_page = int(request.GET.get('page', 1))
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

    # 페이지가 달라져도 카테고리를 유지하기 위한 쿼리셋
    book_cate = Article.objects.filter(articleCategory="book").order_by('-pk')
    book_info_cate = []
    for i in book_cate:
        book_cate = i.bookID.bookCategoryID
        book_info_cate.append(book_cate)

    book_info_cate = set(book_info_cate)
    
    context['book_cate'] = book_info_cate
    context['book_info_date_year'] = book_info_date_year
    context['book_info_date_month'] = book_info_date_month
    context['page_year'] = page_year
    context['page_month'] = page_month
    context['page_book'] = page_book

    return render(request,"articles/book.html",context)
# 이달의 행사
# 필요 요소: 행사사진, 행사 이름, 기사 내용, 등록일자, 기사카테고리 
# 기능 : 기사카테고리 드롭박스, 검색도구, 페이지네이션
# pagination
def ThisMonthEventView(request):
    event_info = Article.objects.filter(articleCategory="event").order_by('-pk')
    paginator = Paginator(event_info, 2)
    page_number = request.GET.get('page')
    context = {}
    if paginator.num_pages > 1:
        context['is_paginated'] = True
    else:
        context['is_paginated'] = False

    context['page_obj'] = paginator.get_page(page_number)
    page_number_range = 5
    current_page = int(request.GET.get('page', 1))
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
    return render(request,"articles/event.html",context)
# 검색도구
def result(request):
    query = request.GET.get('query')
    page_number = request.GET.get('page')
    posts = None
    if query:
        posts = Article.objects.all().filter(articleTitle__contains=query,articleCategory="event").order_by('-pk')
    paginator = Paginator(posts,2)
    # page_obj = paginator.get_page(page_number)
    context = {}
    if paginator.num_pages > 1:
        context['is_paginated'] = True
    else:
        context['is_paginated'] = False
    context['query'] = query
    context['page_obj'] = paginator.get_page(page_number)
    page_number_range = 5
    current_page = int(request.GET.get('page', 1))
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
    return render(request,"articles/result.html",context)
 
# 이달의 작가 
# 필요 요소: 행사 사진, 작가사진, 작가등등 작가Id, 기사제목, 기사내용, 기사카테고리 
# 기능 : 기사카테고리 드롭박스
class ThisMonthAuthorListView(ListView):
    model = Article
    queryset = Article.objects.filter(articleCategory="author").order_by('-pk')
    template_name = 'articles/author.html'
    context_object_name = 'author_list'
    paginate_by = 1

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
        