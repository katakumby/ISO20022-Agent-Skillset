---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.21 SettlementSystemMethod <SttlmSysMtd>"]
file_pages: [580]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.21 SettlementSystemMethod <SttlmSysMtd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 580 to 580.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 580

```text
7.1.27.1.21  SettlementSystemMethod <SttlmSysMtd>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
SettlementSystemMethod <SttlmSysMtd> contains one of the following elements (see
"SettlementSystemMethod4Choice" on page 286 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 287
Or}   Proprietary <Prtry> [1..1] ± 287
7.1.27.1.22  TaxCapacity <TaxCpcty>
Presence: [0..1]
Definition: Tax role capacity of the instructing party.
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 320 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 321
Or}   Proprietary <Prtry> [1..1] ± 321
7.1.27.1.23  StampDutyIndicator <StmpDtyInd>
Presence: [0..1]
Definition: Indicates whether the settlement amount includes the stamp duty amount.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.27.1.24  StampDutyTaxBasis <StmpDtyTaxBsis>
Presence: [0..1]
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 580 February 2025
```

