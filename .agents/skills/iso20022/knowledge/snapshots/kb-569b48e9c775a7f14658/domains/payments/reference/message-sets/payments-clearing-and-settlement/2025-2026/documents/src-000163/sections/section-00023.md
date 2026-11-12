---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.13 AccountServicerReference <AcctSvcrRef>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.13 AccountServicerReference <AcctSvcrRef>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
EffectiveInterbankSettlementDate <FctvIntrBkSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1169
Or}   DateTime <DtTm> [1..1] DateTime 1169
2.4.3.13  AccountServicerReference <AcctSvcrRef>
Presence: [0..1]
Definition: Unique reference, as assigned by the account servicing institution, to unambiguously identify
the instruction.
Datatype: "Max35Text" on page 1246
2.4.3.14  ClearingSystemReference <ClrSysRef>
Presence: [0..1]
Definition: Unique reference, as assigned by a clearing system, to unambiguously identify the
instruction.
Datatype: "Max35Text" on page 1246
2.4.3.15  CreditSettlementKey <CdtSttlmKey>
Presence: [0..1]
Definition: Cryptographic key provided by the CreditorAgent to confirm that settlement on the creditor's
account is guaranteed.
Datatype: "SHA256SignatureText" on page 1247
2.4.3.16  InstructingAgent <InstgAgt>
Presence: [0..1]
Definition: Agent that instructs the next party in the chain to carry out the (set of) instruction(s).
Usage: The instructing agent is the party sending the status message and not the party that sent the
original instruction that is being reported on.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
40 March 2026
```

