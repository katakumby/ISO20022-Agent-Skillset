---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.2 SettlementSystemMethod4Choice", "7.1.19.2.1 Code <Cd>"]
file_pages: [287]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.2.1 Code <Cd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 287 to 287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 287

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 287
Or}   Proprietary <Prtry> [1..1] ± 287
7.1.19.2.1  Code <Cd>
Presence: [1..1]
Definition: Settlement system expressed as an ISO 20022 code.
Datatype: "SettlementSystemMethod1Code" on page 647
CodeName Name Definition
NSET Default Settle through the default settlement
system/method. If there is a standing
instruction in place for settlement
through the alternate settlement system/
method, then this standing instruction is
to be ignored.
YSET Alternative Settle through the alternate settlement
system/method. If there is a standing
instruction in place for settlement
through the default settlement system/
method, then this standing instruction is
to be ignored.
7.1.19.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement system expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.3  ClassificationType32Choice
Definition: Choice of format for the classification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 287
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 288
7.1.19.3.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 287 February 2025
```

