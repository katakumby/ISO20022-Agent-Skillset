---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.20 ExPostCostCalculationBasis <ExPstCostClctnBsis>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.20 ExPostCostCalculationBasis <ExPstCostClctnBsis>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
15.4.5.8.20  ExPostCostCalculationBasis <ExPstCostClctnBsis>
Presence: [0..1]
Definition: Specifies the basis for ex-post calculations. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 00120.
ExPostCostCalculationBasis <ExPstCostClctnBsis> contains one of the following
ExPostCostCalculationBasis1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 320
Or}   Proprietary <Prtry> [1..1] ± 320
15.4.5.8.20.1  Code <Cd>
Presence: [1..1]
Definition: Ex post cost calculation basis expressed as a code.
Datatype: "ExPostCostCalculationBasis1Code" on page 5300
CodeName Name Definition
FIXB FixedBasis Basic for cost calculation is fixed, that is
calendar year.
ROLL RollingBasis Basis for cost calculation is rolling, that
is, the last twelve months.
15.4.5.8.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Ex post cost calculation basis expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
15.4.5.8.21  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the security.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 320 May 2026
```

