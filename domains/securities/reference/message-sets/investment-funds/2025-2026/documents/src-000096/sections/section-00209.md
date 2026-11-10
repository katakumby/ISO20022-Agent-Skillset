---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.1 Identification <Id>"]
file_pages: [308]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 308 to 308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 308

```text
Constraints
• CostsAndCharges1Guideline
One repetition of CostsAndCharges may be present for the specification of Ex Ante costs and
charges.
• CostsAndCharges2Guideline
One repetition of CostsAndCharges may be present for the specification of Ex Post costs and
charges
15.4.5.1  Identification <Id>
Presence: [0..1]
Definition: Unique technical identifier for an instance of a report within a fund reference data report, as
assigned by the issuer of the report.
Datatype: "Max35Text" on page 5403
15.4.5.2  Version <Vrsn>
Presence: [0..1]
Definition: Version Number. When used in reference to MiFID, this is in the scope of the European
MiFID Template (EMT) reference 00001 and is the version of the template for which the EMT data is
provided.
Version <Vrsn> contains the following elements (see "MarketPracticeVersion1" on page 4818 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
15.4.5.3  AuthorisedProxy <AuthrsdPrxy>
Presence: [0..1]
Definition: Party that reports the data on behalf of the issuer and the entry point e-mail address for
contact. When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT)
references 00002, 00003 and 00004.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 308 May 2026
```

