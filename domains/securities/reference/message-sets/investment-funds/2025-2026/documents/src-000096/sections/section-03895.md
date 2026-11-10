---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.14 PartiallySettledStatus10", "66.1.45.14.1 Reason <Rsn>", "66.1.45.14.1.2 Proprietary <Prtry>"]
file_pages: [5186]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.14.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5186 to 5186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5186

```text
CodeName Name Definition
GAT1 GatedOneNAV Redemption has been gated, all
settlement will be done at the same
price.
UCPS UnitsCashPartiallySettled Units and cash are both partially settled.
UPST UnitsPartiallySettled Units are partially settled.
66.1.45.14.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Partially settled reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.14.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the partially settled reason.
Datatype: "Max350Text" on page 5403
66.1.45.15  AcceptedStatusReason1Choice
Definition: Choice of formats for an accepted status reason code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5186
Or}   Proprietary <Prtry> [1..1] ± 5187
66.1.45.15.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status expressed as a code.
Datatype: "AcceptedStatusReason1Code" on page 5270
CodeName Name Definition
PLAC PlaceNotAllowed Status of the account modification
instruction is accepted but modification
of the account data will not be carried
out for the place.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5186 May 2026
```

