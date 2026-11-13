---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.1 AmendmentIndicator <AmdmntInd>"]
file_pages: [2805]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.1 AmendmentIndicator <AmdmntInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2805 to 2805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2805

```text
Constraints
• BulkCashSettlementDetailsRule
Either IndividualExecutionDetails/CashSettlementDetails or BulkCashSettlementDetails may be
present, but not both.
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences of
IndividualExecutionDetails/SettlementAmount.
• SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualExecutionDetails/
SettlementAmount must be the same in all occurrences of IndividualExecutionDetails.
49.4.5.1  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicates whether the confirmation is an amendment of a previous confirmation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
49.4.5.2  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
49.4.5.3  PlaceOfTrade <PlcOfTrad>
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
49.4.5.4  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Definition: Date and time at which the order was placed by the investor or its agent.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2805 May 2026
```

