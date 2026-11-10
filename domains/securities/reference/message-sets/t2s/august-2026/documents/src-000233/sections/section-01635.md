---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.1 Address <Adr>"]
file_pages: [2269]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.1 Address <Adr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2269 to 2269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2269

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       RestrictionType <RstrctnTp> [1..1]  2285
{Or         Code <Cd> [1..1] Text 2285
Or}         Proprietary <Prtry> [1..1] ± 2285
       ValidFrom <VldFr> [1..1] DateTime 2285
       ValidUntil <VldUntil> [0..1] DateTime 2286
Or}   Other <Othr> [1..*]  2286
     FieldName <FldNm> [1..1] Text 2286
     OldFieldValue <OdFldVal> [1..1] Text 2286
     NewFieldValue <NewFldVal> [1..1] Text 2286
58.4.2.2.2.1  Address <Adr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address.
Address <Adr> contains the following UpdateLogAddress2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] ± 2269
   New <New> [1..1] ± 2270
58.4.2.2.2.1.1  Old <Od>
Presence: [1..1]
Definition: Old value before change
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2269 August 2026
```

