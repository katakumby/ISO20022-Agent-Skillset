---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.3 SecuritiesTransactionType47Choice", "35.1.16.3.2 Proprietary <Prtry>"]
file_pages: [1535]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.3.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1535 to 1535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1535

```text
CodeName Name Definition
CORP CorporateAction Relates to a corporate action.
CLAI MarketClaim Relates to a market claim.
AUTO AutoCollateralisation Relates to an auto-collateralisation
movement.
SWIF SwitchFrom Transaction is a change of an
investment from one sub-fund to another
sub-fund (redemption-leg).
SWIT SwitchTo Transaction is a change of an
investment from one sub-fund to another
sub-fund (subscription-leg).
CONV DepositoryReceiptConversion Relates to a depository receipt
conversion.
ETFT ExchangeTradedFunds Relates to an ETF creation or
redemption.
ISSU Issuance Relates to the issuance of a security
such as an equity or a depositary
receipt.
SLRE LendingReallocation Internal reallocation of a holding on loan
from one safekeeping account to
another.
INSP MoveOfStock Relates to a movement of shares into or
out of a pooled account.
SBBK SellBuyBack Relates to a sell buy back transaction.
REDI Withdrawal Relates to the withdrawal of specified
amounts from specified subaccounts.
35.1.16.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.4  ClassificationType32Choice
Definition: Choice of format for the classification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1535 March 2026
```

