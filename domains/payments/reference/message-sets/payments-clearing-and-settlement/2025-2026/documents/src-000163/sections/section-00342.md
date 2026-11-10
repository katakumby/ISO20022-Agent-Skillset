---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.27 InstructionForNextAgent <InstrForNxtAgt>"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.27 InstructionForNextAgent <InstrForNxtAgt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
InstructionForCreditorAgent <InstrForCdtrAgt> contains the following elements (see
"InstructionForCreditorAgent3" on page 1203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 1203
   InstructionInformation <InstrInf> [0..1] Text 1203
4.4.3.27.23.27  InstructionForNextAgent <InstrForNxtAgt>
Presence: [0..*]
Definition: Further information related to the processing of the payment instruction that may need to be
acted upon by the next agent.
InstructionForNextAgent <InstrForNxtAgt> contains the following InstructionForNextAgent1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 476
   InstructionInformation <InstrInf> [0..1] Text 476
4.4.3.27.23.27.1  Code <Cd>
Presence: [0..1]
Definition: Coded information related to the processing of the payment instruction, provided by the
initiating party, and intended for the next agent in the payment chain.
Datatype: "Instruction4Code" on page 1234
CodeName Name Definition
PHOA PhoneNextAgent Please advise/contact next agent by
phone.
TELA TelecomNextAgent Please advise/contact next agent by the
most efficient means of
telecommunication.
4.4.3.27.23.27.2  InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Further information complementing the coded instruction or instruction to the next agent that
is bilaterally agreed or specific to a user community.
Datatype: "Max140Text" on page 1244
4.4.3.27.23.28  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
476 March 2026
```

