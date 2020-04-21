from django.contrib import admin

# Register your models here.

from automl.models import MLModel, Configuration, Deployment, TraningResult, Datasource


admin.site.register(MLModel)
admin.site.register(Configuration)
admin.site.register(Deployment)
admin.site.register(TraningResult)
admin.site.register(Datasource)