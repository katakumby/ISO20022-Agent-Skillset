---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.7 DeniedReason16Choice", "17.1.16.7.2 Proprietary <Prtry>"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.7.2 Proprietary <Prtry>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
DCAN DeniedSinceAlreadyCancelled Cancellation request was denied since
the instruction has already been
cancelled.
DPRG DeniedSinceInProgress Cancellation request was denied
because the process of settlement is in
progress.
DREP DeniedSinceRepoEnded Cancellation request was denied
because the repo was cancelled.
DSET DeniedSinceAlreadySettled Cancellation request was denied
because the instruction was already
settled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
17.1.16.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.8  DeniedStatus16Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 435
Or}   Reason <Rsn> [1..*]  435
     Code <Cd> [1..1] ± 435
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 435
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
434 March 2024
```

