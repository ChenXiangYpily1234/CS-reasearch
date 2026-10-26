import re
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/cs-research'

class PackageTests(unittest.TestCase):
    def test_skill_discovery_and_ui(self):
        entry = SKILL / 'SKILL.md'
        self.assertTrue(entry.is_file(), 'Missing SKILL.md')
        front = yaml.safe_load(entry.read_text().split('---', 2)[1])
        self.assertEqual(front['name'], SKILL.name)
        self.assertTrue(front['description'].startswith('Use when'))
        ui = yaml.safe_load((SKILL / 'agents/openai.yaml').read_text())
        self.assertIn('$cs-research', ui['interface']['default_prompt'])

    def test_frozen_contract(self):
        path = SKILL / 'config/workflow.yaml'
        self.assertTrue(path.is_file(), 'Missing workflow YAML')
        c = yaml.safe_load(path.read_text())
        self.assertEqual(c['literature']['paper_count'], {'min': 20, 'max': 30})
        self.assertEqual(c['experiment']['seeds'], [41, 42])
        self.assertEqual(c['experiment']['confirmation_seed'], 43)
        inference = c['experiment']['inference']
        self.assertTrue(inference['seed_equals_training_seed'])
        self.assertTrue(inference['paired_seed_across_methods'])
        self.assertEqual(inference['deterministic_inference_seed_status'], 'N/A')
        self.assertEqual(inference['seed_unavailable_status'], 'UNCONTROLLED')
        self.assertEqual(c['experiment']['training_datasets'], 1)
        self.assertEqual(c['experiment']['test_datasets'], 2)
        self.assertEqual(c['methods']['count'], 12)
        self.assertEqual(c['methods']['web_generated'], 11)
        self.assertEqual(c['seed_gate']['comparison'], 'strict')
        self.assertEqual(c['supervision']['unavailable_status'], 'BLOCKED_MODEL')
        self.assertIsNone(c['experiment']['batch']['effective'])
        self.assertIsNone(c['project']['research_direction'])
        self.assertEqual(c['project']['status'], 'NOT_RUN')
        self.assertTrue(all(x['status'] == 'NOT_RUN' for x in c['stages']))
        self.assertEqual(len({x['id'] for x in c['stages']}), 8)
        self.assertEqual(c['skills']['story']['name'], 'paper-storycraft')
        self.assertEqual(c['skills']['editable_ppt']['name'], 'image-to-editable-ppt')
        self.assertEqual(c['skills']['presentation']['name'], 'presentation-skill')

    def test_inference_seed_policy_is_in_prompts_and_freeze(self):
        for rel in ['prompts/chatgpt-ideation.md', 'prompts/research-workflow.md',
                    'templates/experiment-freeze.md', 'references/workflow.md',
                    'templates/method-card.md', 'SKILL.md']:
            content = (SKILL / rel).read_text()
            self.assertIn('推理', content, rel)
            self.assertIn('seed', content, rel)

    def test_behavior_scenarios_are_parseable(self):
        data = yaml.safe_load((ROOT / 'tests/scenarios.yaml').read_text())
        self.assertEqual(len(data['cases']), 5)
        self.assertEqual(len({c['id'] for c in data['cases']}), 5)
        self.assertTrue(all(c['request'] and c['expected'] for c in data['cases']))

    def test_skill_dependencies_have_direct_links(self):
        c = yaml.safe_load((SKILL / 'config/workflow.yaml').read_text())
        entry = (SKILL / 'SKILL.md').read_text()
        for dependency in c['skills'].values():
            self.assertIn('](' + dependency['url'] + ')', entry)
        for f in SKILL.rglob('*.md'):
            self.assertNotIn('persistent', f.read_text().lower())

    def test_portable_references(self):
        self.assertTrue((SKILL / 'SKILL.md').exists())
        files = list(SKILL.rglob('*.md'))
        for f in files:
            text = f.read_text()
            self.assertNotIn('/Users/', text)
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if '://' not in link and not link.startswith('#'):
                    target = (f.parent / link.split('#')[0]).resolve()
                    self.assertTrue(target.is_relative_to(SKILL.resolve()), link)
                    self.assertTrue(target.exists(), f'{f}: {link}')

if __name__ == '__main__':
    unittest.main()
