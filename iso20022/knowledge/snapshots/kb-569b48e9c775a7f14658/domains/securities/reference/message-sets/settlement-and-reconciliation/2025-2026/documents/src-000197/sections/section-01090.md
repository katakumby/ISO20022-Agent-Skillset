---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.1 ExposureType25Choice", "35.1.16.1.1 Code <Cd>"]
file_pages: [1530]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1530 to 1530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1530

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1530
Or}   Proprietary <Prtry> [1..1] ± 1531
35.1.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Collateral movement exposure type expressed as an ISO 20022 code.
Datatype: "ExposureType15Code" on page 2063
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
FIXI FixedIncome Trading of fixed income instruments.
FORX ForeignExchange FX trades in general.
FORW ForwardForeignExchange Forward FX trades.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1530 March 2026
```

