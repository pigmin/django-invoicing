from django.conf import settings


class TaxationPolicy(object):
    """
    Abstract class for defining taxation policies.
    Taxation policy is a way to handle what tax rate should be put on the invoice items by default if not set any.
    It depends on customer billing data.

    Custom taxation policy should implement only method ``get_default_tax(vat_id, country_code)``.
    This method should return a percent value of tax that should be added to the invoice item
    or 0 if tax is not applicable.
    """

    @classmethod
    def get_default_tax(cls):
        """
        Gets default tax rate. Simple returns ``settings.TAX``

        :return: Decimal()
        """
        return getattr(settings, 'INVOICING_TAX_RATE')

    @classmethod
    def get_supplier_country_code(cls):
        """
        Gets suppliers country. Simply returns ``settings.TAX_COUNTRY``

        :return: unicode
        """
        supplier = getattr(settings, 'INVOICING_SUPPLIER')
        return supplier['country_code']

    @classmethod
    def get_tax_rate(cls, vat_id, country_code):
        """
        Methods

        :param vat_id: customer vat id
        :param country_code:  customer country in ISO 2-letters format
        :return: Decimal()
        """
        raise NotImplementedError('Method get_tax_rate should be implemented.')
