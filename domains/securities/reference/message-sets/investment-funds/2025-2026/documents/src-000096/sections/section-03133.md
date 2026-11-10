---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.3 SubBalanceInformation2", "66.1.5.3.1 Quantity <Qty>"]
file_pages: [4360, 4361]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.3.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4360 to 4361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4360

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4360
{Or   SubBalanceType <SubBalTp> [1..1] CodeSet 4360
Or}   ExtendedSubBalanceType <XtndedSubBalTp> [1..1] Text 4362
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4362
66.1.5.3.1  Quantity <Qty>
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
66.1.5.3.2  SubBalanceType <SubBalTp>
Presence: [1..1]
Warning   Either SubBalanceType or ExtendedSubBalanceType must be present, but not both.
Definition: Reason for the sub-balance.
Datatype: "SecuritiesBalanceType1Code" on page 5359
CodeName Name Definition
BLOK Blocked Balance of securities that are blocked or
frozen. A financial instrument may be
unavailable due to external
circumstances such as a court order,
death of beneficiary or account owner, or
bankruptcy.
BORR Borrowed Balance of securities that have been
borrowed from another party.
COLI CollateralIn Balance of securities that belong to a
third party and that are held for the
purpose of collateralisation.
COLO CollateralOut Balance of securities that belong to the
safekeeping account indicated within this
message, and are deposited with a third
party for the purpose of collateralisation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4360 May 2026
```

## File page 4361

```text
CodeName Name Definition
LOAN OnLoan Balance of securities that have been
loaned to a third party.
MARG DerivativesMargin Balance of securities that are used as
collateral for derivatives.
PDMT PendingDeliveryMatchedBalance Balance of securities pending delivery
that have been matched. This is only
applicable in a CSD to participant
communication.
PRMT PendingReceiptMatchedBalance Balance of securities pending receipt
that have been matched. This is only
applicable in a CSD to participant
communication.
PRUM PendingReceiptUnmatchedBalance Balance of securities pending receipt
that are unmatched. This is only
applicable in a CSD to participant
communication.
PECA PendingCorporateAction Balance of securities, before ex-date,
that are involved in a corporate action
(CA). Securities blocked due to a CA, for
example, proxi, in escrow, are to be
identified in the BLOK sub-balance.
PEND PendingDelivery Balance of securities that are pending
delivery.
PENR PendingReceipt Balance of securities that are pending
receipt.
PLED Pledged Balance of securities that are pledged,
for example, a financial instrument is
unavailable because it has been used or
given as a guarantee.
PDUM PendingDeliveryUnmatchedBalance Balance of securities pending delivery
that are unmatched. This is only
applicable in a CSD to participant
communication.
REGO OutForRegistration Balance of securities currently being
processed by the institution responsible
for registering the new beneficial owner
(or nominee) of securities after a
transaction has settled.
RSTR Restricted Balance of securities that may only be
sold under certain conditions or require
legal documents.
OTHR Unclassified Balance of securities that is unclassified,
ie, is not identified with one of the
existing sub-balance types.
TRAN InTransshipment Balance of physical securities that are in
transshipment, eg, in the process of
being transferred from one depository or
agent to another.
DRAW Drawn Balance of securities that are drawn for
redemption.
WDOC WaitingDocumentation Financial instrument is unavailable due
to missing or incomplete documentation
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4361 May 2026
```

