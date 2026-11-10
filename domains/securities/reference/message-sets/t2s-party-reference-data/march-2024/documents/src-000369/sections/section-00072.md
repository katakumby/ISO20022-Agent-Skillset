---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.2 Record <Rcrd>", "8.4.2.2.2.1 Address <Adr>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.2.1 Address <Adr>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       RestrictionType <RstrctnTp> [1..1]  108
{Or         Code <Cd> [1..1] Text 108
Or}         Proprietary <Prtry> [1..1] ± 108
       ValidFrom <VldFr> [1..1] DateTime 108
       ValidUntil <VldUntil> [0..1] DateTime 109
Or}   Other <Othr> [1..*]  109
     FieldName <FldNm> [1..1] Text 109
     OldFieldValue <OdFldVal> [1..1] Text 109
     NewFieldValue <NewFldVal> [1..1] Text 109
8.4.2.2.2.1  Address <Adr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address.
Address <Adr> contains the following UpdateLogAddress2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] ± 92
   New <New> [1..1] ± 93
8.4.2.2.2.1.1  Old <Od>
Presence: [1..1]
Definition: Old value before change
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
92 March 2024
```

