---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.17 Regulatory Reporting", "10.1.17.1 RegulatoryReporting10", "10.1.17.1.1 DebitCreditReportingIndicator <DbtCdtRptgInd>"]
file_pages: [1217]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.17.1.1 DebitCreditReportingIndicator <DbtCdtRptgInd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1217 to 1217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1217

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitCreditReportingIndicator <DbtCdtRptgInd> [1..1] CodeSet 1217
   Authority <Authrty> [0..1]  1217
     Name <Nm> [0..1] Text 1218
     Country <Ctry> [0..1] CodeSet C10 1218
   Details <Dtls> [0..*]  C40 1218
     Type <Tp> [0..1]  1219
{Or       Code <Cd> [1..1] CodeSet 1219
Or}       Proprietary <Prtry> [1..1] Text 1219
     Date <Dt> [0..1] Date 1219
     Country <Ctry> [0..1] CodeSet C10 1219
     ReportingCode <RptgCd> [0..1] Text 1219
     Amount <Amt> [0..1] Amount C2, C12 1220
     Information <Inf> [0..*] Text 1220
10.1.17.1.1  DebitCreditReportingIndicator <DbtCdtRptgInd>
Presence: [1..1]
Definition: Identifies whether the regulatory reporting information applies to the debit side, to the credit
side or to both debit and credit sides of the transaction.
Datatype: "RegulatoryReportingType1Code" on page 1236
CodeName Name Definition
CRED Credit Regulatory information applies to the
credit side.
DEBT Debit Regulatory information applies to the
debit side.
BOTH Both Regulatory information applies to both
credit and debit sides.
10.1.17.1.2  Authority <Authrty>
Presence: [0..1]
Definition: Entity requiring the regulatory reporting information.
Authority <Authrty> contains the following RegulatoryAuthority2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1218
   Country <Ctry> [0..1] CodeSet C10 1218
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1217 March 2026
```

