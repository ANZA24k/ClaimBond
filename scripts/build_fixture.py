"""Build authenticated Studio inputs from the published safe fixture."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

SHA='9e9ecbc5572f5d6746f07a0a6ae8792303fec176'
ROOT=Path(__file__).resolve().parents[1]

def manifest(names):
    result=[]
    for name in names:
        path=ROOT/'fixtures/live_claim'/f'{name}.md'
        body=path.read_bytes()
        result.append(dict(url=f'https://raw.githubusercontent.com/ANZA24k/ClaimBond/{SHA}/fixtures/live_claim/{name}.md',sha256=hashlib.sha256(body).hexdigest(),bytes=len(body),media_type='text/markdown'))
    return dict(sources=sorted(result,key=lambda x:x['url']))

if __name__=='__main__':
    ts=int(datetime.now(timezone.utc).timestamp())
    t=dict(claim='Fixture R-17 satisfied all mandatory release checks.',category='SOFTWARE',question='According to the locked policy and authenticated records, did Fixture R-17 satisfy all mandatory release checks?',support='The primary record establishes C1, C2 and C3 passed for R-17; optional checks do not block acceptance.',refutation='An authenticated primary record establishes a failed mandatory check for R-17.',materiality='A failure for R-16 or optional B1 is not a material refutation. Credible conflicting mandatory R-17 records warrant CONFLICTED.',scope='Only the fictional release R-17 and the locked records.',time_scope='The published commit-pinned fixture test period.',context='Harmless fictional software acceptance demonstration.',criteria=[dict(id='MANDATORY',text='Did all mandatory C1, C2 and C3 checks pass for build R-17 under the locked acceptance policy?')],source_policy='PINNED_GITHUB_TEXT_V1',max_sources=4,max_bytes=16384,challenge_deadline=ts+3600,adjudication_deadline=ts+7200,challenger_bond=10**15)
    print(json.dumps(dict(terms=t,claimant_manifest=manifest(['acceptance','primary','secondary']),challenger_manifest=manifest(['challenger']),value_wei=10**15),indent=2))
