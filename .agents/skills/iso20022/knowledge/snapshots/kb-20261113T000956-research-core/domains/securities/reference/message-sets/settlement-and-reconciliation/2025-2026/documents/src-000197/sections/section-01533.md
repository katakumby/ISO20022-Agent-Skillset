---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.30 Transaction Type", "35.1.30.1 SettlementTransactionCondition42Choice", "35.1.30.1.2 Proprietary <Prtry>"]
file_pages: [2032]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.30.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2032 to 2032.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2032

```text
CodeName Name Definition
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
TRAN Transformation Transaction resulting from a
transformation.
TRIP TripartySegregation Securities are not be delivered but
segregated following triparty collateral
transaction.
UNEX Unexposed Delivery cannot be performed until
money is received.
35.1.30.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.30.2  TradeTransactionCondition5Choice
Definition: Choice of format for the trade transaction condition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2032
Or}   Proprietary <Prtry> [1..1] ± 2033
35.1.30.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade conditions expressed as an ISO 20022 code.
Datatype: "TradeTransactionCondition4Code" on page 2172
CodeName Name Definition
CBNS CumBonus Indicates whether the trade is executed
cum bonus.
XBNS ExBonus Indicates whether the trade is executed
ex bonus.
CCPN CumCoupon Indicates whether the trade is executed
cum coupon.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2032 March 2026
```

