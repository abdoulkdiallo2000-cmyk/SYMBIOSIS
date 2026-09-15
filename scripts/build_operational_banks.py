from __future__ import annotations

import json
from pathlib import Path

from task_bank.family_a import GENERATORS as A
from task_bank.family_b import GENERATORS as B
from task_bank.family_c import GENERATORS as C
from task_bank.family_d import GENERATORS as D

ROOT=Path(__file__).resolve().parents[1]


def write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def main() -> None:
    generators={**A,**B,**C,**D}
    packages=[generators[p](f) for p in sorted(generators) for f in range(1,7)]
    write(ROOT/"data/task_bank_v1.0.json",{"schema_version":"1.0","bank_version":"1.0-prepilot","packages":packages})
    print(f"Wrote {len(packages)} operational packages ({sum(len(p['trials']) for p in packages)} trials).")


if __name__=="__main__": main()
