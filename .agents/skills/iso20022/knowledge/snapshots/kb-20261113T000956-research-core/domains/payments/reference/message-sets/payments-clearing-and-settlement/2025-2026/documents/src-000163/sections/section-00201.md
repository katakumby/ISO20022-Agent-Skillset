---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.1.12 InstructingAgent <InstgAgt>"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.1.12 InstructingAgent <InstgAgt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
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
4.4.1.12  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Usage: The instructing agent is the party sending the return message and not the party that sent the
original instruction that is being returned.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
286 March 2026
```

