---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.14 MarketClientSide <MktClntSd>"]
file_pages: [578]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.14 MarketClientSide <MktClntSd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 578 to 578.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 578

```text
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds
or to sell the indicated currency in order to obtain the necessary currency to fund the transaction.
CurrencyToBuyOrSell <CcyToBuyOrSell> contains one of the following elements (see
"CurrencyToBuyOrSell1Choice" on page 330 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 330
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 330
7.1.27.1.14  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction is for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 283 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 283
Or}   Proprietary <Prtry> [1..1] ± 283
7.1.27.1.15  NettingEligibility <NetgElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
NettingEligibility <NetgElgblty> contains one of the following elements (see
"NettingEligibility4Choice" on page 303 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 303
Or}   Proprietary <Prtry> [1..1] ± 303
7.1.27.1.16  Registration <Regn>
Presence: [0..1]
Definition: Specifies whether registration should occur upon receipt.
Registration <Regn> contains one of the following elements (see "Registration9Choice" on page 378
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 378
Or}   Proprietary <Prtry> [1..1] ± 378
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 578 February 2025
```

