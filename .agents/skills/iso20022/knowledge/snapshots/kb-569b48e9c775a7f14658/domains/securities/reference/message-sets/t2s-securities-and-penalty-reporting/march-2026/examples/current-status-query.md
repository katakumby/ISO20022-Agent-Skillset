---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Current status query"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.026.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P357-P358; XML P362-P381"}, {"source_id": "src-000374", "locator": "Word file/printed pages29"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000309", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.026.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["march-2026"]
---

# Current status query

[src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P357-P358; XML P362-P381.

**P357** Description 

**P358** In this example a T2S actor has sent to T2S a Settlement Instruction Current Status Query requesting all high priority “High [0003]” settlement instructions for securities account ‘1000000123’ where the settlement status is pending.

```xml
<SctiesSttlmTxQry>
    <QryDef>
      <QryTp>STTS</QryTp>
      <SchCrit>
        <Sts>
          <Tp>
            <SttlmSts>
              <Cd>PEND</Cd>
            </SttlmSts>
          </Tp>
        </Sts>
        <Prty>
          <Nmrc>0003</Nmrc>
        </Prty>
        <SfkpgAcct>
          <Id>1000000123</Id>
        </SfkpgAcct>
      </SchCrit>
    </QryDef>
</SctiesSttlmTxQry>
```

## Review and validation

All source example pages compared2026-11-09: [29](../../../../../../../evidence/omitted/ee91000c612ec4a5d041e4e9.md). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
