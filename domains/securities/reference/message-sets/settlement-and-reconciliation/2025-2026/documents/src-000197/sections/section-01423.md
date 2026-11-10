---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.21 PendingReason28Choice", "35.1.29.21.1 Code <Cd>"]
file_pages: [1905, 1906]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.21.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1905 to 1906.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1905

```text
35.1.29.21.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending.
Datatype: "PendingReason6Code" on page 2110
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
35.1.29.21.2  Proprietary <Prtry>
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
35.1.29.22  Status19Choice
Definition: Choice of status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1905 March 2026
```

## File page 1906

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AffirmationStatus <AffirmSts> [1..1] ± 1907
Or   AllocationStatus <AllcnSts> [1..1]  1907
{Or     Code <Cd> [1..1] CodeSet 1907
Or}     Proprietary <Prtry> [1..1] ± 1907
Or   RepoCallRequestStatus <RepoCallReqSts> [1..1] ± 1908
Or   CorporateActionEventProcessingStatus
<CorpActnEvtPrcgSts>
[1..1]  1908
{Or     Code <Cd> [1..1] CodeSet 1908
Or}     Proprietary <Prtry> [1..1] ± 1909
Or   CorporateActionEventStage <CorpActnEvtStag> [1..1]  1909
{Or     Code <Cd> [1..1] CodeSet 1909
Or}     Proprietary <Prtry> [1..1] ± 1910
Or   InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 1910
Or   InstructionProcessingStatus <InstrPrcgSts> [1..1]  1910
{Or     Code <Cd> [1..1] CodeSet 1910
Or}     Proprietary <Prtry> [1..1] ± 1912
Or   MatchingStatus <MtchgSts> [1..1] ± 1912
Or   RegistrationProcessingStatus <RegnPrcgSts> [1..1]  1913
{Or     Code <Cd> [1..1] CodeSet 1913
Or}     Proprietary <Prtry> [1..1] ± 1913
Or   ResponseStatus <RspnSts> [1..1]  1913
{Or     Code <Cd> [1..1] CodeSet 1914
Or}     Proprietary <Prtry> [1..1] ± 1914
Or   ReplacementProcessingStatus <RplcmntPrcgSts> [1..1]  1914
{Or     Code <Cd> [1..1] CodeSet 1915
Or}     Proprietary <Prtry> [1..1] ± 1915
Or   CancellationProcessingStatus <CxlPrcgSts> [1..1]  1916
{Or     Code <Cd> [1..1] CodeSet 1916
Or}     Proprietary <Prtry> [1..1] ± 1916
Or   SettlementStatus <SttlmSts> [1..1] ± 1917
Or}   SettlementConditionModificationStatus
<SttlmCondModSts>
[1..1]  1917
{Or     Code <Cd> [1..1] CodeSet 1917
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1906 March 2026
```

