"""
usmart_sdk tests.
"""

import unittest
from usmart_sdk.usmart import USMART


class TestUSMART(unittest.TestCase):
    """
    Test usmart_sdk's usmart bject.
    """

    def setUp(self):
        self.usmartIdOfFirstElement = 'AVvm5Awld_J1iIwX7HJx'
        self.usmartIdOfSecondElement = 'AVvm5Awld_J1iIwX7HJ0'
        self.treetag702usmartId = "AVvm5Ea2d_J1iIwX7Maa"
        pass

    def test_init(self):
        """
        Instantiate object without auth details
        """
        usmart = USMART()

    def test_auth_init(self):
        """
        Instantiate object with broken auth details
        """
        with self.assertRaises(Exception) as context:
            usmart = USMART({})

        self.assertTrue('Auth requires keyId' in context.exception)

    def test_auth_init_with_keyId(self):
        """
        Instantiate object with broken auth details (keyId)
        """
        with self.assertRaises(Exception) as context:
            usmart = USMART({
                "keyId": "<<SAMPLE_ID>>"
            })

        self.assertTrue(('Auth requires keySecret' in str(context.exception)))

    def test_auth_init(self):
        """
        Instantiate object with broken auth details (keyId)
        """
        USMART({
            "keyId": "<<SAMPLE_ID>>",
            "keySecret": "<<KEY_SECRET>>"
        })

    def test_sample_request(self):
        """
        Test Sample request
        """
        organisation = '28ccd497-7cad-4470-bd17-721d5cbbd6ef'
        resource = 'cd580a25-9918-4bba-a699-fa640a0cc44a'
        usmart = USMART()

        response = usmart.request(
            organisation,
            resource
        )
        self.assertTrue(
            len(response.json()),
            10
        )

    def test_sample_request_with_limit(self):
        """
        Test Sample request
        """
        organisation = '28ccd497-7cad-4470-bd17-721d5cbbd6ef'
        resource = 'cd580a25-9918-4bba-a699-fa640a0cc44a'
        usmart = USMART()

        response = usmart.request(
            organisation,
            resource,
            query={
                "limit": 1
            }
        )
        self.assertTrue(
            len(response.json()) == 1
        )
        self.assertTrue(
            response.json()[0]["usmart_id"] == self.usmartIdOfFirstElement
        )

    def test_sample_request_with_limit_and_offset(self):
        """
        Test Sample request
        """
        organisation = '28ccd497-7cad-4470-bd17-721d5cbbd6ef'
        resource = 'cd580a25-9918-4bba-a699-fa640a0cc44a'
        usmart = USMART()

        response = usmart.request(
            organisation,
            resource,
            query={
                "limit": 1,
                "offset": 1
            }
        )
        self.assertTrue(
            len(response.json()),
            1
        )
        self.assertTrue(
            response.json()[0]["usmart_id"] == self.usmartIdOfSecondElement
        )

    def test_sample_request_with_equals(self):
        """
        Test Sample request
        """
        organisation = '28ccd497-7cad-4470-bd17-721d5cbbd6ef'
        resource = 'cd580a25-9918-4bba-a699-fa640a0cc44a'
        usmart = USMART()

        response = usmart.request(
            organisation,
            resource,
            query={
                "equals": [{
                  "key": "TREELOCATIONX",
                  "value": "333285.78"
                }]
            }
        )
        self.assertTrue(
            len(response.json()),
            1
        )
        self.assertTrue(
            response.json()[0]["usmart_id"] == self.treetag702usmartId
        )
