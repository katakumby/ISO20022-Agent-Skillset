---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.200 SafekeepingPlace2Code"]
file_pages: [5359, 5360]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.200 SafekeepingPlace2Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5359 to 5360.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5359

```text
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
66.2.2.200  SafekeepingPlace2Code
Definition: Specifies the type of place of safekeeping.
Type: CodeSet
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
ALLP AllPlaces All places of safekeeping where the
financial instrument is held.
66.2.2.201  SecuritiesAccountPurposeType1Code
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
66.2.2.202  SecuritiesBalanceType1Code
Definition: Specifies the nature of the securities or investment fund balance.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5359 May 2026
```

## File page 5360

```text
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5360 May 2026
```

