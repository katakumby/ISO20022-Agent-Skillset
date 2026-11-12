---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.1 LegIdentification <LegId>"]
file_pages: [3551, 3552]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.1 LegIdentification <LegId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3551 to 3552.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3551

```text
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
53.4.5.16.1  LegIdentification <LegId>
Presence: [0..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 5403
53.4.5.16.2  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class related to the redemption leg of the order.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3551 May 2026
```

## File page 3552

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3553
{Or     ISIN <ISIN> [1..1] IdentifierSet 3553
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3554
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3554
Or     RIC <RIC> [1..1] IdentifierSet 3554
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3554
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3554
Or     CTA <CTA> [1..1] IdentifierSet 3554
Or     QUICK <QUICK> [1..1] IdentifierSet 3554
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3555
Or     Dutch <Dtch> [1..1] IdentifierSet 3555
Or     Valoren <Vlrn> [1..1] IdentifierSet 3555
Or     Sicovam <SCVM> [1..1] IdentifierSet 3555
Or     Belgian <Belgn> [1..1] IdentifierSet 3555
Or     Common <Cmon> [1..1] IdentifierSet 3555
Or     DTI <DTI> [1..1] IdentifierSet 3555
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3555
       Identification <Id> [1..1] Text 3556
       IdentificationSource <IdSrc> [1..1] ± 3556
   Name <Nm> [0..1] Text 3556
   ShortName <ShrtNm> [0..1] Text 3556
   SupplementaryIdentification <SplmtryId> [0..1] Text 3556
   ClassType <ClssTp> [0..1] Text 3556
   SecuritiesForm <SctiesForm> [0..1] CodeSet 3557
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3557
   ProductGroup <PdctGrp> [0..1] Text 3557
   SeriesIdentification <SrsId> [0..1]  C35 3557
     SeriesDate <SrsDt> [0..1] ± 3558
     SeriesName <SrsNm> [0..1] Text 3558
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3552 May 2026
```

