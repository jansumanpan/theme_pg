# -*- coding: utf-8 -*-
from openerp import http

# class ThemePg(http.Controller):
#     @http.route('/theme_pg/theme_pg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_pg/theme_pg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_pg.listing', {
#             'root': '/theme_pg/theme_pg',
#             'objects': http.request.env['theme_pg.theme_pg'].search([]),
#         })

#     @http.route('/theme_pg/theme_pg/objects/<model("theme_pg.theme_pg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_pg.object', {
#             'object': obj
#         })