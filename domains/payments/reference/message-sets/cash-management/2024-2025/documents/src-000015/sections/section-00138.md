---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>"]
file_pages: [231, 232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 231 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 231

```text
    /TransactionReport[*]/TransactionOrError/Transaction/CreditDebitIndicator 
Must be absent
• PaymentInstructionStatusRule
If PaymentCommonInformation/PaymentInstructionStatus is present, then TransactionReport/
Transaction/Payment/InstructionStatus/PaymentInstructionStatus is not allowed.
If PaymentCommonInformation/PaymentInstructionStatus is not present, then TransactionReport/
Transaction/Payment/InstructionStatus/PaymentInstructionStatus is optional.
On Condition
    /PaymentCommonInformation/CommonStatus[1] is present
Following Must be True
    /TransactionReport[*]/TransactionOrError/Transaction/Payment/Status[1] Must 
be absent
• TransferValueDateRule
If PaymentCommonInformation/RequestedExecutionDate is present, then TransactionReport/
Transaction/Payment/RequestedExecutionDate is not allowed.
If PaymentCommonInformation/RequestedExecutionDate is not present, then TransactionReport/
Transaction/Payment/RequestedExecutionDate is optional.
On Condition
    /PaymentCommonInformation/RequestedExecutionDate is present
Following Must be True
    /TransactionReport[*]/TransactionOrError/Transaction/Payment/
RequestedExecutionDate Must be absent
5.4.2.1.1  PaymentCommonInformation <PmtCmonInf>
Presence: [0..1]
Definition: Common detailed payment instruction information.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 231 February 2025
```

## File page 232

```text
PaymentCommonInformation <PmtCmonInf> contains the following PaymentCommon6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentFrom <PmtFr> [0..1]  233
     SystemIdentification <SysId> [0..1] ± 233
     MemberIdentification <MmbId> [0..1] ± 233
     Country <Ctry> [0..1] CodeSet C5 234
     AccountIdentification <AcctId> [0..1] ± 234
   PaymentTo <PmtTo> [0..1]  235
     SystemIdentification <SysId> [0..1] ± 235
     MemberIdentification <MmbId> [0..1] ± 235
     Country <Ctry> [0..1] CodeSet C5 236
     AccountIdentification <AcctId> [0..1] ± 236
   CommonStatus <CmonSts> [0..*]  237
     Code <Cd> [0..1]  237
{Or       Pending <Pdg> [1..1] CodeSet 238
Or       Final <Fnl> [1..1] CodeSet 239
Or       RTGS <RTGS> [1..1] Text 239
Or       Settlement <Sttlm> [1..1] Text 239
Or}       Proprietary <Prtry> [1..1] Text 239
     DateTime <DtTm> [0..1] ± 239
     Reason <Rsn> [0..*]  240
{Or       Unmatched <Umtchd> [1..1] CodeSet 240
Or       Cancelled <Canc> [1..1] CodeSet 242
Or       Suspended <Sspd> [1..1] CodeSet 242
Or       PendingFailingSettlement <PdgFlngSttlm> [1..1] CodeSet 242
Or       PendingSettlement <PdgSttlm> [1..1] CodeSet 245
Or       ProprietaryRejection <PrtryRjctn> [1..1]  247
         ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 247
         Reason <Rsn> [1..1] Text 247
Or}       Proprietary <Prtry> [1..1] Text 248
   RequestedExecutionDate <ReqdExctnDt> [0..1] ± 248
   EntryDate <NtryDt> [0..1] ± 248
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 248
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 232 February 2025
```

