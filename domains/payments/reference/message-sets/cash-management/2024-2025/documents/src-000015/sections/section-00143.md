---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>", "5.4.2.1.1.3 CommonStatus <CmonSts>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1.3 CommonStatus <CmonSts>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
5.4.2.1.1.3  CommonStatus <CmonSts>
Presence: [0..*]
Definition: Status of a transfer.
CommonStatus <CmonSts> contains the following PaymentStatus6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1]  237
{Or     Pending <Pdg> [1..1] CodeSet 238
Or     Final <Fnl> [1..1] CodeSet 239
Or     RTGS <RTGS> [1..1] Text 239
Or     Settlement <Sttlm> [1..1] Text 239
Or}     Proprietary <Prtry> [1..1] Text 239
   DateTime <DtTm> [0..1] ± 239
   Reason <Rsn> [0..*]  240
{Or     Unmatched <Umtchd> [1..1] CodeSet 240
Or     Cancelled <Canc> [1..1] CodeSet 242
Or     Suspended <Sspd> [1..1] CodeSet 242
Or     PendingFailingSettlement <PdgFlngSttlm> [1..1] CodeSet 242
Or     PendingSettlement <PdgSttlm> [1..1] CodeSet 245
Or     ProprietaryRejection <PrtryRjctn> [1..1]  247
       ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 247
       Reason <Rsn> [1..1] Text 247
Or}     Proprietary <Prtry> [1..1] Text 248
5.4.2.1.1.3.1  Code <Cd>
Presence: [0..1]
Definition: Status of a transfer, in coded form, as assigned by the transaction administrator.
Code <Cd> contains one of the following PaymentStatusCode6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1] CodeSet 238
Or   Final <Fnl> [1..1] CodeSet 239
Or   RTGS <RTGS> [1..1] Text 239
Or   Settlement <Sttlm> [1..1] Text 239
Or}   Proprietary <Prtry> [1..1] Text 239
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 237 February 2025
```

