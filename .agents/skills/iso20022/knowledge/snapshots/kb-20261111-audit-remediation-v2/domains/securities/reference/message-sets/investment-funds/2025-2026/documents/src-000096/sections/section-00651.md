---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.17 Conversion <Convs>", "34.4.4.17.1 SourceSecurity <SrcScty>"]
file_pages: [886]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.17.1 SourceSecurity <SrcScty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 886 to 886.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 886

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Reference <Ref> [0..1] Text 892
   AdditionalInformation <AddtlInf> [0..*] ± 892
34.4.4.17.1  SourceSecurity <SrcScty>
Presence: [1..1]
Definition: Identification of the source security.
Impacted by: C19 "IdentificationGuideline"
SourceSecurity <SrcScty> contains the following FinancialInstrumentIdentification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  887
{Or     ISIN <ISIN> [1..1] IdentifierSet 887
Or     SEDOL <SEDOL> [1..1] IdentifierSet 888
Or     CUSIP <CUSIP> [1..1] IdentifierSet 888
Or     RIC <RIC> [1..1] IdentifierSet 888
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 888
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 888
Or     CTA <CTA> [1..1] IdentifierSet 888
Or     QUICK <QUICK> [1..1] IdentifierSet 888
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 889
Or     Dutch <Dtch> [1..1] IdentifierSet 889
Or     Valoren <Vlrn> [1..1] IdentifierSet 889
Or     Sicovam <SCVM> [1..1] IdentifierSet 889
Or     Belgian <Belgn> [1..1] IdentifierSet 889
Or     Common <Cmon> [1..1] IdentifierSet 889
Or     DTI <DTI> [1..1] IdentifierSet 889
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  889
       Identification <Id> [1..1] Text 890
       IdentificationSource <IdSrc> [1..1] ± 890
   Name <Nm> [0..1] Text 890
   ShortName <ShrtNm> [0..1] Text 890
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 886 May 2026
```

