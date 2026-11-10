---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.38 RemittanceInformation <RmtInf>"]
file_pages: [897]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.38 RemittanceInformation <RmtInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 897 to 897.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 897

```text
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
7.4.2.38  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
RemittanceInformation <RmtInf> contains the following elements (see "RemittanceInformation2" on
page 1192 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 1192
7.4.2.39  UnderlyingAllocation <UndrlygAllcn>
Presence: [0..*]
Definition: Provides information on the underlying allocations that make up the payment.
Usage: Only used by the Securities industry.
Impacted by: C78 "UnderlyingAllocationGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
897 March 2026
```

