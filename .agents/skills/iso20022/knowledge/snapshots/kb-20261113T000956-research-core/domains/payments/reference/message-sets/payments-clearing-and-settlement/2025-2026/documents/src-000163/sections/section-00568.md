---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.42 InstructionForNextAgent <InstrForNxtAgt>"]
file_pages: [772]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.42 InstructionForNextAgent <InstrForNxtAgt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 772 to 772.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 772

```text
InstructionForCreditorAgent <InstrForCdtrAgt> contains the following elements (see
"InstructionForCreditorAgent3" on page 1203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 1203
   InstructionInformation <InstrInf> [0..1] Text 1203
6.4.2.42  InstructionForNextAgent <InstrForNxtAgt>
Presence: [0..*]
Definition: Further information related to the processing of the payment instruction that may need to be
acted upon by the next agent.
Usage: The next agent may not be the creditor agent.
The instruction can relate to a level of service, can be an instruction that has to be executed by the
agent, or can be information required by the next agent.
InstructionForNextAgent <InstrForNxtAgt> contains the following InstructionForNextAgent1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 772
   InstructionInformation <InstrInf> [0..1] Text 772
6.4.2.42.1  Code <Cd>
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
6.4.2.42.2  InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Further information complementing the coded instruction or instruction to the next agent that
is bilaterally agreed or specific to a user community.
Datatype: "Max140Text" on page 1244
6.4.2.43  Purpose <Purp>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
772 March 2026
```

