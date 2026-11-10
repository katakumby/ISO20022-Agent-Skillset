---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.1 LegIdentification <LegId>"]
file_pages: [3936, 3937]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.1 LegIdentification <LegId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3936 to 3937.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3936

```text
55.4.5.20.1  LegIdentification <LegId>
Presence: [0..1]
Definition: Unique technical identifier for the instance of the leg within a switch.
Datatype: "Max35Text" on page 5403
55.4.5.20.2  LegExecutionIdentification <LegExctnId>
Presence: [0..1]
Definition: Unique identifier for the instance of the leg execution within a switch confirmation.
Datatype: "Max35Text" on page 5403
55.4.5.20.3  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Investment fund class to which the subscription leg of the investment fund order execution is
related.
Impacted by: C18 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3936 May 2026
```

## File page 3937

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument107
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3938
{Or     ISIN <ISIN> [1..1] IdentifierSet 3938
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3939
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3939
Or     RIC <RIC> [1..1] IdentifierSet 3939
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3939
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3939
Or     CTA <CTA> [1..1] IdentifierSet 3939
Or     QUICK <QUICK> [1..1] IdentifierSet 3939
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3940
Or     Dutch <Dtch> [1..1] IdentifierSet 3940
Or     Valoren <Vlrn> [1..1] IdentifierSet 3940
Or     Sicovam <SCVM> [1..1] IdentifierSet 3940
Or     Belgian <Belgn> [1..1] IdentifierSet 3940
Or     Common <Cmon> [1..1] IdentifierSet 3940
Or     DTI <DTI> [1..1] IdentifierSet 3940
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3940
       Identification <Id> [1..1] Text 3941
       IdentificationSource <IdSrc> [1..1] ± 3941
   Name <Nm> [0..1] Text 3941
   ShortName <ShrtNm> [0..1] Text 3941
   SupplementaryIdentification <SplmtryId> [0..1] Text 3941
   ClassType <ClssTp> [0..1] Text 3941
   SecuritiesForm <SctiesForm> [0..1] CodeSet 3942
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3942
   ProductGroup <PdctGrp> [0..1] Text 3942
   SeriesIdentification <SrsId> [0..1]  C34 3942
     SeriesDate <SrsDt> [0..1] ± 3943
     SeriesName <SrsNm> [0..1] Text 3943
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3937 May 2026
```

