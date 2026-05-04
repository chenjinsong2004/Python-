from django.utils.safestring import mark_safe
import copy
from django.http.request import QueryDict
"""
在views.py中
    # 根据自己的情况筛选数据
    queryset = models.MobileInfo.objects.all()
    # 实例化分页对象
    page_object = Pagination(request, queryset)

    context = {
            "queryset":page_object.page_queryset,  # 分完页的数据
            "page_string":page_object.html(), # 生成页码
        }
    return render(request, 'pretty_list.html', context)

在HTML页面中
    <nav aria-label="Page navigation">
  <ul class="pagination">
    <li>
      <a href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
      {{page_string}}
    <li>
      <a href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
"""
class Pagination(object):
    def __init__(self, request, queryset, page_size = 10, page_param="page", plus=5):
        """
        request: 请求对象
        queryset: 符合条件的数据
        page_size: 每页多少条数据
        page_param: 在URL中传递获取分页参数
        plus: 显示当前页的前后几页
        """
        page = int(request.GET.get(page_param, 1))

        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
    
        # 计算出总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1

        self.total_page_count = total_page_count
        self.plus = plus


    def html(self):
        
        # 计算出前5页和后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库数据少，都没达到11页就用这个
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2*self.plus
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.page - self.plus
                    end_page = self.page
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
            
        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])

        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(),i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(),i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))
        
        page_string = mark_safe("".join(page_str_list))

        return page_string