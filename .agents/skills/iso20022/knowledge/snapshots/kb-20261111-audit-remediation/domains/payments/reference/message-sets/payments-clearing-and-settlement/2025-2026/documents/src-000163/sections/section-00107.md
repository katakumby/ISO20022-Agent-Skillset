---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.1.10 PaymentTypeInformation <PmtTpInf>"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.1.10 PaymentTypeInformation <PmtTpInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
3.4.1.10  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation27" on page 1206 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 1206
   ClearingChannel <ClrChanl> [0..1] CodeSet 1207
   ServiceLevel <SvcLvl> [0..*]  1207
{Or     Code <Cd> [1..1] CodeSet 1207
Or}     Proprietary <Prtry> [1..1] Text 1207
   LocalInstrument <LclInstrm> [0..1]  1208
{Or     Code <Cd> [1..1] CodeSet 1208
Or}     Proprietary <Prtry> [1..1] Text 1208
   SequenceType <SeqTp> [0..1] CodeSet 1208
   CategoryPurpose <CtgyPurp> [0..1]  1208
{Or     Code <Cd> [1..1] CodeSet 1209
Or}     Proprietary <Prtry> [1..1] Text 1209
3.4.1.11  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
149 March 2026
```

