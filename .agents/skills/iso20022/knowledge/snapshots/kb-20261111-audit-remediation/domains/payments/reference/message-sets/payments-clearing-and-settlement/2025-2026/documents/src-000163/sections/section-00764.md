---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>", "8.4.2.1 CreditIdentification <CdtId>"]
file_pages: [1027]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2.1 CreditIdentification <CdtId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1027 to 1027.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1027

```text
8.4.2.1  CreditIdentification <CdtId>
Presence: [1..1]
Definition: Unique identification, as assigned by a sending party, to unambiguously identify the credit
instruction within the message.
Datatype: "Max35Text" on page 1246
8.4.2.2  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual direct debit transaction or a batch entry for the
sum of the amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 1241):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
8.4.2.3  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Further specifies the type of transaction.
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation28" on page 1203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 1204
   ClearingChannel <ClrChanl> [0..1] CodeSet 1204
   ServiceLevel <SvcLvl> [0..*]  1204
{Or     Code <Cd> [1..1] CodeSet 1205
Or}     Proprietary <Prtry> [1..1] Text 1205
   LocalInstrument <LclInstrm> [0..1]  1205
{Or     Code <Cd> [1..1] CodeSet 1205
Or}     Proprietary <Prtry> [1..1] Text 1205
   CategoryPurpose <CtgyPurp> [0..1]  1205
{Or     Code <Cd> [1..1] CodeSet 1206
Or}     Proprietary <Prtry> [1..1] Text 1206
8.4.2.4  TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1027 March 2026
```

