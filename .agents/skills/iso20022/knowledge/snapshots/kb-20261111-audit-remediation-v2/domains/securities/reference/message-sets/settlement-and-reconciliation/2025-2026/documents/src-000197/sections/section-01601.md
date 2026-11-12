---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.122 SafekeepingPlace1Code"]
file_pages: [2137, 2138]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.122 SafekeepingPlace1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2137 to 2138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2137

```text
35.2.2.122  SafekeepingPlace1Code
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
35.2.2.123  SafekeepingPlace3Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
35.2.2.124  SecuritiesAccountPurposeType1Code
Definition: Specifies the purpose of the securities account.
Type: CodeSet
CodeName Name Definition
MARG Margin Account is used when financing is done
by the broker.
SHOR ShortSale Account is used for short sale orders.
ABRD Abroad Account is located in a financial
institution outside the country where the
transaction is taking place.
CEND Centralised Account and all its related positions are
held in one location.
DVPA CashDVP Account is used for settlement upon
delivery, or a collection on a delivery
basis.
PHYS Physical Account is used for physical domestic
safekeeping.
35.2.2.125  SecuritiesBalanceType11Code
Definition: Specifies the nature of the securities or investment fund balance.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2137 March 2026
```

## File page 2138

```text
Type: CodeSet
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2138 March 2026
```

