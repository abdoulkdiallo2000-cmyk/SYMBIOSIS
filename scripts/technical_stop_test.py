"""Pre-pilot STOP SYMBIOSIS technical test harness.
This simulates session-state transitions only. It does not test a real network stack.
A real implementation must repeat the same assertions against the deployed interface/provider boundary.
"""
from dataclasses import dataclass
import random

@dataclass
class Session:
    active: bool=True
    paused: bool=False
    revoked: bool=False
    transmissions_after_ack: int=0
    def refuse(self): return 'human_decision_preserved'
    def pause(self): self.paused=True; return 'paused'
    def resume(self):
        if self.revoked: raise RuntimeError('revoked')
        self.paused=False
    def stop(self):
        self.active=False; self.paused=True; self.revoked=True
        return 'ack'
    def transmit(self):
        if self.revoked:
            self.transmissions_after_ack += 1
            raise RuntimeError('blocked_after_stop')
        if self.paused: raise RuntimeError('blocked_while_paused')
        return 'sent'

def run(n=100,seed=20260914):
    rng=random.Random(seed)
    failures=[]
    for i in range(n):
        s=Session()
        for _ in range(rng.randint(0,5)): s.transmit()
        s.stop()
        try: s.transmit()
        except RuntimeError: pass
        else: failures.append((i,'post-stop transmission allowed'))
        if s.transmissions_after_ack!=1: failures.append((i,'unexpected counter'))
        if not s.revoked or s.active: failures.append((i,'state not revoked'))
    return failures

if __name__=='__main__':
    f=run();
    if f:
        print('FAIL',f[:10]); raise SystemExit(1)
    print('PASS: 100/100 simulated revocation scenarios blocked post-STOP transmission attempts.')
