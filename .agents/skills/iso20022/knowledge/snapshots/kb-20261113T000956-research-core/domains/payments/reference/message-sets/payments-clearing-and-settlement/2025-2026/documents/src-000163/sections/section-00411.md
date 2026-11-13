---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "4.4.3.27.24.35 InstructionForNextAgent <InstrForNxtAgt>", "4.4.3.27.24.35.1 Code <Cd>"]
file_pages: [557]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24.35.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 557 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 557

```text
InstructionForNextAgent <InstrForNxtAgt> contains the following InstructionForNextAgent1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 557
   InstructionInformation <InstrInf> [0..1] Text 557
4.4.3.27.24.35.1  Code <Cd>
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
4.4.3.27.24.35.2  InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Further information complementing the coded instruction or instruction to the next agent that
is bilaterally agreed or specific to a user community.
Datatype: "Max140Text" on page 1244
4.4.3.27.24.36  Purpose <Purp>
Presence: [0..1]
Definition: Underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
4.4.3.27.24.37  RemittanceInformation <RmtInf>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
557 March 2026
```

