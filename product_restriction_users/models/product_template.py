# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Mruthul Raj(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import fields, models


class ProductTemplate(models.Model):
    """Inherit the product category for restricted the users for
     particular products"""
    _inherit = 'product.template'

    restrict_user_ids = fields.Many2many('res.users',
                                         help="Restrict the users for "
                                              "particular products")
    is_product = fields.Boolean(default=True, string='Product Restriction',
                                help="Enable product restriction")
    is_category = fields.Boolean(default=True, string='Category Restriction',
                                 help="Enable category restriction")
