import odoo
import logging
_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    @odoo.http.route('/hello', auth='public')
    def foo_handler(self):
        return "Welcome to Real Estate Management"