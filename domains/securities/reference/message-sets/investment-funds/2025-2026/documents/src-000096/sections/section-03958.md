---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.48 Transaction Type", "66.1.48.1 TradeTransactionCondition8Choice", "66.1.48.1.2 Proprietary <Prtry>"]
file_pages: [5255]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.48.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5255 to 5255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5255

```text
Datatype: "TradeTransactionCondition5Code" on page 5378
CodeName Name Definition
XCPN ExCoupon Indicates whether the trade is executed
ex coupon.
CCPN CumCoupon Indicates whether the trade is executed
cum coupon.
66.1.48.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade condition expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
66.1.48.2  SettlementTransactionCondition30Choice
Definition: Choice of format for the settlement transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
66.1.48.2.1  Code <Cd>
Presence: [1..1]
Definition: Settlement condition expressed as a code.
Datatype: "SettlementTransactionCondition11Code" on page 5363
CodeName Name Definition
NOMC NoAutomaticMarketClaim No market claim should be automatically
generated.
66.1.48.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement condition expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5255 May 2026
```

