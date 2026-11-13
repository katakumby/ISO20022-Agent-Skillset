---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.33 RegulatoryReporting <RgltryRptg>"]
file_pages: [200]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.33 RegulatoryReporting <RgltryRptg>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 200 to 200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
3.4.2.33  RegulatoryReporting <RgltryRptg>
Presence: [0..10]
Definition: Information needed due to regulatory and statutory requirements.
RegulatoryReporting <RgltryRptg> contains the following elements (see "RegulatoryReporting10" on
page 1216 for details)
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
3.4.2.34  RelatedRemittanceInformation <RltdRmtInf>
Presence: [0..10]
Definition: Provides information related to the handling of the remittance information by any of the
agents in the transaction processing chain.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
200 March 2026
```

