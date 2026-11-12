---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.83 PendingReason31Choice", "35.1.29.83.2 Proprietary <Prtry>"]
file_pages: [2008]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.83.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2008 to 2008.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2008

```text
CodeName Name Definition
LATE MarketDeadlineMissed Instruction was received after market
deadline.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
PRCY CounterpartyInstructionOnHold Counterparty's instruction is a preadvice,
that is, for matching only.
REGT CertificatesRejected Certificates have been lodged with the
registrar but rejected due to incomplete
documentation or foreign ownership
limitation reached.
SETS SettlementSystemMethodModified Settlement system/method has been
modified at central securities depository
to allow settlement.
CERT WrongCertificatesNumbers Certificate number error.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
35.1.29.83.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.84  CancellationReason23Choice
Definition: Choice of format for the cancellation reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2008
Or}   Proprietary <Prtry> [1..1] ± 2009
35.1.29.84.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Datatype: "CancelledStatusReason9Code" on page 2049
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2008 March 2026
```

