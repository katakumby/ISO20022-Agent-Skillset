---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Payment Type", "6.1.17.1 PaymentTypeInformation27", "6.1.17.1.1 InstructionPriority <InstrPrty>"]
file_pages: [869]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17.1.1 InstructionPriority <InstrPrty>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 869 to 869.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 869

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 869
   ClearingChannel <ClrChanl> [0..1] CodeSet 869
   ServiceLevel <SvcLvl> [0..*]  870
{Or     Code <Cd> [1..1] CodeSet 870
Or}     Proprietary <Prtry> [1..1] Text 870
   LocalInstrument <LclInstrm> [0..1]  870
{Or     Code <Cd> [1..1] CodeSet 870
Or}     Proprietary <Prtry> [1..1] Text 870
   SequenceType <SeqTp> [0..1] CodeSet 871
   CategoryPurpose <CtgyPurp> [0..1]  871
{Or     Code <Cd> [1..1] CodeSet 871
Or}     Proprietary <Prtry> [1..1] Text 871
6.1.17.1.1  InstructionPriority <InstrPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the instruction.
Datatype: "Priority2Code" on page 904
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
6.1.17.1.2  ClearingChannel <ClrChanl>
Presence: [0..1]
Definition: Specifies the clearing channel to be used to process the payment instruction.
Datatype: "ClearingChannel2Code" on page 891
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
869 March 2026
```

