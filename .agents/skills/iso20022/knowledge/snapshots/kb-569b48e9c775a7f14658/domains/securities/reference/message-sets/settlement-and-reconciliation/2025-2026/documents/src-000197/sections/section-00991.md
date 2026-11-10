---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.16 SecuritiesBalanceType6Choice"]
file_pages: [1427, 1428]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.16 SecuritiesBalanceType6Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1427 to 1428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1427

```text
Quantity <Qty> contains one of the following elements (see "SubBalanceQuantity8Choice" on
page 1730 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1730
Or   Proprietary <Prtry> [1..1] ± 1731
Or}   QuantityAndAvailability <QtyAndAvlbty> [1..1] ± 1731
35.1.4.16  SecuritiesBalanceType6Choice
Definition: Choice of format for the balance type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1427
Or}   Proprietary <Prtry> [1..1] ± 1429
35.1.4.16.1  Code <Cd>
Presence: [1..1]
Definition: Sub-balance expressed as an ISO 20022 code.
Datatype: "SecuritiesBalanceType11Code" on page 2137
CodeName Name Definition
BLOK Blocked Balance of financial instruments that are
blocked.
AWAS AvailableWithNoAdditionalStatus Balance of financial instruments that are
freely available with no specific
additional status.
AVAI Available Balance of financial instruments that are
available.
BLCA BlockedCorporateAction Balance of financial instrument blocked
following a corporate action, including
proxy activities.
BLOT BlockedTrading Balance of financial instruments that are
blocked for trading.
BLOV BlockedAuthenticity Balance of financial instruments that are
blocked for verification of authenticity.
BORR Borrowed Balance of financial instruments that
have been borrowed from another party.
COLI CollateralIn Balance of securities that belong to a
third party and that are held for the
purpose of collateralisation.
COLO CollateralOut Balance of securities that belong to the
safekeeping account indicated within this
message, and are deposited with a third
party for the purpose of collateralisation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1427 March 2026
```

## File page 1428

```text
CodeName Name Definition
COLA EligibleForCollateralPurposes Balance of securities that are eligible for
use for collateral purposes.
LOAN OnLoan Loan for consumption.
MARG DerivativesMargin Account is used when financing is by the
broker/dealer.
PECA PendingCorporateActionReceipt Balance of financial instrument pending
receipt following a corporate action.
PEDA PendingCorporateActionDelivery Balance of financial instrument pending
delivery following a corporate action.
PLED Pledged Balance of securities that belong to and
is kept in the safekeeping account
indicated within this message, and that
are pledged.
REGO OutForRegistration Balance of financial instruments
currently being processed by the
institution responsible for registering the
new beneficial owner (or nominee).
RSTR Restricted Balance of financial instruments that
may only be sold under certain
conditions or require legal documents.
OTHR Unclassified Other. See Narrative.
TRAN InTransshipment Transaction has been generated due to
transformation following a corporate
action.
DRAW Drawn Settlement transactions relates to drawn
securities.
CLEN TaxExempt Tax-exempt financial instruments are to
be settled.
DIRT NonTaxExempt Taxable financial instruments are to be
settled.
NOMI Registered Balance of financial instruments that are
registered (in nominee name or in the
name of the beneficial owner).
SPOS StreetPosition Balance of financial instruments that
remain registered in the name of the
prior beneficial owner.
UNRG Unregistered Balance of securities that could not be
registered due to foreign ownership
limitation.
ISSU Issued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has been received.
QUAS QuasiIssued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has not yet been
received.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1428 March 2026
```

