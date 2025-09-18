# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################

import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class PaymentMoyasarController(http.Controller):
    checkout_url = '/payment/moyasar/checkout'

    @http.route(checkout_url, type='http', auth='public', csrf=False)
    def moyasar_payment_checkout(self,**kwargs):
        transaction_id = request.env['payment.transaction'].sudo().search([('reference','=',kwargs.get('reference'))])
        transaction_id._handle_notification_data('moyasar',kwargs)
        return request.redirect('/payment/status')