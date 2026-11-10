---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.3 Amount Range", "9.1.3.1 ImpliedCurrencyAmountRange1Choice", "9.1.3.1.5 NotEqualAmount <NEQAmt>"]
file_pages: [197, 198]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.3.1.5 NotEqualAmount <NEQAmt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 197 to 198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 197

```text
9.1.3.1.5  NotEqualAmount <NEQAmt>
Presence: [1..1]
Definition: Value that an amount must not match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 313
9.1.3.2  AmountRangeBoundary1
Definition: Limit for an amount range.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 197
   Included <Incl> [1..1] Indicator 197
9.1.3.2.1  BoundaryAmount <BdryAmt>
Presence: [1..1]
Definition: Amount value of the range limit.
Datatype: "ImpliedCurrencyAndAmount" on page 313
9.1.3.2.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary amount is included in the range of amount values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
9.1.4 Balance
9.1.4.1  SecuritiesBalanceType6Choice
Definition: Choice of format for the balance type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 197
Or}   Proprietary <Prtry> [1..1] ± 199
9.1.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Sub-balance expressed as an ISO 20022 code.
Datatype: "SecuritiesBalanceType11Code" on page 337
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 197 September 2025
```

## File page 198

```text
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
DRAW Drawn Settlement transactions relates to drawn
securities.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 198 September 2025
```

