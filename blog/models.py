from django.core import paginator
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from modelcluster.fields import ParentalKey
from wagtail.core.fields import StreamField
from.post_pager import pager

from wagtail.admin.edit_handlers import (
    FieldPanel, 
    MultiFieldPanel, 
    StreamFieldPanel, 
    InlinePanel
    )
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
# Create your models here.


class BlogArticlesList(Page):
    template = 'blog/blog_articles_list.html'
    
    description = models.CharField(max_length=100, blank=True, null=True, help_text='')
    articles_per_page = models.IntegerField(max_length=3)
    subpage_types = ['blog.ArticleCategory', ]
    
   
    max_count = 1
    

    def get_context(self, request, *args, **kwargs):
        per_page = self.articles_per_page
        
        context = super().get_context(request, *args, **kwargs)
        all_posts = ArticleDetails.objects.live().public().order_by('-first_published_at')   
        parents = [post.get_parent().id for post in  all_posts]
        
        all_categories = ArticleCategory.objects.all()

        live_cats = all_categories.filter(id__in=parents)
        
        context = {
            'posts': pager(request, all_posts, per_page=per_page), #pager is a custom function from within the folder 'post_pager.py
            'categories': live_cats,
        }

        return context
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
        StreamFieldPanel('description'),
        FieldPanel('articles_per_page'),
        ], heading='Article Main Page Settings')
    ]

class ArticleAuthor(models.Model):
    '''
    This is the blog authors model that will hold all the authors
    
    '''
    name = models.CharField(max_length=100)
    author_bio = StreamField([
        ('author_bio', blocks.RichTextBlock(blank=False, null=True, default='Nothing')),

    ])
    
    photo = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, related_name='+', on_delete=models.SET_NULL)
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),           
            FieldPanel('author_bio'),           
            ImageChooserPanel('photo'),
        ],heading='Author Details(Name, Bio, & Photo')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article Author'
        verbose_name_plural = 'Article Authors'

register_snippet(ArticleAuthor)


class ArticleAuthorOrderable(Orderable):
    page = ParentalKey('blog.ArticleDetails', related_name='article_author')
    author = models.ForeignKey('blog.ArticleAuthor', on_delete=models.CASCADE)
    
    panels = [
        SnippetChooserPanel('author'),
    
    ]


class ArticleCategory(Page):   
    category_description = models.TextField()
    template = 'blog/blog_articles_list.html'

    content_panels = Page.content_panels + [
        MultiFieldPanel([            
            FieldPanel('category_description'),

        ], heading='Article Category')
    ]
    subpage_types = ['blog.ArticleDetails', ]

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        all_posts = ArticleDetails.objects.live().child_of(self)
        
        try:
            articles_per_page = BlogArticlesList.objects.all()[0] #get per page from the bloglists
            per_page = articles_per_page.articles_per_page
        except:
            per_page = 1
        # pager is a custom function imported from 'post_pager.py'
        posts = pager(request, all_posts, per_page=per_page)
        context['posts'] = posts

        context['current_category'] = self.title

        return context


    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'





class ArticleDetails(Page):
    template = 'blog/article_details.html'
    subpage_types =[]

    
    short_summary = models.TextField(blank=False, null=True, max_length=160)
   
    article_image = models.ForeignKey('wagtailimages.Image', blank=False, null=True, related_name='blogimage', on_delete=models.SET_NULL) 
    article_content = StreamField([
        ('article_content', blocks.RichTextBlock()),
       
    ], max_num=1)

    content_panels = Page.content_panels + [                  
        MultiFieldPanel([
            InlinePanel('article_author', label='Author', min_num=1, max_num=1)
        ], heading='Article Author'),

        MultiFieldPanel([
            FieldPanel('short_summary')
        ], heading='(Short Summary 150 to 160 characters)'),        
        
        ImageChooserPanel('article_image'),
        StreamFieldPanel('article_content', ),
    ]    


    class Meta:
        verbose_name = 'ArticleDetails'
        verbose_name_plural = 'ArticleDetails'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        latest_posts = ArticleDetails.objects.live().public().order_by('-first_published_at')
        post_id  = self.id
        latest_posts = latest_posts.exclude(id=post_id)
        latest_posts = latest_posts[:3]
        context ['latest_posts'] = latest_posts

        return context


    # max_count = 1
    # subpage_types = [None]


    
