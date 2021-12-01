from .connector import PsConnector, PsCustomers, PsOrders, PsProduct


def save_raw_data_factory(ps_entity: PsConnector):
    ps_entity.resources()
    ps_entity.save_resources()
    return ps_entity


def get_raw_orders():
    save_raw_data_factory(PsOrders())


def get_raw_customers():
    save_raw_data_factory(PsCustomers())


def get_raw_products():
    save_raw_data_factory(PsProduct())
