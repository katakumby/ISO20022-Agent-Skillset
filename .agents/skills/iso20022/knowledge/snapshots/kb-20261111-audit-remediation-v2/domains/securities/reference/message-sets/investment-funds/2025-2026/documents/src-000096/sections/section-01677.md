---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.1 OrderReference <OrdrRef>"]
file_pages: [2362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.1 OrderReference <OrdrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2362 to 2362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2362

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       Common <Cmon> [1..1] IdentifierSet 2475
Or       DTI <DTI> [1..1] IdentifierSet 2475
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  2475
         Identification <Id> [1..1] Text 2476
         IdentificationSource <IdSrc> [1..1] ± 2476
     FinancialInstrumentName <FinInstrmNm> [0..1] Text 2476
     RedemptionCompletion <RedCmpltn> [0..1] CodeSet 2476
     FinalConfirmation <FnlConf> [0..1] Indicator 2476
Constraints
• PhysicalDeliveryDetails1Rule
If PhysicalDeliveryIndicator is "false" or "0" (No), then PhysicalDeliveryDetails is not allowed.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'false'
 Or    /PhysicalDeliveryIndicator is equal to value '0'
Following Must be True
    /PhysicalDeliveryDetails Must be absent
• PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'true'
 Or    /PhysicalDeliveryIndicator is equal to value '1'
Following Must be True
    /PhysicalDeliveryDetails Must be present
• PriceDifferenceReasonRule
Any occurrence of InformativePriceDetails/PriceDifferenceReason may not be present.
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in SettlementAmount, if
present.
On Condition
    /RequestedSettlementCurrency is present
 And    /SettlementAmount is present
Following Must be True
    /RequestedSettlementCurrency Must be equal to /SettlementAmount/
attribute::Currency
46.4.5.10.1  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2362 May 2026
```

