---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.2 NewPaymentValueSet <NewPmtValSet>", "6.4.2.2.1 Instruction <Instr>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.2.1 Instruction <Instr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
NewPaymentValueSet <NewPmtValSet> contains the following PaymentInstruction33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Instruction <Instr> [0..1] CodeSet 342
   Type <Tp> [0..1]  342
{Or     Code <Cd> [1..1] CodeSet 343
Or}     Proprietary <Prtry> [1..1] Text 344
   Priority <Prty> [0..1]  345
{Or     Code <Cd> [1..1] CodeSet 345
Or}     Proprietary <Prtry> [1..1] Text 345
   ProcessingValidityTime <PrcgVldtyTm> [0..1]  345
{Or     FromDateTime <FrDtTm> [1..1] DateTime 346
Or     ToDateTime <ToDtTm> [1..1] DateTime 346
Or}     DateTimeRange <DtTmRg> [1..1] ± 346
6.4.2.2.1  Instruction <Instr>
Presence: [0..1]
Definition: Further information related to the processing of the payment instruction. The instruction can
relate to a level of service between the bank and the customer, or give instructions to and for specific
parties in the payment chain.
.
Datatype: "Instruction1Code" on page 859
CodeName Name Definition
PBEN PayTheBeneficiary (Ultimate) creditor to be paid only after
verification of identity.
TTIL TimeTill Payment instruction is valid and eligible
for execution until the date and time
stipulated. Otherwise, the payment
instruction will be rejected.
TFRO TimeFrom Payment instruction will be valid and
eligible for execution from the date and
time stipulated.
6.4.2.2.2  Type <Tp>
Presence: [0..1]
Definition: Type, or nature, of the payment, for example an express payment.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 342 February 2025
```

