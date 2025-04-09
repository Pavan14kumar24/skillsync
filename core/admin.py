from django.contrib import admin
from .models import Course, Skill, SkillProficiency

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'progress')

class SkillProficiencyAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'proficiency')

admin.site.register(Course, CourseAdmin)
admin.site.register(Skill)
admin.site.register(SkillProficiency, SkillProficiencyAdmin)