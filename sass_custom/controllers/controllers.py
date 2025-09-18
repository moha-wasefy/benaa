# -*- coding: utf-8 -*-
# from odoo import http


# class SassCustom(http.Controller):
#     @http.route('/sass_custom/sass_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sass_custom/sass_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sass_custom.listing', {
#             'root': '/sass_custom/sass_custom',
#             'objects': http.request.env['sass_custom.sass_custom'].search([]),
#         })

#     @http.route('/sass_custom/sass_custom/objects/<model("sass_custom.sass_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sass_custom.object', {
#             'object': obj
#         })

