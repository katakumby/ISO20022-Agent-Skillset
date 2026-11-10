---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.4 Status <Sts>", "4.4.2.2.2.2.3.4.1 PaymentInstructionStatus <PmtInstrSts>"]
file_pages: [157]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.4.1 PaymentInstructionStatus <PmtInstrSts>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 157 to 157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 157

```text
Status <Sts> contains the following InstructionStatusSearch5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstructionStatus <PmtInstrSts> [0..1]  157
{Or     PendingStatus <PdgSts> [1..1] CodeSet 157
Or     FinalStatus <FnlSts> [1..1] CodeSet 158
Or}     PendingAndFinalStatus <PdgAndFnlSts> [1..1] CodeSet 159
   PaymentInstructionStatusDateTime
<PmtInstrStsDtTm>
[0..1]  159
{Or     FromDateTime <FrDtTm> [1..1] DateTime 159
Or     ToDateTime <ToDtTm> [1..1] DateTime 159
Or}     DateTimeRange <DtTmRg> [1..1] ± 159
   ProprietaryStatusReason <PrtryStsRsn> [0..1] Text 160
4.4.2.2.2.2.3.4.1  PaymentInstructionStatus <PmtInstrSts>
Presence: [0..1]
Definition: Status of a transfer.
PaymentInstructionStatus <PmtInstrSts> contains one of the following
PaymentStatusCodeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingStatus <PdgSts> [1..1] CodeSet 157
Or   FinalStatus <FnlSts> [1..1] CodeSet 158
Or}   PendingAndFinalStatus <PdgAndFnlSts> [1..1] CodeSet 159
4.4.2.2.2.2.3.4.1.1  PendingStatus <PdgSts>
Presence: [1..1]
Definition: Qualifies further the pending status.
Datatype: "PendingStatus4Code" on page 869
CodeName Name Definition
ACPD Accepted Transaction has been accepted by the
clearing agent.
VALD Validated Transaction has been validated by the
clearing agent.
MATD Matched Transaction has been matched with a
corresponding transaction by the
clearing agent.
AUTD Authorised Transaction has been authorised by the
transaction administrator or authorised
party.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 157 February 2025
```

