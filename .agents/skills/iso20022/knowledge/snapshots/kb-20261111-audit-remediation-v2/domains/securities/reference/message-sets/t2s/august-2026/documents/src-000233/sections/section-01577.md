---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.4 Message Building Blocks", "48.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "48.4.3.3 EligibilitySetProfile <ElgbltySetPrfl>"]
file_pages: [2202]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.4.3.3 EligibilitySetProfile <ElgbltySetPrfl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2202 to 2202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2202

```text
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 3326
48.4.3.3  EligibilitySetProfile <ElgbltySetPrfl>
Presence: [0..1]
Definition: Number identifying the collateral eligibility set profile of the counterparty.
EligibilitySetProfile <ElgbltySetPrfl> contains the following elements (see "GenericIdentification1" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
48.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2202 August 2026
```

