"""Official GLSim consensus engine integration; mocks, not hosted Full Consensus."""
import json
import runpy
from pathlib import Path
from glsim.engine import SimEngine
from glsim.state import StateStore, TxStatus
from glsim.consensus import run_consensus

HELPERS = runpy.run_path('tests/direct/test_protocol.py')


def test_five_validator_lifecycle():
    engine=SimEngine(StateStore())
    engine.activate()
    try:
        engine.vm.warp(HELPERS['epoch'](100))
        a='0x'+'11'*20;b='0x'+'22'*20
        addr,_=engine.deploy('contracts/claimbond.py',sender=a)
        def call(method,args=None,sender=a,value=0):
            engine.vm.value=value
            engine.vm.origin=bytes.fromhex(sender[2:])
            return engine.call_method(addr,method,args or [],sender=sender)
        cid=call('create_claim',[json.dumps(HELPERS['terms']()),json.dumps(HELPERS['package'](['acceptance','primary','secondary']))],value=10)
        claim=json.loads(call('get_claim',[cid]))
        call('challenge',[cid,claim['terms_hash'],json.dumps(HELPERS['package'](['challenger']))],sender=b,value=10)
        call('lock_evidence',[cid])
        claim=json.loads(call('get_claim',[cid]))
        for side in ['claimant','challenger']:
            for src in claim[side+'_manifest']:
                engine.vm.mock_web(src['url'],dict(status=200,body=Path('fixtures/live_claim/'+src['url'].split('/')[-1]).read_text()))
        engine.vm.mock_llm('You adjudicate',json.dumps(HELPERS['verdict']()))
        result=run_consensus(engine,lambda:(call('adjudicate',[cid]),b''),num_validators=5,max_rotations=1)
        assert result.status==TxStatus.FINALIZED and result.error is None
        assert result.votes==['agree']*5
        call('settle',[cid])
        from genlayer import Address
        assert call('get_credit',[Address(a)])==20
        final=json.loads(call('get_claim',[cid]))
        assert final['state']=='SETTLED' and final['result']['verdict']['outcome']=='SUPPORTED'
        assert len(final['decision_hash'])==64
        accounting=json.loads(call('get_accounting'))
        assert accounting['deposits']==accounting['credits']==20 and accounting['escrow']==0
    finally:
        engine.deactivate()
