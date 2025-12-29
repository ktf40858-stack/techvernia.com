#!/usr/bin/env python3
import sys,io,re
if sys.platform=='win32':sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools=['beamery','eightfold-ai','fetcher','findem','harver','hirevue','humanly','paradox-olivia','phenom','pymetrics','seekout','sense','textio','workable-ai']
with open('GenuisNet.ai/js/crowdstrike-i18n.js','r',encoding='utf-8') as f:
    template=f.read()

for tool in tools:
    name=tool.replace('-',' ').title()
    content=template
    content=re.sub(r'// CROWDSTRIKE I18N',f'// {tool.upper().replace("-"," ")} I18N',content)
    content=re.sub(r'const crowdstrikeTranslations',f'const {tool.replace("-","")}Translations',content)
    content=re.sub(r'crowdstrike',tool,content)
    content=re.sub(r'CrowdStrike Falcon',name,content)
    content=re.sub(r'CrowdStrike',name,content)
    content=re.sub(r'endpoint protection platform','HR recruiting platform',content)
    content=re.sub(r'cybersecurity','HR',content,flags=re.IGNORECASE)
    with open(f'GenuisNet.ai/js/{tool}-i18n.js','w',encoding='utf-8') as f:
        f.write(content)
    print(f'✓ {tool}')
print('\n✅ 14 fichiers complets générés')
