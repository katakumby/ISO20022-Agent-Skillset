---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [1945]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# Continuation at file page 1945

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1945 to 1945.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1945

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 2051
Or       CTA <CTA> [1..1] IdentifierSet 2051
Or       QUICK <QUICK> [1..1] IdentifierSet 2051
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 2051
Or       Dutch <Dtch> [1..1] IdentifierSet 2052
Or       Valoren <Vlrn> [1..1] IdentifierSet 2052
Or       Sicovam <SCVM> [1..1] IdentifierSet 2052
Or       Belgian <Belgn> [1..1] IdentifierSet 2052
Or       Common <Cmon> [1..1] IdentifierSet 2052
Or       DTI <DTI> [1..1] IdentifierSet 2052
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  2052
         Identification <Id> [1..1] Text 2053
         IdentificationSource <IdSrc> [1..1] ± 2053
     FinancialInstrumentName <FinInstrmNm> [0..1] Text 2053
     RedemptionCompletion <RedCmpltn> [0..1] CodeSet 2053
     FinalConfirmation <FnlConf> [0..1] Indicator 2053
Constraints
• OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or one or more occurrences of
RelatedPartyDetails/OrderOriginatorEligibility may be present, but not both.
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
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1945 May 2026
```

