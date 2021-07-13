from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Problem)
admin.site.register(ProblemNote)
admin.site.register(ProblemTag)
admin.site.register(TheoryNote)
admin.site.register(TheoryTopic)
admin.site.register(Score)
admin.site.register(Attempt)