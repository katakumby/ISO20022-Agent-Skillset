---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.141 SecuritiesBalanceType12Code"]
file_pages: [3291, 3292]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.141 SecuritiesBalanceType12Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3291 to 3292.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3291

```text
CodeName Name Definition
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
LODE PendingOnLoanDelivery Balance of financial instruments that are
pending delivery in relation to a lending
transaction.
82.2.2.141  SecuritiesBalanceType12Code
Definition: Specifies the nature of the securities or investment fund balance.
Type: CodeSet
CodeName Name Definition
BLOK Blocked Balance of financial instruments that are
blocked.
AWAS AvailableWithNoAdditionalStatus Balance of financial instruments that are
freely available with no specific
additional status.
BLCA BlockedCorporateAction Balance of financial instrument blocked
following a corporate action, including
proxy activities.
BLOT BlockedTrading Balance of financial instruments that are
blocked for trading.
BLOV BlockedAuthenticity Balance of financial instruments that are
blocked for verification of authenticity.
BORR Borrowed Balance of financial instruments that
have been borrowed from another party.
BODE PendingBorrowedDelivery Balance of financial instruments that are
pending delivery in relation to a borrow
transaction.
BORE PendingBorrowedReceipt Balance of financial instruments that are
pending receipt in relation to a borrow
transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3291 August 2026
```

## File page 3292

```text
CodeName Name Definition
COLI CollateralIn Balance of securities that belong to a
third party and that are held for the
purpose of collateralisation.
COLO CollateralOut Balance of securities that belong to the
safekeeping account indicated within this
message, and are deposited with a third
party for the purpose of collateralisation.
LOAN OnLoan Loan for consumption.
LODE PendingOnLoanDelivery Balance of financial instruments that are
pending delivery in relation to a lending
transaction.
LORE PendingOnLoanReceipt Balance of financial instruments that are
pending receipt in relation to a lending
transaction.
MARG DerivativesMargin Account is used when financing is by the
broker/dealer.
PECA PendingCorporateActionReceipt Balance of financial instrument pending
receipt following a corporate action.
PEDA PendingCorporateActionDelivery Balance of financial instrument pending
delivery following a corporate action.
PEND PendingDelivery Processing has not been completed.
PENR PendingReceipt The instruction is pending receipt of
securities, for example, from a purchase,
loan etc.
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
WDOC WaitingDocumentation Financial instrument is unavailable due
to missing or incomplete documentation
pertaining to the account, or due to a
missing or incomplete order.
BTRA BeingTransferred Financial instrument is unavailable as a
result of a transfer order, pending
movement in the shareholders' register.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3292 August 2026
```

