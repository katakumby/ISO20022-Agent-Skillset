---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.3 SubBalanceType11Choice"]
file_pages: [2848, 2849]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.3 SubBalanceType11Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2848 to 2849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2848

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification56" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2968
   Issuer <Issr> [1..1] Text 2968
   SchemeName <SchmeNm> [0..1] Text 2968
   Balance <Bal> [1..1] Quantity 2968
82.1.5.3  SubBalanceType11Choice
Definition: Choice of format for the sub-balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2848
Or}   Proprietary <Prtry> [1..1] ± 2850
82.1.5.3.1  Code <Cd>
Presence: [1..1]
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Datatype: "SecuritiesBalanceType12Code" on page 3291
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
Target2-Securities 2848 August 2026
```

## File page 2849

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
Target2-Securities 2849 August 2026
```

