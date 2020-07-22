from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Q

from books.models import BookCategory, Publisher, Book


class BookList(generic.ListView):
    model = Book
    template_name = "books/list.html"
    context_object_name = "total_book_list"
    queryset = Book.objects.all().order_by("-pk")

    # 한 페이지에 보여줄 데이터 수
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        page_number_range = 5  # 페이지 그룹에 속한 페이지 수
        current_page = int(self.request.GET.get("page", 1))

        # 시작/끝 index 조회
        start_index = int((current_page - 1) / page_number_range) * page_number_range
        end_index = start_index + page_number_range

        # 현재 페이지가 속한 페이지 그룹의 범위
        current_page_group_range = paginator.page_range[start_index:end_index]

        start_page = paginator.page(current_page_group_range[0])
        end_page = paginator.page(current_page_group_range[-1])

        has_previous_page = start_page.has_previous()
        has_next_page = end_page.has_next()

        context["current_page_group_range"] = current_page_group_range
        if has_previous_page:
            context["has_previous_page"] = has_previous_page
            context["previous_page"] = start_page.previous_page_number

        if has_next_page:
            context["has_next_page"] = has_next_page
            context["next_page"] = end_page.next_page_number

        categoryList = BookCategory.objects.all()
        context["categoryList"] = categoryList

        return context


class BookSearchView(generic.ListView):
    model = Book
    template_name = "books/search.html"
    context_object_name = "book_search"
    queryset = Book.objects.all().order_by("-pk")

    def get_queryset(self):
        result = super(BookSearchView, self).get_queryset()
        query = self.request.GET.get("q")
        query2 = self.request.GET.get("category")
        print(query)
        print(query2)
        if query:
            result = result.filter(Q(bookTitle__icontains=query))
        elif query2:
            result = result.filter(Q(bookCategoryID=query2))

        return result

    # 한 페이지에 보여줄 데이터 수
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context["paginator"]
        page_number_range = 5  # 페이지 그룹에 속한 페이지 수
        current_page = int(self.request.GET.get("page", 1))

        # 시작/끝 index 조회
        start_index = int((current_page - 1) / page_number_range) * page_number_range
        end_index = start_index + page_number_range

        # 현재 페이지가 속한 페이지 그룹의 범위
        current_page_group_range = paginator.page_range[start_index:end_index]

        start_page = paginator.page(current_page_group_range[0])
        end_page = paginator.page(current_page_group_range[-1])

        has_previous_page = start_page.has_previous()
        has_next_page = end_page.has_next()

        context["current_page_group_range"] = current_page_group_range
        if has_previous_page:
            context["has_previous_page"] = has_previous_page
            context["previous_page"] = start_page.previous_page_number

        if has_next_page:
            context["has_next_page"] = has_next_page
            context["next_page"] = end_page.next_page_number

        categoryList = BookCategory.objects.all()
        context["categoryList"] = categoryList

        return context


class BookDetailView(generic.DetailView):
    queryset = Book.objects.all()
    template_name = "books/detail.html"
    context_object_name = "book_detail"
