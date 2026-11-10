---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.46 TradeType4Choice", "7.1.19.46.2 Proprietary <Prtry>"]
file_pages: [356]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.46.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 356 to 356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
CodeName Name Definition
AGEN Agency Trade in which an agent intermediates
between a buyer and a seller.
GUAR GuaranteedClose Trade which is guaranteed to be
finalized.
EMTR EmployeeTradeReporting Transaction relates to employee trade
reporting.
ISSU Issuance Relates to the issuance of a security
such as an equity or a depositary
receipt.
BOST BondStart The trade is a Bond start.
BOEN BondEnd The trade is a Bond end.
LABO LendingAndBorrowing Indicates that the trade is a Lending and
borrowing.
BORE BondRepricing The trade is a Bond repricing.
OFIT OfferingIssuingTrade Indicates that the trade is a Offering
issue trade.
BOSU BondSubstitution The trade is a Bond substitution.
FBBT FutureBuyBackTrade The security will be bought back in the
future.
OPTN Options Indicates that the trade is a Option
contract trade.
FUOP FuturesOption Indicates that the trade is a Futures
option contract trade.
FUTR Futures Indicates that the trade is a Futures
contract trade.
7.1.19.46.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Third party reporting information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.47  BeneficialOwnership4Choice
Definition: Choice of format for the beneficial ownership.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 356 February 2025
```

