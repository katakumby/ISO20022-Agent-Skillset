---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.26 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "55.4.5.19.26.1 Type <Tp>"]
file_pages: [3923]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.26.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3923 to 3923.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3923

```text
GatingOrHoldBackDetails <GtgOrHldBckDtls> contains the following HoldBackInformation5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 3923
   Amount <Amt> [0..1] Amount C2, C8 3924
   ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 3924
   FinancialInstrumentIdentification <FinInstrmId> [0..1]  3924
{Or     ISIN <ISIN> [1..1] IdentifierSet 3925
Or     SEDOL <SEDOL> [1..1] IdentifierSet 3925
Or     CUSIP <CUSIP> [1..1] IdentifierSet 3926
Or     RIC <RIC> [1..1] IdentifierSet 3926
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 3926
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 3926
Or     CTA <CTA> [1..1] IdentifierSet 3926
Or     QUICK <QUICK> [1..1] IdentifierSet 3926
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 3926
Or     Dutch <Dtch> [1..1] IdentifierSet 3927
Or     Valoren <Vlrn> [1..1] IdentifierSet 3927
Or     Sicovam <SCVM> [1..1] IdentifierSet 3927
Or     Belgian <Belgn> [1..1] IdentifierSet 3927
Or     Common <Cmon> [1..1] IdentifierSet 3927
Or     DTI <DTI> [1..1] IdentifierSet 3927
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  3927
       Identification <Id> [1..1] Text 3928
       IdentificationSource <IdSrc> [1..1] ± 3928
   FinancialInstrumentName <FinInstrmNm> [0..1] Text 3928
   RedemptionCompletion <RedCmpltn> [0..1] CodeSet 3928
   FinalConfirmation <FnlConf> [0..1] Indicator 3928
55.4.5.19.26.1  Type <Tp>
Presence: [1..1]
Definition: Type of gating or a hold back.
Datatype: "GateHoldBack1Code" on page 5307
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3923 May 2026
```

