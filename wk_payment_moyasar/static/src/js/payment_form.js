/** @odoo-module */
/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */

import paymentForm from '@payment/js/payment_form';
import MoyasarPaymentForm from '@wk_payment_moyasar/js/moyasar_payment';

paymentForm.include({
    _processRedirectFlow(providerCode, paymentOptionId, paymentMethodCode, processingValues) {
        if (providerCode === 'moyasar') {
            const div = document.createElement('div');
            div.innerHTML = processingValues['redirect_form_html'];
            const redirectForm = div.querySelector('div');
            document.body.appendChild(redirectForm);
            this.call('ui', 'unblock');
            new MoyasarPaymentForm();
        }
        else {
            this._super(...arguments);
        }
    }
});