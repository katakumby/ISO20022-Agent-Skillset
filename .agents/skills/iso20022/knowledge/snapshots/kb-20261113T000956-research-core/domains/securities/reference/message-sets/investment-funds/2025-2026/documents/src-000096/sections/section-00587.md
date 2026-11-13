---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.7 Instrument <Instrm>", "32.4.2.7.1 Security <Scty>", "32.4.2.7.1.1 Identification <Id>"]
file_pages: [795]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.7.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 795 to 795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 795

```text
Security <Scty> contains the following FinancialInstrumentIdentification6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  795
{Or     ISIN <ISIN> [1..1] IdentifierSet 796
Or     SEDOL <SEDOL> [1..1] IdentifierSet 796
Or     CUSIP <CUSIP> [1..1] IdentifierSet 797
Or     RIC <RIC> [1..1] IdentifierSet 797
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 797
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 797
Or     CTA <CTA> [1..1] IdentifierSet 797
Or     QUICK <QUICK> [1..1] IdentifierSet 797
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 797
Or     Dutch <Dtch> [1..1] IdentifierSet 798
Or     Valoren <Vlrn> [1..1] IdentifierSet 798
Or     Sicovam <SCVM> [1..1] IdentifierSet 798
Or     Belgian <Belgn> [1..1] IdentifierSet 798
Or     Common <Cmon> [1..1] IdentifierSet 798
Or     DTI <DTI> [1..1] IdentifierSet 798
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  798
       Identification <Id> [1..1] Text 799
       IdentificationSource <IdSrc> [1..1] ± 799
   Name <Nm> [0..1] Text 799
   ShortName <ShrtNm> [0..1] Text 799
   ClassificationType <ClssfctnTp> [0..1] ± 799
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
32.4.2.7.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 795 May 2026
```

