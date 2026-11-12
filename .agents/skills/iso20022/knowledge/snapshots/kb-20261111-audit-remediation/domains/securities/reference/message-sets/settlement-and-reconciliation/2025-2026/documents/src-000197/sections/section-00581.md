---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.16 AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>", "26.4.18.1 ProcessingStatus <PrcgSts>", "26.4.18.1.4 PendingCancellation <PdgCxl>", "26.4.18.1.4.2 Reason <Rsn>", "26.4.18.1.4.2.1 Code <Cd>", "26.4.18.1.4.2.1.1 Code <Cd>"]
file_pages: [874]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.18.1.4.2.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 874 to 874.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 874

```text
26.4.18.1.4.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Datatype: "PendingReason32Code" on page 2105
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
OTHR Other Other. See Narrative.
26.4.18.1.4.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending, using a proprietary
format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
26.4.18.1.4.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
26.4.18.1.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 874 March 2026
```

