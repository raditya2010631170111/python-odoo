# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import float_compare, float_is_zero
from collections import defaultdict
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.stock.models.stock_rule import ProcurementException



class SaleOrder(models.Model):
    _inherit = "sale.order"


    mo_origin_ids = fields.One2many("mrp.production",'so_id','MO Origin')

    mrp_production_count = fields.Integer(
        "Count of MO generated",
        compute='_compute_mrp_production_count',
        groups='mrp.group_mrp_user')

    def _compute_mrp_production_count(self):
        for sale in self:
            sale.mrp_production_count = len(sale.procurement_group_id.stock_move_ids.created_production_id.procurement_group_id.mrp_production_ids)
            len_mo = len(sale.mo_origin_ids)
            if not sale.mrp_production_count and len_mo:
                sale.mrp_production_count = len_mo



    def action_view_mrp_production(self):
        self.ensure_one()
        mrp_production_ids = self.procurement_group_id.stock_move_ids.created_production_id.procurement_group_id.mrp_production_ids.ids
        if not mrp_production_ids:
            mrp_production_ids = self.mo_origin_ids.ids
        action = {
            'res_model': 'mrp.production',
            'type': 'ir.actions.act_window',
        }
        if len(mrp_production_ids) == 1:
            action.update({
                'view_mode': 'form',
                'res_id': mrp_production_ids[0],
            })
        else:
            action.update({
                'name': _("Manufacturing Orders Generated by %s", self.name),
                'domain': [('id', 'in', mrp_production_ids)],
                'view_mode': 'tree,form',
            })
        return action
