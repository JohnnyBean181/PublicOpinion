from django.shortcuts import render
from django.views import generic
from django.db.models import Prefetch
from .models import Combineddata, KeywordsAssociation
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "OpinionReader/index.html"
    context_object_name = "latest_opinion_list"

    def get_queryset(self):
        """Return the last five published questions."""
        # return Combineddata.objects.order_by("-date")[:250]
        # 使用Prefetch预加载关联的Keywords，通过KeywordsAssociation中间表
        prefetch_keywords = Prefetch(
            'keywordsassociation_set',  # 这里使用你的关联表名的小写形式
            queryset=KeywordsAssociation.objects.select_related('keyword'),  # 预先加载Keyword
            to_attr='keywords'  # 将关联的Keyword对象列表存储在'keywords'属性上
        )

        return (
            Combineddata.objects
            .order_by("-date")[:250]
            .prefetch_related(prefetch_keywords)
        )


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Combineddata
    template_name = "OpinionReader/detail.html"

