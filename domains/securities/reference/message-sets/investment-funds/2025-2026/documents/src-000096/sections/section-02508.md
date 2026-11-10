---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.1 MasterReference <MstrRef>"]
file_pages: [3536]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3536 to 3536.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3536

```text
Constraints
• FinancialInstrumentQuantity1Rule
If SubscriptionLegDetails/FinancialInstrumentQuantityChoice is not present, then
RedemptionLegDetails/FinancialInstrumentQuantityChoice is mandatory in each occurrence of
RedemptionLegDetails.
If SubscriptionLegDetails/FinancialInstrumentQuantityChoice is present, then it must be present in
each occurrence of SubscriptionLegDetails.
• InvestmentAccountDetailsRule
Either InvestmentAccountDetails or all occurrences of SubscriptionLegDetails/
InvestmentAccountDetails and RedemptionLegDetails/InvestmentAccountDetails must be present,
but not both.
Either InvestmentAccountDetails or all occurrences of SubscriptionLegDetails/
InvestmentAccountDetails and RedemptionLegDetails/InvestmentAccountDetails must be present,
but not both.
• OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or a single occurrence of
RedemptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility or a single occurrence of
SubscriptionLegDetails/InvestmentAccountDetails/OrderOriginatorEligibility should be only present.
53.4.5.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
53.4.5.2  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Definition: Date and time the order is placed by the investor or its agent.
Datatype: "ISODateTime" on page 5388
53.4.5.3  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
PlaceOfTrade <PlcOfTrad> contains one of the following elements (see
"PlaceOfTradeIdentification4Choice" on page 4808 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C12 4809
Or   Exchange <Xchg> [1..1] IdentifierSet 4809
Or   Party <Pty> [1..1] IdentifierSet C4 4809
Or}   OverTheCounter <OverTheCntr> [1..1] Text 4809
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3536 May 2026
```

