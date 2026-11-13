---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.1 ReversalIdentification <RvslId>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.1 ReversalIdentification <RvslId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C18,
C17
393
     CreditorAgent <CdtrAgt> [0..1] ± 394
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C18,
C17
395
     Creditor <Cdtr> [0..1]  396
{Or       Party <Pty> [1..1] ± 396
Or}       Agent <Agt> [1..1] ± 397
     CreditorAccount <CdtrAcct> [0..1] ± C18,
C17
398
     UltimateCreditor <UltmtCdtr> [0..1]  399
{Or       Party <Pty> [1..1] ± 399
Or}       Agent <Agt> [1..1] ± 400
     Purpose <Purp> [0..1] ± 401
   SupplementaryData <SplmtryData> [0..*] ± C30 401
4.4.3.8.1  ReversalIdentification <RvslId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the reversed transaction.
Usage: The instructing party is the party sending the reversal message and not the party that sent the
original instruction that is being reversed.
Datatype: "Max35Text" on page 609
4.4.3.8.2  OriginalInstructionIdentification <OrgnlInstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original instructing party for the original instructed
party, to unambiguously identify the original instruction.
Datatype: "Max35Text" on page 609
4.4.3.8.3  OriginalEndToEndIdentification <OrgnlEndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original initiating party, to unambiguously identify
the original transaction.
Datatype: "Max35Text" on page 609
4.4.3.8.4  OriginalUETR <OrgnlUETR>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 309 March 2026
```

