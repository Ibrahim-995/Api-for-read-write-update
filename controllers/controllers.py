# # -*- coding: utf-8 -*-
# from odoo import http
# import logging
# _logger = logging.getLogger(__name__)
#
# class AaaApiDevelop(http.Controller):
#     @http.route('/aaa/api/develop', auth='public', website=False, type='http', methods=['GET'])
#     def index(self, **kw):
#         _logger.info(kw)
#         sum = int(kw['a']) + int(kw['b'])
#         sub = int(kw['a']) - int(kw['b'])
#         mul = int(kw['a']) * int(kw['b'])
#         div = int(kw['a']) / int(kw['b'])
#
#
#         # value1 = str(sum)
#         # value2 = str(sub)
#         # value3 = str(mul)
#         # value4 = str(div)
#
#
#         # return "Sum is: " + value1 + "\nSub is: " + value2 + "\nMul is: " + value3 + "\nDiv is: " + value4
#





from odoo import http


# Api for 5 type data in contacs

class AaaApi1Develop(http.Controller):
    @http.route('/aaa/api1/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        contacts = http.request.env['res.partner'].sudo().search([])

        contact_list = []
        for contact in contacts:
            contact_list.append({
                'name':contact.name,
                'email':contact.email,
                'address':contact.street,
                'phone':contact.phone,
                'website':contact.website,
            })

        return contact_list

# Api for 5 type data in crm(my activities)

class AaaApi2Develop(http.Controller):
    @http.route('/aaa/api2/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        crm = http.request.env['crm.lead'].sudo().search([])

        contact_list2 = []
        for contact in crm:
            contact_list2.append({
                'customer':contact.partner_id,
                'email':contact.email_from,
                'phone':contact.phone,
                'salseperson':contact.user_id,
                'team':contact.team_id,
            })

        return contact_list2

# Api for 5 type data in crm(extra info)


class AaaApi3Develop(http.Controller):
    @http.route('/aaa/api3/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        crmextra = http.request.env['crm.lead'].sudo().search([])

        contact_list3 = []
        for contact in crmextra:
            contact_list3.append({
                'company name':contact.partner_name,
                'address':contact.street,
                'campaign':contact.campaign_id,
                'medium':contact.medium_id,
                'source':contact.source_id,


            })

        return contact_list3



#Api for adding data

class AaaAddDataApiDevelop(http.Controller):
    @http.route('/aaa/apiadd/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        http.request.env['res.partner'].sudo().create({'name':kw['name']})

        return kw

#other way

class AaaAddotherDataApiDevelop(http.Controller):
    @http.route('/aaa/apiaddother/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        http.request.env['res.partner'].sudo().create(kw)

        return kw

#Api for update data

class AaaupdateDataApiDevelop(http.Controller):
    @http.route('/aaa/apiupdate/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
       user = http.request.env['res.partner'].sudo().search([('id','=',kw['id'])])
       user.write({
           'name':kw['name'],
           'email':kw['email'],
           'phone': kw['phone'],
           'vat':kw['vat'],
           'function': kw['position'],
           'website': kw['website'],
           'mobile': kw['mobile'],

       })

       return kw

    