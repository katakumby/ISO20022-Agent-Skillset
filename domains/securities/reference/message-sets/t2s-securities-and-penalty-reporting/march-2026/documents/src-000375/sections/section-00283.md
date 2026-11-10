---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous"]
file_pages: [360]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18 Miscellaneous

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 360 to 360.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 360

```text
7.1.18 Miscellaneous
7.1.18.1  ExposureType25Choice
Definition: Choice of format for the exposure information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 360
Or}   Proprietary <Prtry> [1..1] ± 361
7.1.18.1.1  Code <Cd>
Presence: [1..1]
Definition: Collateral movement exposure type expressed as an ISO 20022 code.
Datatype: "ExposureType15Code" on page 504
CodeName Name Definition
BFWD BondForward Any securities traded out beyond 3 days
which include treasury notes, Japanese
Governement Bonds (JGBs) and Gilts.
PAYM CashSettlement In support of any type of cash
settlement.
CCPC CCPCollateral Collateral covering the initial margin
requirements for OTC trades cleared
through a CCP.
COMM Commodities Any good exchanged during commerce,
which includes goods traded on a
commodity exchange.
CRDS CreditDefaultSwap Swap designed to transfer the credit
exposure of fixed income products
between parties.
CRTL CreditLine Opening of a credit line before trading.
CRSP CreditSupport Cash lending/borrowing; letter of credit;
signing of master agreement.
CCIR CrossCurrencyIRS Cross currency agreement between two
parties (known as counterparties) where
one stream of future interest payments is
exchanged for another based on a
specified principal amount.
CRPR CrossProduct Combination of various types of trades.
EQPT EquityOption Trading of equity option (also known as
stock options).
EXTD ExchangeTradedDerivatives Trading of exchanged traded derivatives
in general.
EQUS EquitySwap Equity swap trades where the return of
an equity is exchanged for either a fixed
or a floating rate of interest.
EXPT ExoticOption Trading of exotic option, for example, a
non standard option.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 360 March 2026
```

