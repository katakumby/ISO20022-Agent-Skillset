---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.1 GroupHeader <GrpHdr>", "8.4.1.1 MessageIdentification <MsgId>"]
file_pages: [1021]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.1.1 MessageIdentification <MsgId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1021 to 1021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1021

```text
GroupHeader <GrpHdr> contains the following GroupHeader119 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 1021
   CreationDateTime <CreDtTm> [1..1] DateTime 1021
   NumberOfTransactions <NbOfTxs> [1..1] Text 1021
   ControlSum <CtrlSum> [0..1] Quantity 1021
   InstructingAgent <InstgAgt> [0..1] ± 1021
   InstructedAgent <InstdAgt> [0..1] ± 1022
8.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the
chain to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 1246
8.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
8.4.1.3  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message.
Datatype: "Max15NumericText" on page 1244
8.4.1.4  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
8.4.1.5  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1021 March 2026
```

