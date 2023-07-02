"""
自定义分类组件
"""
from django.utils.safestring import mark_safe

import copy


class Pagination:

#####################封装功能普适版#######################

    def __init__(self,req,queryset,plus=5,page_size=15,pages="page"):

        query_dict = copy.deepcopy(req.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.enpage = pages

#设置可跳转页数
        self.plus = plus
#获取当前页（默认为1）
        page = int(req.GET.get(pages, 1))
        # 如果不是整数
        if type(page) != int:
            # 强制让页码为1
            page = 1
        self.page = page
        self.page_size=page_size
         
#每页面展示的数据条数（有序）
        self.start = (self.page - 1) * self.page_size
        self.end = self.page * self.page_size
        self.page_queryset = queryset[self.start:self.end]


#计算总页数
        total_count = queryset.count()
        #非实例变量（无self.前缀）只在特定的方法或函数内部使用
        total_page_count, div = divmod(total_count,self.page_size)
        if div:
            total_page_count +=1
        self.page_count = total_page_count


#####################封装功能细调版#######################

    def pagenum(self):
#每页面展示可跳转页面值
        # 如果总页数大于 11
        if self.page_count > self.plus * 2 + 1:
            # 如果当前页面页码位置小于等于5，页面显示1-11页
            if self.page <= 5:
                start_page = 1
                end_page = self.plus * 2 + 2
            # 当页面页码位置大于5时
            else:
                # 防止页码超出范围
                if self.page >= self.page_count - self.plus:
                    start_page = self.page_count - self.plus * 2
                    end_page = self.page_count + 1
                else:
                    # 计算出当前页的前5页和后5页
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1
        #若总页码小于11，页面仅显示
        else:
            start_page = 1
            end_page = self.page_count + 1

#创建页码
        # 页码
        page_str_list = []
    #！！！！！！！！！解决在搜索的同时分页的问题
       
# 跳到首页
    #########！！添加GET
        self.query_dict.setlist(self. enpage, [1])
        self.head_page = '?{}'.format(self.query_dict.urlencode())

# 跳到上10页
        # 当前页面值小于 11则直接跳到1
        if self.page < self.plus * 2 + 1:
    #########！！添加GET
            self.query_dict.setlist(self. enpage, [1])
            prev = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), "<<")
            page_str_list.append(prev)
        else:
    #########！！添加GET
            self.query_dict.setlist(self.enpage,[self.page - 10])
            prev = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), "<<")
            page_str_list.append(prev)

# 依次显示当前页面的11条分页
        for i in range(start_page, end_page):
            # 如果是当前页,高亮显示
            if self.page == i:
    #########！！添加GET
                self.query_dict.setlist(self. enpage, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
    #########！！添加GET
                self.query_dict.setlist(self. enpage, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

# 跳到下10页

        # 如果当前页面页数 大于 最大页面数量减去(plus*2+1),则直接跳到最后一页,防止超过最大页数
        if self.page >= self.page_count - self.plus * 2 + 1:
    #########！！添加GET
            self.query_dict.setlist(self.enpage,[self.page_count])
            next = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), ">>")
            page_str_list.append(next)
        else:
    #########！！添加GET
            self.query_dict.setlist(self.enpage,[self.page + 10])
            next = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), ">>")
            page_str_list.append(next)

        self.page_string = mark_safe("".join(page_str_list))
# 跳到尾页
    #########！！添加GET
        self.query_dict.setlist(self.enpage,[self.page_count])
        self.end_page = '?{}'.format(self.query_dict.urlencode())

