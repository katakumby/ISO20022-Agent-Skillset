---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.2 Instrument <Instrm>", "38.4.15.8.2.1 Security <Scty>", "38.4.15.8.2.1.1 Identification <Id>", "38.4.15.8.2.1.1.16 OtherProprietaryIdentification <OthrPrtryId>", "38.4.15.8.2.1.1.16.1 Identification <Id>"]
file_pages: [1387]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.2.1.1.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1387 to 1387.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1387

```text
38.4.15.8.2.1.1.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
38.4.15.8.2.1.1.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
38.4.15.8.2.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
38.4.15.8.2.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
38.4.15.8.2.1.4  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Type of security.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 4816 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 4816
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 4816
38.4.15.8.2.1.5  RestrictedIndicator <RstrctdInd>
Presence: [0..1]
Definition: Indicates whether the security is a restricted security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1387 May 2026
```

