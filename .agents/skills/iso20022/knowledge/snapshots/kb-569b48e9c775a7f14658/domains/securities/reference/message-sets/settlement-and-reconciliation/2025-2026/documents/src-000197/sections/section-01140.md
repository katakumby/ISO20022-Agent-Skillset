---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.48 SecuritiesTransactionType43Choice", "35.1.16.48.2 Proprietary <Prtry>"]
file_pages: [1587]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.48.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1587 to 1587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1587

```text
35.1.16.48.2  Proprietary <Prtry>
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
35.1.16.49  TradeOriginator3Choice
Definition: Choice of format for the trading capacity of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1587
Or}   Proprietary <Prtry> [1..1] ± 1588
35.1.16.49.1  Code <Cd>
Presence: [1..1]
Definition: Trading party capacity expressed as an ISO 20022 code.
Datatype: "OriginatorRole2Code" on page 2088
CodeName Name Definition
SINT SystematicInternaliser Firms which, on an organised, frequent
and systematic basis deal on their own
account by executing client orders
outside a regulated market or a
Multilateral Trading Facility. SI's will have
the obligation to provide, and make
public, a definite bid and offer quote for
liquid securities. They act as
"mini"exchanges.
MLTF MultilateralTradingFacility Multilateral system which brings together
multiple third-party buying and selling
interests in financial instruments in a way
that results in a contract.
RMKT RegulatedMarket Market on which financial instruments
can be traded according to rules defined
by the stock exchange.
MKTM MarketMaker Dealer or specialist that is trading for
their own account in the OTC market.
Market makers are expected to maintain
an orderly market by being available to
buy or sell.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1587 March 2026
```

