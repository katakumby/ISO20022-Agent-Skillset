---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.1 LegIdentification <LegId>"]
file_pages: [3863]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.1 LegIdentification <LegId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3863 to 3863.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3863

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 3926
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 3926
Or       CTA <CTA> [1..1] IdentifierSet 3926
Or       QUICK <QUICK> [1..1] IdentifierSet 3926
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 3926
Or       Dutch <Dtch> [1..1] IdentifierSet 3927
Or       Valoren <Vlrn> [1..1] IdentifierSet 3927
Or       Sicovam <SCVM> [1..1] IdentifierSet 3927
Or       Belgian <Belgn> [1..1] IdentifierSet 3927
Or       Common <Cmon> [1..1] IdentifierSet 3927
Or       DTI <DTI> [1..1] IdentifierSet 3927
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  3927
         Identification <Id> [1..1] Text 3928
         IdentificationSource <IdSrc> [1..1] ± 3928
     FinancialInstrumentName <FinInstrmNm> [0..1] Text 3928
     RedemptionCompletion <RedCmpltn> [0..1] CodeSet 3928
     FinalConfirmation <FnlConf> [0..1] Indicator 3928
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
55.4.5.19.1  LegIdentification <LegId>
Presence: [0..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3863 May 2026
```

