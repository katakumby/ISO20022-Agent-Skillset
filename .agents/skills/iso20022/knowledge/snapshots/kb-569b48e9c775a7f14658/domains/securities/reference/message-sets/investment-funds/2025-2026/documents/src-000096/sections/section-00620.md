---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.7 Instrument <Instrm>", "34.4.4.7.1 Security <Scty>"]
file_pages: [850]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.7.1 Security <Scty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 850 to 850.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 850

```text
Instrument <Instrm> contains one of the following FinancialInstrument101Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Security <Scty> [1..1]  C18 850
     Identification <Id> [1..1]  851
{Or       ISIN <ISIN> [1..1] IdentifierSet 852
Or       SEDOL <SEDOL> [1..1] IdentifierSet 852
Or       CUSIP <CUSIP> [1..1] IdentifierSet 853
Or       RIC <RIC> [1..1] IdentifierSet 853
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 853
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 853
Or       CTA <CTA> [1..1] IdentifierSet 853
Or       QUICK <QUICK> [1..1] IdentifierSet 853
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 853
Or       Dutch <Dtch> [1..1] IdentifierSet 854
Or       Valoren <Vlrn> [1..1] IdentifierSet 854
Or       Sicovam <SCVM> [1..1] IdentifierSet 854
Or       Belgian <Belgn> [1..1] IdentifierSet 854
Or       Common <Cmon> [1..1] IdentifierSet 854
Or       DTI <DTI> [1..1] IdentifierSet 854
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  854
         Identification <Id> [1..1] Text 855
         IdentificationSource <IdSrc> [1..1] ± 855
     Name <Nm> [0..1] Text 855
     ShortName <ShrtNm> [0..1] Text 855
     ClassificationType <ClssfctnTp> [0..1] ± 855
Or   CashAsset <CshAsst> [1..1] ± C16 855
Or}   OtherAsset <OthrAsst> [1..1] ± 856
34.4.4.7.1  Security <Scty>
Presence: [1..1]
Definition: Identification of the security.
Impacted by: C18 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 850 May 2026
```

