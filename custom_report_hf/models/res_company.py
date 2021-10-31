""" init object """
import logging

from odoo import fields, models

LOGGER = logging.getLogger(__name__)


class ResCompany(models.Model):
    """ init object  res.company"""
    _inherit = 'res.company'

    footer_logo = fields.Binary(string="Report Footer Logo")
    header_logo = fields.Binary(string="Report Header Logo")

