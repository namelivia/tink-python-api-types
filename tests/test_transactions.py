from tink_python_api_types.transaction import (
    TransactionsPage,
    Transaction,
    Descriptions,
    Dates,
    Types,
    Categories,
    PFM,
)
from tink_python_api_types.common import Amount


class TestTransactions:
    def test_transactions_page_is_buildable(self):
        page = TransactionsPage(
            **{
                "next_page_token": "string",
                "transactions": [
                    {
                        "account_id": "4a2945d1481c4f4b98ab1b135afd96c0",
                        "amount": {
                            "currency_code": "GBP",
                            "value": {"scale": "1", "unscaled_value": "-1300"},
                        },
                        "booked_date_time": "2020-12-15T09:25:12Z",
                        "categories": {
                            "pfm": {
                                "id": "d8f37f7d19c240abb4ef5d5dbebae4ef",
                                "name": "",
                            }
                        },
                        "dates": {"booked": "2020-12-15", "value": "2020-12-15"},
                        "descriptions": {
                            "display": "Tesco",
                            "original": "TESCO STORES 3297",
                        },
                        "id": "d8f37f7d19c240abb4ef5d5dbebae4ef",
                        "identifiers": {
                            "provider_transaction_id": "500015d3-acf3-48cc-9918-9e53738d3692"
                        },
                        "merchant_information": {
                            "merchant_category_code": "string",
                            "merchant_name": "string",
                        },
                        "provider_mutability": "MUTABILITY_UNDEFINED",
                        "reference": "string",
                        "status": "BOOKED",
                        "transaction_date_time": "string",
                        "types": {
                            "financial_institution_type_code": "DEB",
                            "type": "DEFAULT",
                        },
                        "value_date_time": "2020-12-15T09:25:12Z",
                    }
                ],
            }
        )
        assert type(page) is TransactionsPage
        assert type(page.transactions[0]) is Transaction
        assert type(page.transactions[0].amount) is Amount
        assert type(page.transactions[0].descriptions) is Descriptions
        assert type(page.transactions[0].dates) is Dates
        assert type(page.transactions[0].types) is Types
        assert type(page.transactions[0].categories) is Categories
        assert type(page.transactions[0].categories.pfm) is PFM

    def test_transactions_page_is_buildable_different_format(self):
        page = TransactionsPage(
            **{
                "next_page_token": "string",
                "transactions": [
                    {
                        "id": "d8f37f7d19c240abb4ef5d5dbebae4ef",
                        "account_id": "4a2945d1481c4f4b98ab1b135afd96c0",
                        "amount": {
                            "currency_code": "GBP",
                            "value": {"scale": "1", "unscaled_value": "-1300"},
                        },
                        "categories": {
                            "pfm": {
                                "id": "d8f37f7d19c240abb4ef5d5dbebae4ef",
                                "name": "",
                            }
                        },
                        "dates": {"booked": "2020-12-15"},
                        "descriptions": {
                            "display": "Tesco",
                            "original": "TESCO STORES 3297",
                        },
                        "provider_mutability": "MUTABILITY_UNDEFINED",
                        "status": "BOOKED",
                        "types": {
                            "type": "DEFAULT",
                        },
                    }
                ],
            }
        )
        assert type(page) is TransactionsPage
        assert type(page.transactions[0]) is Transaction
        assert type(page.transactions[0].amount) is Amount
        assert type(page.transactions[0].descriptions) is Descriptions
        assert type(page.transactions[0].dates) is Dates
        assert type(page.transactions[0].types) is Types
        assert type(page.transactions[0].categories) is Categories
        assert type(page.transactions[0].categories.pfm) is PFM
