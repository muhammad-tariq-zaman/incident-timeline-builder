import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestTimeline(unittest.TestCase):
    def test_sorted_with_gaps(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "ev.csv")
            open(p, "w").write("timestamp,description,actor\n"
                               "2026-10-26T10:15:00,Resolved,ali\n"
                               "2026-10-26T10:00:00,Outage reported,bob\n")
            tl = main.build(p)
            self.assertEqual(tl[0]["description"], "Outage reported")
            self.assertIsNone(tl[0]["gap_minutes"])
            self.assertEqual(tl[1]["gap_minutes"], 15.0)


if __name__ == "__main__":
    unittest.main()
