---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Settlement instruction query"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.026.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P323-P324; XML P328-P353"}, {"source_id": "src-000374", "locator": "Word file/printed pages28"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000309", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.026.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["march-2026"]
---

# Settlement instruction query

[src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P323-P324; XML P328-P353.

**P323** Description

**P324** In this example a T2S Actor has sent to T2S a Settlement Instruction Query requesting all settlement instructions where the securities account is ‘1000000123’ and the settlement quantity is greater than or equal to 50000 units and less than or equal to 60000 units (as per a range of valid quantity values).

```xml
<SctiesSttlmTxQry>
    <QryDef>
      <QryTp>INST</QryTp>
      <SchCrit>
        <SfkpgAcct>
          <Id>1000000123</Id>
        </SfkpgAcct>
        <SttlmQty>
          <Qty>
            <Unit>
              <FrToQty>
                <FrQty>
                  <Bdry>50000</Bdry>
                  <Incl>true</Incl>
                </FrQty>
                <ToQty>
                  <Bdry>60000</Bdry>
                  <Incl>true</Incl>
                </ToQty>
              </FrToQty> 
            </Unit>
          </Qty>
        </SttlmQty>
      </SchCrit>
    </QryDef>
 </SctiesSttlmTxQry>
```

## Review and validation

All source example pages compared2026-11-09: [28](../../../../../assets/src-000374/source-page-renders/word-page-28.png). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
