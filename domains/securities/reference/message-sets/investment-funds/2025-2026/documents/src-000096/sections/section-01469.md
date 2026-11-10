---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.47 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "43.4.5.9.47.1 Type <Tp>"]
file_pages: [2048]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.47.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2048 to 2048.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2048

```text
GatingOrHoldBackDetails <GtgOrHldBckDtls> contains the following HoldBackInformation5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 2048
   Amount <Amt> [0..1] Amount C3, C10 2049
   ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 2049
   FinancialInstrumentIdentification <FinInstrmId> [0..1]  2049
{Or     ISIN <ISIN> [1..1] IdentifierSet 2050
Or     SEDOL <SEDOL> [1..1] IdentifierSet 2050
Or     CUSIP <CUSIP> [1..1] IdentifierSet 2051
Or     RIC <RIC> [1..1] IdentifierSet 2051
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 2051
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 2051
Or     CTA <CTA> [1..1] IdentifierSet 2051
Or     QUICK <QUICK> [1..1] IdentifierSet 2051
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 2051
Or     Dutch <Dtch> [1..1] IdentifierSet 2052
Or     Valoren <Vlrn> [1..1] IdentifierSet 2052
Or     Sicovam <SCVM> [1..1] IdentifierSet 2052
Or     Belgian <Belgn> [1..1] IdentifierSet 2052
Or     Common <Cmon> [1..1] IdentifierSet 2052
Or     DTI <DTI> [1..1] IdentifierSet 2052
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  2052
       Identification <Id> [1..1] Text 2053
       IdentificationSource <IdSrc> [1..1] ± 2053
   FinancialInstrumentName <FinInstrmNm> [0..1] Text 2053
   RedemptionCompletion <RedCmpltn> [0..1] CodeSet 2053
   FinalConfirmation <FnlConf> [0..1] Indicator 2053
43.4.5.9.47.1  Type <Tp>
Presence: [1..1]
Definition: Type of gating or a hold back.
Datatype: "GateHoldBack1Code" on page 5307
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2048 May 2026
```

