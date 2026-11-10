---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.3 Constraints"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.3 Constraints

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         Restriction <Rstrctn> [1..1]  106
           Old <Od> [1..1]  106
             RestrictionType <RstrctnTp> [1..1]  107
{Or               Code <Cd> [1..1] Text 107
Or}               Proprietary <Prtry> [1..1] ± 107
             ValidFrom <VldFr> [1..1] DateTime 107
             ValidUntil <VldUntil> [0..1] DateTime 107
           New <New> [1..1]  107
             RestrictionType <RstrctnTp> [1..1]  108
{Or               Code <Cd> [1..1] Text 108
Or}               Proprietary <Prtry> [1..1] ± 108
             ValidFrom <VldFr> [1..1] DateTime 108
             ValidUntil <VldUntil> [0..1] DateTime 109
Or}         Other <Othr> [1..*]  109
           FieldName <FldNm> [1..1] Text 109
           OldFieldValue <OdFldVal> [1..1] Text 109
           NewFieldValue <NewFldVal> [1..1] Text 109
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 109
   SupplementaryData <SplmtryData> [0..*] ± C4 109
8.3 Constraints
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
82 March 2024
```

