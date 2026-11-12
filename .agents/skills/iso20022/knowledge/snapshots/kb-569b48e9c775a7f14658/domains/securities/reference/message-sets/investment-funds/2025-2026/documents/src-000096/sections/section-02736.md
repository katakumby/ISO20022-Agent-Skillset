---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.2 LegExecutionIdentification <LegExctnId>"]
file_pages: [3864, 3865]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.2 LegExecutionIdentification <LegExctnId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3864 to 3865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3864

```text
55.4.5.19.2  LegExecutionIdentification <LegExctnId>
Presence: [0..1]
Definition: Unique identifier for the instance of the leg execution within a switch confirmation.
Datatype: "Max35Text" on page 5403
55.4.5.19.3  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the redemption leg of the investment fund order execution is
related.
Impacted by: C18 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3864 May 2026
```

## File page 3865

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3866
{Or     ISIN <ISIN> [1..1] IdentifierSet 3866
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3867
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3867
Or     RIC <RIC> [1..1] IdentifierSet 3867
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3867
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3867
Or     CTA <CTA> [1..1] IdentifierSet 3867
Or     QUICK <QUICK> [1..1] IdentifierSet 3867
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3868
Or     Dutch <Dtch> [1..1] IdentifierSet 3868
Or     Valoren <Vlrn> [1..1] IdentifierSet 3868
Or     Sicovam <SCVM> [1..1] IdentifierSet 3868
Or     Belgian <Belgn> [1..1] IdentifierSet 3868
Or     Common <Cmon> [1..1] IdentifierSet 3868
Or     DTI <DTI> [1..1] IdentifierSet 3868
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3868
       Identification <Id> [1..1] Text 3869
       IdentificationSource <IdSrc> [1..1] ± 3869
   Name <Nm> [0..1] Text 3869
   ShortName <ShrtNm> [0..1] Text 3869
   SupplementaryIdentification <SplmtryId> [0..1] Text 3869
   ClassType <ClssTp> [0..1] Text 3869
   SecuritiesForm <SctiesForm> [0..1] CodeSet 3870
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3870
   ProductGroup <PdctGrp> [0..1] Text 3870
   SeriesIdentification <SrsId> [0..1]  C34 3870
     SeriesDate <SrsDt> [0..1] ± 3871
     SeriesName <SrsNm> [0..1] Text 3871
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3865 May 2026
```

