---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.40 SecuritiesBalanceType11Code"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.40 SecuritiesBalanceType11Code

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
CodeName Name Definition
REMS RemoveSecuritiesRestrictionReference Removal of a securities restriction
reference, already present within the
settlement instruction, representing a
securities sub-position to be utilised
within the settlement instruction for the
delivery or receipt of securities.
9.2.2.40  SecuritiesBalanceType11Code
Definition: Specifies the nature of the securities or investment fund balance.
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
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 337 September 2025
```

