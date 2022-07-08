from django.shortcuts import render
from itertools import chain
from django.views.generic import ListView
from Assets.models import PostCCB, PostEFCC, PostICPC


class SearchView(ListView):
    template_name = 'search/view.html'
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            ccb_results = PostCCB.objects.search(query)
            efcc_results = PostEFCC.objects.search(query)
            icpc_results = PostICPC.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                ccb_results,
                efcc_results,
                icpc_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return PostCCB.objects.none()  # just an empty queryset as default
