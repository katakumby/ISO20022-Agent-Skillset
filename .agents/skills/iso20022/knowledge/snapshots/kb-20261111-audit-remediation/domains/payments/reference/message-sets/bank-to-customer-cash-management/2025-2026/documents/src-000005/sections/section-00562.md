---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.4 Message Building Blocks", "5.4.2 ReportingRequest <RptgReq>", "5.4.2.9 RequestedBalanceType <ReqdBalTp>"]
file_pages: [795]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.4.2.9 RequestedBalanceType <ReqdBalTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 795 to 795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 795

```text
CodeName Name Definition
DEBT Debit Floor limit applies to debit entries.
BOTH Both Floor limit applies to both credit and
debit entries.
5.4.2.9  RequestedBalanceType <ReqdBalTp>
Presence: [0..*]
Definition: Provides details on the requested balance reporting.
RequestedBalanceType <ReqdBalTp> contains the following elements (see "BalanceType13" on
page 817 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  817
{Or     Code <Cd> [1..1] CodeSet 817
Or}     Proprietary <Prtry> [1..1] Text 817
   SubType <SubTp> [0..1]  817
{Or     Code <Cd> [1..1] CodeSet 818
Or}     Proprietary <Prtry> [1..1] Text 818
5.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C9 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 850 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 851
   Envelope <Envlp> [1..1] (External Schema) 851
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
795 March 2026
```

