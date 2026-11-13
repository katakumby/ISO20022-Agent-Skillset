---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.12 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "56.4.3.2.12.1 Type <Tp>"]
file_pages: [4168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.12.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4168 to 4168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4168

```text
GatingOrHoldBackDetails <GtgOrHldBckDtls> contains the following HoldBackInformation4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] CodeSet 4168
   Amount <Amt> [0..1] Amount C1, C8 4169
   ExpectedReleaseDate <XpctdRlsDt> [0..1] Date 4169
   FinancialInstrumentIdentification <FinInstrmId> [0..1]  4169
{Or     ISIN <ISIN> [1..1] IdentifierSet 4170
Or     SEDOL <SEDOL> [1..1] IdentifierSet 4170
Or     CUSIP <CUSIP> [1..1] IdentifierSet 4171
Or     RIC <RIC> [1..1] IdentifierSet 4171
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 4171
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 4171
Or     CTA <CTA> [1..1] IdentifierSet 4171
Or     QUICK <QUICK> [1..1] IdentifierSet 4171
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 4171
Or     Dutch <Dtch> [1..1] IdentifierSet 4172
Or     Valoren <Vlrn> [1..1] IdentifierSet 4172
Or     Sicovam <SCVM> [1..1] IdentifierSet 4172
Or     Belgian <Belgn> [1..1] IdentifierSet 4172
Or     Common <Cmon> [1..1] IdentifierSet 4172
Or     DTI <DTI> [1..1] IdentifierSet 4172
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  4172
       Identification <Id> [1..1] Text 4173
       IdentificationSource <IdSrc> [1..1] ± 4173
   FinancialInstrumentName <FinInstrmNm> [0..1] Text 4173
   RedemptionCompletion <RedCmpltn> [0..1] CodeSet 4173
56.4.3.2.12.1  Type <Tp>
Presence: [1..1]
Definition: Type of gating or a hold back.
Datatype: "GateHoldBack1Code" on page 5307
CodeName Name Definition
GATE Gating Gating of redemption proceeds.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4168 May 2026
```

