# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
#################################################################################

{
    "name"              :  "Website Moyasar Payment Gateway",
    "summary"           :  """Maximize Odoo website potential using Moyasar Payment Gateway integration. 
                            Seamlessly enhance user experience, security, and payment diversity, 
                            optimizing transaction processes. Website Moyasar Payment Gateway offers 
                            encrypted and secure payment catering to various customers' needs. It offers several 
                            payment methods for users to choose from.""",
    "category"          :  "Website",
    "version"           :  "1.0.0",
    "sequence"          :  1,
    "author"            :  "Webkul Software Pvt. Ltd.",
    "license"           :  "Other proprietary",
    "website"           :  "https://store.webkul.com/odoo-website-moyasar-payment-gateway.html",
    "description"       :  """Effortlessly optimize your payment solutions with Odoo Website Moyasar 
                            Payment Gateway. Elevate user experience through secure and streamlined transactions.""",
    "live_test_url"     :  'https://odoodemo.webkul.com/?module=wk_payment_moyasar',
    "depends"           :  ['payment'],
    "data"              :  [
                            'views/payment_moyasar_template.xml',
                            'views/payment_provider_views.xml',
                            'views/payment_templates.xml',
                            'data/moyasar_payment_data.xml',
                            ],
    "images"            :  ['static/description/banner.png'],
    "installable"       :  True,
    "auto_install"      :  False,
    "price"             :  149,
    "currency"          :  "USD",
    'assets'            : {
                            'web.assets_frontend': [
                                'wk_payment_moyasar/static/src/js/payment_form.js',
                                'wk_payment_moyasar/static/src/js/moyasar_payment.js',
                            ],
                        },
    "pre_init_hook"     :  "pre_init_check",
    'post_init_hook'    : 'post_init_hook',
    'uninstall_hook'    : 'uninstall_hook',
}
