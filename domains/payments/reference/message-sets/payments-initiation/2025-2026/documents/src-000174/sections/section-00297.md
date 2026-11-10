---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.7 PaymentTypeInformation <PmtTpInf>"]
file_pages: [429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.7 PaymentTypeInformation <PmtTpInf>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 429 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 429

```text
5.4.2.7  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation29" on page 569 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 569
   ServiceLevel <SvcLvl> [0..*]  570
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] Text 570
   LocalInstrument <LclInstrm> [0..1]  570
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] Text 571
   SequenceType <SeqTp> [0..1] CodeSet 571
   CategoryPurpose <CtgyPurp> [0..1]  571
{Or     Code <Cd> [1..1] CodeSet 571
Or}     Proprietary <Prtry> [1..1] Text 571
5.4.2.8  RequestedCollectionDate <ReqdColltnDt>
Presence: [1..1]
Definition: Date and time at which the creditor requests that the amount of money is to be collected from
the debtor.
Datatype: "ISODate" on page 603
5.4.2.9  Creditor <Cdtr>
Presence: [1..1]
Definition: Party to which an amount of money is due.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 429 March 2026
```

