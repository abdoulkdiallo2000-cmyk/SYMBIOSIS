"""Dependency-free validator for the JSON-Schema keywords used by this pack."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def resolve(root:dict,ref:str):
    node=root
    for part in ref.removeprefix('#/').split('/'): node=node[part]
    return node

def validate(value,schema,root,path='$'):
    if '$ref' in schema: return validate(value,resolve(root,schema['$ref']),root,path)
    if 'const' in schema: assert value==schema['const'],(path,'const')
    if 'enum' in schema: assert value in schema['enum'],(path,'enum')
    types=schema.get('type'); types=[types] if isinstance(types,str) else types
    mapping={'object':dict,'array':list,'string':str,'integer':int,'boolean':bool,'null':type(None)}
    if types:
        assert any(isinstance(value,mapping[x]) and not (x=='integer' and isinstance(value,bool)) for x in types),(path,types,type(value))
    if isinstance(value,dict):
        for key in schema.get('required',[]): assert key in value,(path,'missing',key)
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False: assert not (set(value)-set(props)),(path,'additional',set(value)-set(props))
        for key,sub in props.items():
            if key in value: validate(value[key],sub,root,f'{path}.{key}')
    if isinstance(value,list):
        assert len(value)>=schema.get('minItems',0) and len(value)<=schema.get('maxItems',10**12),(path,'items')
        if schema.get('uniqueItems'): assert len({json.dumps(x,sort_keys=True) for x in value})==len(value),(path,'unique')
        if 'items' in schema:
            for i,item in enumerate(value): validate(item,schema['items'],root,f'{path}[{i}]')
    if isinstance(value,str):
        assert len(value)>=schema.get('minLength',0),(path,'minLength')
        if 'pattern' in schema: assert re.search(schema['pattern'],value),(path,'pattern',value)
    if isinstance(value,int) and 'minimum' in schema: assert value>=schema['minimum'],(path,'minimum')

def main():
    pairs={'task_bank_v1.0.json':'task-bank.schema.json','advice_bank_v1.0.json':'advice-bank.schema.json','h9_register_v1.0.json':'h9-register.schema.json','interaction_profiles_v1.0.json':'interaction-profile.schema.json'}
    for data_name,schema_name in pairs.items():
        data=json.loads((ROOT/'data'/data_name).read_text(encoding='utf-8')); schema=json.loads((ROOT/'schemas'/schema_name).read_text(encoding='utf-8')); validate(data,schema,schema); print('PASS JSON Schema contract:',data_name)

if __name__=='__main__': main()
