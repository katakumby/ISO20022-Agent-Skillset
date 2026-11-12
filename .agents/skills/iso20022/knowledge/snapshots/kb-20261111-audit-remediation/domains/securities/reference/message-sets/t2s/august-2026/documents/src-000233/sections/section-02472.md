---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.137 RestrictionType1Code"]
file_pages: [3289, 3290]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.137 RestrictionType1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3289 to 3290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3289

```text
82.2.2.137  RestrictionType1Code
Definition: Specifies the type of restriction.
Type: CodeSet
CodeName Name Definition
SELR Selling Selling restriction.
BUYR Buying Buying restriction.
PLAR Placing Placing restriction.
HOLR Holding Holding restriction.
VOTR Voting Voting restriction.
82.2.2.138  SafekeepingPlace1Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
82.2.2.139  SafekeepingPlace3Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
82.2.2.140  SecuritiesBalanceType11Code
Definition: Specifies the nature of the securities or investment fund balance.
Type: CodeSet
CodeName Name Definition
BLOK Blocked Balance of financial instruments that are
blocked.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3289 August 2026
```

## File page 3290

```text
CodeName Name Definition
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3290 August 2026
```

