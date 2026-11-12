---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.1 LegIdentification <LegId>"]
file_pages: [3620, 3621]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.1 LegIdentification <LegId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3620 to 3621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3620

```text
Following Must be True
    /PhysicalDeliveryDetails Must be absent
• PhysicalDeliveryDetails2Rule
If PhysicalDeliveryIndicator is "true" or "1" (Yes), then PhysicalDeliveryDetails must be present.
On Condition
    /PhysicalDeliveryIndicator is equal to value 'true'
 Or    /PhysicalDeliveryIndicator is equal to value '1'
Following Must be True
    /PhysicalDeliveryDetails Must be present
53.4.5.17.1  LegIdentification <LegId>
Presence: [0..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 5403
53.4.5.17.2  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class related to the subscription leg of the order.
Impacted by: C20 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3620 May 2026
```

## File page 3621

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3622
{Or     ISIN <ISIN> [1..1] IdentifierSet 3622
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3623
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3623
Or     RIC <RIC> [1..1] IdentifierSet 3623
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3623
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3623
Or     CTA <CTA> [1..1] IdentifierSet 3623
Or     QUICK <QUICK> [1..1] IdentifierSet 3623
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3624
Or     Dutch <Dtch> [1..1] IdentifierSet 3624
Or     Valoren <Vlrn> [1..1] IdentifierSet 3624
Or     Sicovam <SCVM> [1..1] IdentifierSet 3624
Or     Belgian <Belgn> [1..1] IdentifierSet 3624
Or     Common <Cmon> [1..1] IdentifierSet 3624
Or     DTI <DTI> [1..1] IdentifierSet 3624
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3624
       Identification <Id> [1..1] Text 3625
       IdentificationSource <IdSrc> [1..1] ± 3625
   Name <Nm> [0..1] Text 3625
   ShortName <ShrtNm> [0..1] Text 3625
   SupplementaryIdentification <SplmtryId> [0..1] Text 3625
   ClassType <ClssTp> [0..1] Text 3625
   SecuritiesForm <SctiesForm> [0..1] CodeSet 3626
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3626
   ProductGroup <PdctGrp> [0..1] Text 3626
   SeriesIdentification <SrsId> [0..1]  C35 3626
     SeriesDate <SrsDt> [0..1] ± 3627
     SeriesName <SrsNm> [0..1] Text 3627
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3621 May 2026
```

