---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.3 Charge26", "66.1.8.3.1 Type <Tp>"]
file_pages: [4451]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.3.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4451 to 4451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4451

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  4451
{Or     Code <Cd> [1..1] CodeSet 4451
Or}     Proprietary <Prtry> [1..1] ± 4452
   ChargeApplied <ChrgApld> [1..1]  4452
{Or     Amount <Amt> [1..1] Amount C1 4452
Or}     Rate <Rate> [1..1] Rate 4452
66.1.8.3.1  Type <Tp>
Presence: [1..1]
Definition: Type of charge.
Type <Tp> contains one of the following ChargeType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4451
Or}   Proprietary <Prtry> [1..1] ± 4452
66.1.8.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of charge expressed as a code.
Datatype: "ChargeType12Code" on page 5283
CodeName Name Definition
BEND BackEndLoad Sales charge paid by the investor when
redeeming an investment such as an
investment fund.
DISC Discount Charge that has been reduced from the
standard initial charge levied by a fund,
eg, during a launch period or as
negotiated by a funds supermarket /
discount broker.
FEND FrontEndLoad Sales charge paid immediately by the
investor when subscribing to an
investment such as an investment fund.
POST PostageCharge Charge paid for the postage.
REGF RegulatoryFee Fee charged by a regulatory authority,
eg, Securities and Exchange fees.
SHIP ShippingCharge Charge for shipping, including the
insurance of securities.
SPCN SpecialConcessions Charges, drawdown, or other reduction
from or in addition to the deal price.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4451 May 2026
```

