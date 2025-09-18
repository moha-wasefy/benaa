# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################

import logging

from odoo import models,fields

_logger = logging.getLogger(__name__)


class PaymentMoyasarConnect(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(selection_add=[('moyasar', 'Moyasar')], ondelete={'moyasar': 'set default'})
    moyasar_public_key = fields.Char(string="Moyasar Public Key",required_if_provider='moyasar')
    moyasar_secret_key = fields.Char(string="Moyasar Secret Key", required_if_provider='moyasar', groups='base.group_system')