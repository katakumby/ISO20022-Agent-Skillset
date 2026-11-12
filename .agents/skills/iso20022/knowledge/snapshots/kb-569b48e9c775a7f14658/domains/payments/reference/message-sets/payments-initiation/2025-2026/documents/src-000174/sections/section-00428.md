---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Regulatory Reporting"]
file_pages: [579]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17 Regulatory Reporting

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 579 to 579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 579

```text
Definition: Information that locates and identifies a specific address, as defined by postal services,
presented in free format text.
Datatype: "Max70Text" on page 610
6.1.17 Regulatory Reporting
6.1.17.1  RegulatoryReporting10
Definition: Information needed due to regulatory and/or statutory requirements.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitCreditReportingIndicator <DbtCdtRptgInd> [1..1] CodeSet 579
   Authority <Authrty> [0..1]  579
     Name <Nm> [0..1] Text 580
     Country <Ctry> [0..1] CodeSet C18 580
   Details <Dtls> [0..*]  C34 580
     Type <Tp> [0..1]  581
{Or       Code <Cd> [1..1] CodeSet 581
Or}       Proprietary <Prtry> [1..1] Text 581
     Date <Dt> [0..1] Date 581
     Country <Ctry> [0..1] CodeSet C18 581
     ReportingCode <RptgCd> [0..1] Text 582
     Amount <Amt> [0..1] Amount C2, C19 582
     Information <Inf> [0..*] Text 582
6.1.17.1.1  DebitCreditReportingIndicator <DbtCdtRptgInd>
Presence: [1..1]
Definition: Identifies whether the regulatory reporting information applies to the debit side, to the credit
side or to both debit and credit sides of the transaction.
Datatype: "RegulatoryReportingType1Code" on page 600
CodeName Name Definition
CRED Credit Regulatory information applies to the
credit side.
DEBT Debit Regulatory information applies to the
debit side.
BOTH Both Regulatory information applies to both
credit and debit sides.
6.1.17.1.2  Authority <Authrty>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 579 March 2026
```

