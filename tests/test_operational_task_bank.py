import subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class OperationalBankTests(unittest.TestCase):
    def test_primary_validator(self): subprocess.run([sys.executable,str(ROOT/'scripts/validate_task_bank.py')],check=True)
    def test_independent_truth_audit(self): subprocess.run([sys.executable,str(ROOT/'scripts/audit_reference_truths.py')],check=True)
    def test_independent_ablation_audit(self): subprocess.run([sys.executable,str(ROOT/'scripts/audit_ablation_truths.py')],check=True)
    def test_generated_bank_is_reproducible(self):
        before=(ROOT/'data/task_bank_v1.0.json').read_bytes(); subprocess.run([sys.executable,str(ROOT/'scripts/build_operational_banks.py')],check=True); self.assertEqual(before,(ROOT/'data/task_bank_v1.0.json').read_bytes())

if __name__=='__main__': unittest.main()
