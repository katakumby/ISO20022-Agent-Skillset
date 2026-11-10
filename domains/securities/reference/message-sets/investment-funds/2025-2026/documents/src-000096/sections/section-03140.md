---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.5 AdditionalBalanceInformation2", "66.1.5.5.1 Quantity <Qty>"]
file_pages: [4368]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.5.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4368 to 4368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4368

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4368
{Or   SubBalanceType <SubBalTp> [1..1] CodeSet 4368
Or}   ExtendedSubBalanceType <XtndedSubBalTp> [1..1] Text 4369
66.1.5.5.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of securities in the sub-balance.
Quantity <Qty> contains one of the following elements (see "SubBalanceQuantity1Choice" on
page 4398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4398
Or   QuantityAsDSS <QtyAsDSS> [1..1] ± 4399
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1]  4399
     Quantity <Qty> [1..1] ± 4399
     AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 4400
66.1.5.5.2  SubBalanceType <SubBalTp>
Presence: [1..1]
Warning   Either SubBalanceType or ExtendedSubBalanceType must be present, but not both.
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Datatype: "SecuritiesBalanceType2Code" on page 5361
CodeName Name Definition
CLEN TaxExempt Balance of tax-exempt securities.
DIRT NonTaxExempt Balance of taxable securities.
NOMI Registered Balance of securities that are registered
(in the name of a nominee or of the
beneficial owner).
OTHR Unclassified Balance of securities that is unclassified,
ie, is not identified with one of the
existing sub-balance types.
SPOS StreetPosition Balance of securities that remain
registered in the name of the prior
beneficial owner of securities.
UNRG Unregistered Balance of securities that could not be
registered due to foreign ownership
limitation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4368 May 2026
```

