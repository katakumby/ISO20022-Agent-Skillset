---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.1 PaymentToReturnCriteria <PmtToRtrCrit>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.1 PaymentToReturnCriteria <PmtToRtrCrit>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     InterbankSettlementAmountIndicator
<IntrBkSttlmAmtInd>
[0..1] Indicator 201
     PriorityIndicator <PrtyInd> [0..1] Indicator 202
     ProcessingValidityTimeIndicator <PrcgVldtyTmInd> [0..1] Indicator 202
     PurposeIndicator <PurpInd> [0..1] Indicator 202
     InstructionCopyIndicator <InstrCpyInd> [0..1] Indicator 202
     PaymentMessageTypeIndicator <PmtMTInd> [0..1] Indicator 202
     PaymentTypeIndicator <PmtTpInd> [0..1] Indicator 202
     TransactionIdentificationIndicator <TxIdInd> [0..1] Indicator 203
     InterbankSettlementDateIndicator <IntrBkSttlmDtInd> [0..1] Indicator 203
     EndToEndIdentificationIndicator <EndToEndIdInd> [0..1] Indicator 203
     PaymentMethodIndicator <PmtMtdInd> [0..1] Indicator 203
     DebtorIndicator <DbtrInd> [0..1] Indicator 203
     DebtorAgentIndicator <DbtrAgtInd> [0..1] Indicator 204
     InstructingReimbursementAgentIndicator
<InstgRmbrsmntAgtInd>
[0..1] Indicator 204
     InstructedReimbursementAgentIndicator
<InstdRmbrsmntAgtInd>
[0..1] Indicator 204
     IntermediaryIndicator <IntrmyInd> [0..1] Indicator 204
     CreditorAgentIndicator <CdtrAgtInd> [0..1] Indicator 204
     CreditorIndicator <CdtrInd> [0..1] Indicator 205
4.4.2.2.2.4.1  PaymentToReturnCriteria <PmtToRtrCrit>
Presence: [0..1]
Definition: Destination of the payment (be it a member or a system or both).
PaymentToReturnCriteria <PmtToRtrCrit> contains the following SystemReturnCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentificationIndicator <SysIdInd> [0..1] Indicator 194
   MemberIdentificationIndicator <MmbIdInd> [0..1] Indicator 195
   CountryIdentificationIndicator <CtryIdInd> [0..1] Indicator 195
   AccountIdentificationIndicator <AcctIdInd> [0..1] Indicator 195
4.4.2.2.2.4.1.1  SystemIdentificationIndicator <SysIdInd>
Presence: [0..1]
Definition: Indicates whether the system identification is requested.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 194 February 2025
```

