# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################

import logging

from odoo import _,models,fields
from werkzeug import urls
from odoo.addons.wk_payment_moyasar.controllers.main import PaymentMoyasarController

_logger = logging.getLogger(__name__)


class PaymentTransactionTamara(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'moyasar':
            return res
        record_currency = self.env['res.currency'].browse(processing_values.get('currency_id'))
        processing_values.update({'currency':record_currency.name})
        provider_id = self.env['payment.provider'].browse(processing_values.get('provider_id'))
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        txValues = dict()
        txValues = {
            'amount'                : processing_values.get('amount')*pow(10,record_currency.decimal_places),
            'currency'              : processing_values.get('currency'),
            'description'           : processing_values.get('reference'),
            'publishable_api_key'   : provider_id.moyasar_public_key,
            'callback_url'          : str(urls.url_join(base_url, PaymentMoyasarController.checkout_url)) + "?reference={}".format(processing_values.get('reference')),
        }
        return txValues
    
    def _moyasar_payment_process(self, notification_data):
        self.ensure_one()
        if self.state != 'draft':
            _logger.info('Moyasar: trying to validate an already validated tx (ref %s)', self.reference)
            return True
        if notification_data.get('status') == 'paid':
            self.write({
                'provider_reference': notification_data.get('id'),
                'state_message': notification_data.get('message')
                })
            self._set_done()
            return True
        elif notification_data.get('status') == 'failed':
            self.write({
                'provider_reference': notification_data.get('id'),
                'state_message': notification_data.get('message')
                })
            self._set_error(notification_data.get('message'))
            return True


    def _process_notification_data(self, notification_data):
        res = super()._process_notification_data(notification_data)
        if self.provider_code != 'moyasar':
            return res
        return self._moyasar_payment_process(notification_data)