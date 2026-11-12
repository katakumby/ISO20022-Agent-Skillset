---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.3 Constraints"]
file_pages: [2259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
topic_continuations: [{"constraint_ids": ["C4"], "until_heading": "58.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 2260, "topic": "58.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-01632.md"}]
---

# 58.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2259 to 2259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 58.3 Constraints topic continues in [Constraints continuation C4 (file p2260)](section-01632.md#file-page-2260). Read the text before **58.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 2259

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         Restriction <Rstrctn> [1..1]  2283
           Old <Od> [1..1]  2283
             RestrictionType <RstrctnTp> [1..1]  2284
{Or               Code <Cd> [1..1] Text 2284
Or}               Proprietary <Prtry> [1..1] ± 2284
             ValidFrom <VldFr> [1..1] DateTime 2284
             ValidUntil <VldUntil> [0..1] DateTime 2284
           New <New> [1..1]  2284
             RestrictionType <RstrctnTp> [1..1]  2285
{Or               Code <Cd> [1..1] Text 2285
Or}               Proprietary <Prtry> [1..1] ± 2285
             ValidFrom <VldFr> [1..1] DateTime 2285
             ValidUntil <VldUntil> [0..1] DateTime 2286
Or}         Other <Othr> [1..*]  2286
           FieldName <FldNm> [1..1] Text 2286
           OldFieldValue <OdFldVal> [1..1] Text 2286
           NewFieldValue <NewFldVal> [1..1] Text 2286
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 2286
   SupplementaryData <SplmtryData> [0..*] ± C4 2286
58.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2259 August 2026
```

