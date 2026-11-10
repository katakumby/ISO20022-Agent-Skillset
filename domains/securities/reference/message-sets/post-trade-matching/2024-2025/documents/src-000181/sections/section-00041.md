---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.33 OrderOriginatorEligibility <OrdrOrgtrElgblty>"]
file_pages: [60]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.33 OrderOriginatorEligibility <OrdrOrgtrElgblty>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 60 to 60.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 60

```text
CurrencyToBuyOrSell <CcyToBuyOrSell> contains one of the following elements (see
"CurrencyToBuyOrSell1Choice" on page 330 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 330
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 330
3.4.4.33  OrderOriginatorEligibility <OrdrOrgtrElgblty>
Presence: [0..1]
Definition: Counterparties eligibility as defined by article 24 of the EU MiFID Directive applicable to
transactions executed by investment firms for eligible counterparties.
Datatype: "Eligibility1Code" on page 624
CodeName Name Definition
ELIG EligibleCounterparty Eligible customers are the most
sophisticated level of investor, able to
opt out of some the protections afforded
by conduct of business rules.
RETL RetailClient Retail customers are the least
sophisticated level of investor.
PROF ProfessionalClient Professional customers are, for example,
investment firms, credit institutions,
insurance companies.
3.4.4.34  PositionEffect <PosFct>
Presence: [0..1]
Definition: Indicates whether the resulting position after a trade should be an opening position or closing
position. Used for omnibus accounting - where accounts are held on a gross basis instead of being
netted together.
Datatype: "PositionEffect2Code" on page 637
CodeName Name Definition
OPEN OpenPosition Position after the trade the position
should be open.
CLOS ClosePosition Position after the trade the position
should be closed.
ROLL Rolled Results in a position obtained in a
security previously held, sold and
repurchased.
FIFO Fifo First in, first out. Results in a position
obtained after having sold in priority the
securities bought chronologically.
CLOA CloseAccount Trade relates to a closure of an account.
3.4.4.35  DerivativeCovered <DerivCvrd>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 60 February 2025
```

