---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.20 Price", "35.1.20.7 PriceRateOrAmountOrUnknown2Choice", "35.1.20.7.3 UnknownIndicator <UknwnInd>"]
file_pages: [1714]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.20.7.3 UnknownIndicator <UknwnInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1714 to 1714.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1714

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
35.1.20.7.3  UnknownIndicator <UknwnInd>
Presence: [1..1]
Definition: Indicates whether the market price is unknown.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.20.8  TypeOfPrice28Choice
Definition: Choice of format for the type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1714
Or}   Proprietary <Prtry> [1..1] ± 1715
35.1.20.8.1  Code <Cd>
Presence: [1..1]
Definition: Type of price expressed as an ISO 20022 code.
Datatype: "TypeOfPrice11Code" on page 2174
CodeName Name Definition
BIDE Bid Price is the calculated bid price of a
dual-priced fund (offer-bid prices), that
is, the selling price of the units for the
investor.
OFFR Offer Price is the calculated offer price of a
dual-priced investment fund (offer-bid
prices), that is, the buying price of the
units for an investor.
NAVL NetAssetValue Price is the net asset value per unit that
is used either as a transacting price for a
single-priced investment fund class, or
as a notional price for the calculation of
other prices.
CREA Creation Price is the calculated creation price of a
dual-priced investment fund (creation-
cancellation prices) and the highest
possible buying price of the units before
the initial charge. The actual buying or
offer price, which includes charges, will
be higher.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1714 March 2026
```

