# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class CategoryPlugin(CMSPluginBase):
    model = models.Category
    name = 'Category Plugin'
    render_template = 'category_icon_addon/category.html'
    allow_children = True
    child_classes = ['CategoryIconPlugin']


class CategoryIconPlugin(CMSPluginBase):
    model = models.CategoryIcon
    name = 'Icon'
    render_template = 'category_icon_addon/icon.html'
    require_parent = True
    parent_classes = ['CategoryPlugin']


plugin_pool.register_plugin(CategoryPlugin)
plugin_pool.register_plugin(CategoryIconPlugin)