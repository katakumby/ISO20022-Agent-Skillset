---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.7 Instrument <Instrm>", "34.4.4.7.1 Security <Scty>", "34.4.4.7.1.1 Identification <Id>"]
file_pages: [851]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.7.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 851 to 851.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 851

```text
Security <Scty> contains the following FinancialInstrumentIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  851
{Or     ISIN <ISIN> [1..1] IdentifierSet 852
Or     SEDOL <SEDOL> [1..1] IdentifierSet 852
Or     CUSIP <CUSIP> [1..1] IdentifierSet 853
Or     RIC <RIC> [1..1] IdentifierSet 853
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 853
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 853
Or     CTA <CTA> [1..1] IdentifierSet 853
Or     QUICK <QUICK> [1..1] IdentifierSet 853
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 853
Or     Dutch <Dtch> [1..1] IdentifierSet 854
Or     Valoren <Vlrn> [1..1] IdentifierSet 854
Or     Sicovam <SCVM> [1..1] IdentifierSet 854
Or     Belgian <Belgn> [1..1] IdentifierSet 854
Or     Common <Cmon> [1..1] IdentifierSet 854
Or     DTI <DTI> [1..1] IdentifierSet 854
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  854
       Identification <Id> [1..1] Text 855
       IdentificationSource <IdSrc> [1..1] ± 855
   Name <Nm> [0..1] Text 855
   ShortName <ShrtNm> [0..1] Text 855
   ClassificationType <ClssfctnTp> [0..1] ± 855
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
34.4.4.7.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 851 May 2026
```

