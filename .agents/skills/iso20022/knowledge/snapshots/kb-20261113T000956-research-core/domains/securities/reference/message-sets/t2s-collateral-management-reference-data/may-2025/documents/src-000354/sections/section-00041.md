---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["6 reda.028.001.01 CollateralDataStatusAdviceV01", "6.4 Message Building Blocks", "6.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "6.4.3.3 EligibilitySetProfile <ElgbltySetPrfl>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 6.4.3.3 EligibilitySetProfile <ElgbltySetPrfl>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max140Text" on page 83
6.4.3.3  EligibilitySetProfile <ElgbltySetPrfl>
Presence: [0..1]
Definition: Number identifying the collateral eligibility set profile of the counterparty.
EligibilitySetProfile <ElgbltySetPrfl> contains the following elements (see "GenericIdentification1" on
page 65 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   SchemeName <SchmeNm> [0..1] Text 65
   Issuer <Issr> [0..1] Text 65
6.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 69 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 69
   Envelope <Envlp> [1..1] (External Schema) 70
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 45 May 2025
```

