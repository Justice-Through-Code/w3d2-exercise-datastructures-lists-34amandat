'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

import io
from unittest import mock, TestCase

from ripple_media import box_office_data, create_employee_email_address


class TestRippleMediaLists(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_box_office_data(self, mock_stdout):
        box_office_data()

        self.assertEqual(
            "<class 'list'>\n50\nFalse\nTrue\n50\n100\nStar Wars: Episode I - The Phantom Menace\n['Star Wars: Episode I - The Phantom Menace', 'The Sixth Sense', 'Austin Powers: The Spy Who Shagged Me', 'Toy Story 2', 'The Matrix', 'Tarzan', 'Big Daddy', 'The Mummy', 'Runaway Bride', 'The Blair Witch Project']\n",
            mock_stdout.getvalue()
        )

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_create_employee_email_address(self, mock_stdout):
        create_employee_email_address()

        self.assertEqual(
            "daffy duck\n['daffy', 'duck']\ndaffy.duck\ndaffy.duck@ripplemedia.com\n",
            mock_stdout.getvalue()
        )
