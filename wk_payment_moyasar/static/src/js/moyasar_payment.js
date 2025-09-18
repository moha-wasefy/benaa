/** @odoo-module **/
/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */

import publicWidget from "@web/legacy/js/public/public_widget";
import { loadCSS, loadJS } from "@web/core/assets";

var MoyasarPaymentForm = publicWidget.Widget.extend({

    init: async function(){
        var self = this;
        var moyasar_js = "https://cdn.moyasar.com/mpf/1.12.0/moyasar.js";
        var moyasar_css = "https://cdn.moyasar.com/mpf/1.12.0/moyasar.css";
        await loadJS(moyasar_js);
        await loadCSS(moyasar_css);
        return self.start();
    },

    start: function () {
        Moyasar.init({
            element                 :  '.mysr-form',
            amount                  :  $('.amount').val(),
            currency                :  $('.currency').val(),
            description             :  $('.description').val(),
            publishable_api_key     :  $('.publishable_api_key').val(),
            callback_url            :  $('.callback_url').val(),
            methods                 :  ['creditcard'],
            
        })
        $('.payment_moyasar_modal').modal('show');
        $('#moyasar_close').on('click',function(){
            window.location.reload();
        })
    },
});
export default MoyasarPaymentForm;