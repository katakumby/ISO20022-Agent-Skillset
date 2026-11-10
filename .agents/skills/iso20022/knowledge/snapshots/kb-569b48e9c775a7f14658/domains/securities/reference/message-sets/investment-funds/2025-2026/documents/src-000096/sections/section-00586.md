---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.7 Instrument <Instrm>", "32.4.2.7.1 Security <Scty>"]
file_pages: [794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.7.1 Security <Scty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 794 to 794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 794

```text
Instrument <Instrm> contains one of the following FinancialInstrument101Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Security <Scty> [1..1]  C6 794
     Identification <Id> [1..1]  795
{Or       ISIN <ISIN> [1..1] IdentifierSet 796
Or       SEDOL <SEDOL> [1..1] IdentifierSet 796
Or       CUSIP <CUSIP> [1..1] IdentifierSet 797
Or       RIC <RIC> [1..1] IdentifierSet 797
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 797
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 797
Or       CTA <CTA> [1..1] IdentifierSet 797
Or       QUICK <QUICK> [1..1] IdentifierSet 797
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 797
Or       Dutch <Dtch> [1..1] IdentifierSet 798
Or       Valoren <Vlrn> [1..1] IdentifierSet 798
Or       Sicovam <SCVM> [1..1] IdentifierSet 798
Or       Belgian <Belgn> [1..1] IdentifierSet 798
Or       Common <Cmon> [1..1] IdentifierSet 798
Or       DTI <DTI> [1..1] IdentifierSet 798
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  798
         Identification <Id> [1..1] Text 799
         IdentificationSource <IdSrc> [1..1] ± 799
     Name <Nm> [0..1] Text 799
     ShortName <ShrtNm> [0..1] Text 799
     ClassificationType <ClssfctnTp> [0..1] ± 799
Or   CashAsset <CshAsst> [1..1] ± C5 799
Or}   OtherAsset <OthrAsst> [1..1] ± 800
32.4.2.7.1  Security <Scty>
Presence: [1..1]
Definition: Identification of the security.
Impacted by: C6 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 794 May 2026
```

