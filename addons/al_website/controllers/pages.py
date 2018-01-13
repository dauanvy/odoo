# -*- coding: utf-8 -*-
# # from odoo import http
# # from odoo.addons.website.controllers.main import Website

# # #Hien thi du lieu ra homepage
# # class Website(Website):
	# # @http.route(auth='public')
	# # def index(self, data={},**kw):
		# # companies = http.request.env['res.company'].sudo().search([])
		# # data={'companies': companies}
		# # super(Website, self).index(**kw)
		# # #Co the thay template 'website.homepage' bang template khac vi su nhu 'website.services_detail'
		# # return http.request.render('website.homepage', data)
		
# # class Page(http.Controller):
	# # @http.route('/page/services', type='http', auth='public', website=True)
	# # def render_example_page(self):
		# # return http.request.render('website.services', {})
		
	# # @http.route('/page/services/detail', type='http', auth='public', website=True)
	# # def navigate_to_detail_page(self):
		# # companies = http.request.env['res.company'].sudo().search([])
		# # return http.request.render('website.services_detail', {'companies': companies})