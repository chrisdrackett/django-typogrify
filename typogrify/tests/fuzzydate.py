from datetime import datetime, timedelta

from django.test import TestCase

from typogrify.templatetags.typogrify_tags import fuzzydate

class TestFuzzyDate(TestCase):
    def test_returns_yesterday(self):
        yesterday = datetime.now() - timedelta(hours=24)
        self.assertEquals(fuzzydate(yesterday), "yesterday")

        two_days_ago = datetime.now() - timedelta(hours=48)
        self.assertNotEquals(fuzzydate(two_days_ago), "yesterday")

    def test_returns_today(self):
        today = datetime.now()
        self.assertEquals(fuzzydate(today), "today")

    def test_returns_tomorrow(self):
        tomorrow = datetime.now() + timedelta(hours=24)
        self.assertEquals(fuzzydate(tomorrow), "tomorrow")

    def test_formats_current_year(self):
        now = datetime.now()
        testdate = datetime.strptime("%s/10/10" % now.year, "%Y/%m/%d")
        
        expected = "October 10th"
        self.assertEquals(fuzzydate(testdate), expected)

    def test_formats_other_years(self):
        testdate = datetime.strptime("1984/10/10", "%Y/%m/%d")
        
        expected = "October 10th, 1984"
        self.assertEquals(fuzzydate(testdate), expected)
