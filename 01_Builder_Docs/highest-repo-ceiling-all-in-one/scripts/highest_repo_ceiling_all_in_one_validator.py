#!/usr/bin/env python3
import sys, zipfile, re, json
from pathlib import Path
from xml.etree import ElementTree as ET

REQUIRED = [
'00_START_HERE','01_REPO_CEILING_CHARTER','02_SOURCE_TRUTH_INDEX','03_CURRENT_REPO_STATE','04_HIGHEST_REPO_STATE_MODEL','05_GAP_MASTER_LEDGER','06_SOURCE_TRUTH_LAYER','07_WORKBOOK_COMMAND_LAYER','08_GITHUB_REPO_TEMPLATE_LAYER','09_SUPABASE_RUNTIME_LEDGER','10_VERCEL_RUNTIME_CRON_LAYER','11_CODEX_BUILD_LOOP','12_CONNECTOR_GOVERNANCE_LAYER','13_RELEASE_OPERATION_LAYER','14_BUSINESS_FACTORY_LAYER','15_ENVIRONMENT_VARIABLES','16_SECURITY_SECRET_READINESS','17_VALIDATION_TESTING_LAYER','18_RECEIPTS_PROOF_INDEX','19_BLOCKERS_WORKAROUNDS','20_ROLLBACK_RECOVERY_PLAN','21_RELEASE_GATE','22_RECURSIVE_AUDIT_LOG','23_SCORECARD','24_CODEX_INSTALL_HANDOFF','25_BASE44_AGENT_HANDOFF','26_SECOND_GPT_AUDIT_PROMPT','27_FINAL_OPERATOR_HANDOFF','99_VALIDATION_LISTS',
'28_VISUAL_PARITY_CHARTER','29_APPROVED_MOCKUP_TRUTH','30_SCREENSHOT_CAPTURE_MATRIX','31_VISUAL_DRIFT_LEDGER','32_UI_PARITY_SCORECARD','33_PLAYWRIGHT_VISUAL_RECEIPTS','34_CODEX_UI_FIX_LOOP','35_BASE44_VISUAL_LOCK_HANDOFF','36_VISUAL_RELEASE_GATE','37_VISUAL_ROLLBACK_PLAN']

MUST_CONTAIN = {
 '24_CODEX_INSTALL_HANDOFF':['codex/install-highest-repo-ceiling-workbook','01_Builder_Docs/highest-repo-ceiling-one-shot','Do not push to main','Do not deploy production','Do not expose secrets','Do not mark production-ready'],
 '25_BASE44_AGENT_HANDOFF':['Base44','Codex','operator approval','final output'],
 '26_SECOND_GPT_AUDIT_PROMPT':['independent','Do not trust summary claims','VERIFIED','INFERRED','COULD NOT VERIFY','BLOCKERS','WORKAROUNDS','NEXT ACTIONS'],
 '28_VISUAL_PARITY_CHARTER':['Verify final UI matches approved visual source truth','pass threshold','receipts'],
 '30_SCREENSHOT_CAPTURE_MATRIX':['desktop_1440','tablet_768','mobile_390','Playwright screenshot'],
 '31_VISUAL_DRIFT_LEDGER':['P0','P1','P2','Release blocker'],
 '32_UI_PARITY_SCORECARD':['layout/section order','colors/brand','responsive behavior','TOTAL'],
 '36_VISUAL_RELEASE_GATE':['approved_source_truth_loaded','screenshots_captured','no_open_p0_p1_drift','operator_visual_approval'],
 '37_VISUAL_ROLLBACK_PLAN':['rollback_action','receipt_required']
}


def shared_strings(z):
    try:
        xml = z.read('xl/sharedStrings.xml')
    except KeyError:
        return []
    root = ET.fromstring(xml)
    ns = {'a':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    vals=[]
    for si in root.findall('a:si', ns):
        texts=[]
        for t in si.findall('.//a:t', ns):
            texts.append(t.text or '')
        vals.append(''.join(texts))
    return vals


def sheet_names(z):
    root = ET.fromstring(z.read('xl/workbook.xml'))
    ns = {'a':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    return [s.attrib['name'] for s in root.findall('a:sheets/a:sheet', ns)]


def all_text(z):
    ss = shared_strings(z)
    texts = list(ss)
    for name in z.namelist():
        if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
            xml = z.read(name).decode('utf-8', errors='ignore')
            for tag in ['t','v']:
                for m in re.findall(r'<(?:\w+:)?%s[^>]*>(.*?)</(?:\w+:)?%s>' % (tag, tag), xml):
                    texts.append(re.sub('<.*?>','',m))
    return '\n'.join(texts)


def main(path):
    p = Path(path)
    if not p.exists():
        print('FAIL: workbook missing')
        return 2
    with zipfile.ZipFile(p,'r') as z:
        names = sheet_names(z)
        missing = [s for s in REQUIRED if s not in names]
        txt = all_text(z)
        missing_terms = {}
        for sheet, terms in MUST_CONTAIN.items():
            absent = [t for t in terms if t.lower() not in txt.lower()]
            if absent:
                missing_terms[sheet]=absent
    if missing or missing_terms:
        print('HIGHEST REPO CEILING ALL-IN-ONE VALIDATION: FAIL')
        print('required_sheets=%d' % len(REQUIRED))
        print('missing_sheets=' + json.dumps(missing))
        print('missing_terms=' + json.dumps(missing_terms, indent=2))
        return 1
    print('HIGHEST REPO CEILING ALL-IN-ONE VALIDATION: PASS')
    print('required_sheets=%d' % len(REQUIRED))
    print('engineering_ceiling=present')
    print('visual_parity_layer=present')
    print('screenshot_matrix=present')
    print('visual_release_gate=present')
    print('production_readiness=locked_unless_proven')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else 'AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx'))
