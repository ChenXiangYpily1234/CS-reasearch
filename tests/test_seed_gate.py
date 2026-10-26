import importlib.util
import unittest
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/cs-research/scripts/check_seed_gate.py'

class SeedGateTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.is_file(), 'Installable skill needs a seed gate helper')
        spec = importlib.util.spec_from_file_location('seed_gate', SCRIPT)
        self.gate = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.gate)

    def test_strict_maximize_gate(self):
        self.assertTrue(self.gate.qualifies('0.8001', '0.8000', 'maximize'))
        self.assertFalse(self.gate.qualifies('0.8000', '0.8000', 'maximize'))
        self.assertFalse(self.gate.qualifies('0.7999', '0.8000', 'maximize'))

    def test_minimize_and_threshold(self):
        self.assertTrue(self.gate.qualifies('9', '10', 'minimize', '0.5'))
        self.assertFalse(self.gate.qualifies('9', '10', 'minimize', '1'))
        self.assertFalse(self.gate.qualifies('11', '10', 'minimize'))

    def test_decimal_boundary(self):
        self.assertFalse(self.gate.qualifies('0.3', '0.2', 'maximize', '0.1'))
        self.assertTrue(self.gate.qualifies('0.30001', '0.2', 'maximize', '0.1'))

    def test_invalid_evidence(self):
        for value in ('NaN', 'Infinity', '-Infinity', '', 'unknown', None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.gate.qualifies(value, '0.8', 'maximize')
        with self.assertRaises(ValueError):
            self.gate.qualifies('1', '0', 'sideways')
        with self.assertRaises(ValueError):
            self.gate.qualifies('1', '0', 'maximize', '-1')

class CommandTests(unittest.TestCase):
    def test_cli_returns_decision_without_launching(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--candidate', '0.8',
                                 '--competitor', '0.8', '--direction', 'maximize'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout),
                         {'eligible_seed_42': False, 'decision': 'STOPPED_AFTER_41'})

    def test_cli_rejects_nonfinite_input(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--candidate', 'NaN',
                                 '--competitor', '0.8', '--direction', 'maximize'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')

if __name__ == '__main__':
    unittest.main()
