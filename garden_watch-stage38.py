# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: GardenWatch
import unittest
from datetime import datetime

class TestEdgeCases(unittest.TestCase):
    def test_empty_plant_name(self):
        from gardenwatch.garden import Garden
        g = Garden()
        with self.assertRaises(ValueError):
            g.add_plant("", "tomato")

    def test_empty_note(self):
        from gardenwatch.garden import Garden
        g = Garden()
        g.add_plant("tomato")
        with self.assertRaises(ValueError):
            g.add_note("tomato", "")

    def test_invalid_date_format(self):
        from gardenwatch.garden import Garden
        g = Garden()
        g.add_plant("tomato")
        with self.assertRaises(ValueError):
            g.add_note("tomato", "2025-13-01", "Watered")

    def test_duplicate_date_note_same_day(self):
        from gardenwatch.garden import Garden
        g = Garden()
        g.add_plant("tomato")
        g.add_note("tomato", "2025-01-01", "Watered")
        with self.assertRaises(ValueError):
            g.add_note("tomato", "2025-01-01", "Watered")

    def test_empty_plants_list(self):
        from gardenwatch.garden import Garden
        g = Garden()
        with self.assertRaises(ValueError):
            g.get_plants()

    def test_note_after_removal(self):
        from gardenwatch.garden import Garden
        g = Garden()
        g.add_plant("tomato")
        g.add_note("tomato", "2025-01-01", "Watered")
        g.remove_note("tomato", "2025-01-01")
        with self.assertRaises(ValueError):
            g.add_note("tomato", "2025-01-01", "Watered")

if __name__ == '__main__':
    unittest.main()
