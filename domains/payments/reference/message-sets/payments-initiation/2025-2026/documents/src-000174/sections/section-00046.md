---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.21 InstructionForDebtorAgent <InstrForDbtrAgt>"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.21 InstructionForDebtorAgent <InstrForDbtrAgt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
InstructionForCreditorAgent <InstrForCdtrAgt> contains the following elements (see
"InstructionForCreditorAgent3" on page 563 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 563
   InstructionInformation <InstrInf> [0..1] Text 564
2.4.2.19.21  InstructionForDebtorAgent <InstrForDbtrAgt>
Presence: [0..1]
Definition: Further information related to the processing of the payment instruction, that may need to be
acted upon by the debtor agent, depending on agreement between debtor and the debtor agent.
InstructionForDebtorAgent <InstrForDbtrAgt> contains the following InstructionForDebtorAgent1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 72
   InstructionInformation <InstrInf> [0..1] Text 72
2.4.2.19.21.1  Code <Cd>
Presence: [0..1]
Definition: Coded information related to the processing of the payment instruction, provided by the
initiating party, and intended for the creditor's agent.
Datatype: "ExternalDebtorAgentInstruction1Code" on page 593
2.4.2.19.21.2  InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Further information complementing the coded instruction or instruction to the creditor's agent
that is bilaterally agreed or specific to a user community.
Datatype: "Max140Text" on page 608
2.4.2.19.22  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 554 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 554
Or}   Proprietary <Prtry> [1..1] Text 554
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 72 March 2026
```

