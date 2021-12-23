
from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from modelcluster.fields import ParentalKey
from wagtail.core.fields import StreamField
from blog.post_pager import pager

from wagtail.admin.edit_handlers import (
    FieldPanel, 
    MultiFieldPanel, 
    StreamFieldPanel, 
 
    )




class CareerListPage(Page):
    template = 'careers/jobs_list_page.html'
    
    description = models.CharField(max_length=100, blank=True, null=True, help_text='')
    jobs_per_page = models.IntegerField()
    subpage_types = ['careers.JobCategory',
                     ]
    
   
    max_count = 1
    

    def get_context(self, request, *args, **kwargs):
        per_page = self.jobs_per_page
        
        context = super().get_context(request, *args, **kwargs)
        all_jobs = JobPostDetail.objects.live().public().order_by('-first_published_at')
        job_categories = JobCategory.objects.live().public().all()

        context['add_careers_css'] = 'add_careers_css'
        context['all_jobs'] = all_jobs
        context['job_categories'] = job_categories
        
        
     
        return context
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
        StreamFieldPanel('description'),
            FieldPanel('jobs_per_page'),
        ], heading='Jobs Main Page Settings')
    ]


class JobCategory(Page):
    category_description = models.TextField()
    template = 'careers/jobs_list_page.html'
    subpage_types = ['careers.JobPostDetail', ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('category_description'),

        ], heading='Job Category')
    ]
    # subpage_types = ['blog.ArticleDetails', ]

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        all_jobs = CareerListPage.objects.live().child_of(self)

        try:
            # get per page from the bloglists
            obj_per_page = CareerListPage.objects.all()[0]
            per_page = obj_per_page.jobs_per_page
        except:
            per_page = 1
        # pager is a custom function imported from 'post_pager.py'
        all_jobs_posts = pager(request, all_jobs, per_page=per_page)
        context['jobs'] = all_jobs_posts

        context['current_category'] = self.title

        return context

    class Meta:
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'


class JobPostDetail(Page):
    template = 'careers/job_details.html'
    subpage_types =[]

    job_description = StreamField([
        ('job_description', blocks.RichTextBlock()),
       
    ], max_num=1)

    content_panels = Page.content_panels + [ 
        MultiFieldPanel([
            StreamFieldPanel('job_description'),   
        ], heading='Jobs  Desciption')
         
   
        
    ]    




    class Meta:
        verbose_name = 'JobPostDetail'
        verbose_name_plural = 'JobPostDetails'


    # max_count = 1
    # subpage_types = [None]


        

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)        
        context['add_careers_css'] = 'add_careers_css'

        return context


    
