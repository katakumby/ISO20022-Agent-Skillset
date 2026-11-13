---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.17 Conversion <Convs>", "34.4.4.17.1 SourceSecurity <SrcScty>", "34.4.4.17.1.1 Identification <Id>", "34.4.4.17.1.1.16 OtherProprietaryIdentification <OthrPrtryId>", "34.4.4.17.1.1.16.1 Identification <Id>"]
file_pages: [890]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.17.1.1.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 890 to 890.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 890

```text
OtherProprietaryIdentification <OthrPrtryId> contains the following
AlternateSecurityIdentification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 890
   IdentificationSource <IdSrc> [1..1] ± 890
34.4.4.17.1.1.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
34.4.4.17.1.1.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
34.4.4.17.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
34.4.4.17.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
34.4.4.17.2  TotalUnitsNumber <TtlUnitsNb>
Presence: [0..1]
Definition: Number of units of the source security.
Datatype: "DecimalNumber" on page 5400
34.4.4.17.3  UnitsDetails <UnitsDtls>
Presence: [0..*]
Definition: Breakdown of units of the source security.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 890 May 2026
```

