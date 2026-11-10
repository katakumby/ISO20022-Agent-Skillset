---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.079.001.02"
message_family: "camt.079"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.079.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "file_pages": [381, 422]}, {"source_id": "src-000360", "heading": "10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "file_pages": [190, 231]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.079.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 17 camt.079.001.02 IntraBalanceMovementQueryResponseV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp381–422; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 17 camt.079.001.02 IntraBalanceMovementQueryResponseV02, Functionality, file p381.**

The IntraBalanceMovementQueryResponse message is sent from a settlement infrastructure to an
account owner/requestor to provide all intra-balance movement instructions satisfying the selection
criteria, as defined within the query, returning current attributes and latest status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementQueryResponseV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. ReportOrError
Provides information on report or error resulting from the originating query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 381 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00294.md) | 381–381 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00295.md) | 382–384 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00296.md) | 385–386 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00297.md) | 387–387 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.1 Identification &lt;Id&gt; / 17.4.1.3 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00298.md) | 388–388 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00299.md) | 389–389 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 17.4.3.1 QueryReference &lt;QryRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00300.md) | 390–392 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00301.md) | 393–395 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00302.md) | 396–396 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00303.md) | 397–397 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.4 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00304.md) | 398–398 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.4 StatusAndReason &lt;StsAndRsn&gt; / 17.4.4.1.4.2 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00305.md) | 399–399 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00306.md) | 400–402 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00307.md) | 403–403 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.3 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00308.md) | 404–404 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.4 StatusAndReason &lt;StsAndRsn&gt; / 17.4.4.1.5.4.2 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00309.md) | 405–405 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.5 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00310.md) | 406–406 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00311.md) | 407–408 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00312.md) | 409–409 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.1 BalanceFrom &lt;BalFr&gt; / 17.4.4.1.5.11.1.1 Type &lt;Tp&gt; / 17.4.4.1.5.11.1.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00313.md) | 410–410 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.1 BalanceFrom &lt;BalFr&gt; / 17.4.4.1.5.11.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 17.4.4.1.5.11.1.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00314.md) | 411–411 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.2 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00315.md) | 412–412 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.2 BalanceTo &lt;BalTo&gt; / 17.4.4.1.5.11.2.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00316.md) | 413–413 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.2 BalanceTo &lt;BalTo&gt; / 17.4.4.1.5.11.2.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 17.4.4.1.5.11.2.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00317.md) | 414–414 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.5 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00318.md) | 415–415 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.9 StatusDate &lt;StsDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00319.md) | 416–416 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.11 Linkages &lt;Lnkgs&gt; / 17.4.4.1.5.11.11.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00320.md) | 417–417 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.11 Linkages &lt;Lnkgs&gt; / 17.4.4.1.5.11.11.3 Reference &lt;Ref&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00321.md) | 418–418 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.11 Linkages &lt;Lnkgs&gt; / 17.4.4.1.5.11.11.3 Reference &lt;Ref&gt; / 17.4.4.1.5.11.11.3.3 IntraBalanceMovementIdentification &lt;IntraBalMvmntId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00322.md) | 419–419 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.1 Movements &lt;Mvmnts&gt; / 17.4.4.1.5 Movement &lt;Mvmnt&gt; / 17.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 17.4.4.1.5.11.12 Priority &lt;Prty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00323.md) | 420–420 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00324.md) | 421–421 |
| [17 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 17.4 Message Building Blocks / 17.4.4 ReportOrError &lt;RptOrErr&gt; / 17.4.4.2 OperationalError &lt;OprlErr&gt; / 17.4.4.2.2 Description &lt;Desc&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00325.md) | 422–422 |

## src-000360 — 10 camt.079.001.02 IntraBalanceMovementQueryResponseV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp190–231; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 10 camt.079.001.02 IntraBalanceMovementQueryResponseV02, Functionality, file p190.**

The IntraBalanceMovementQueryResponse message is sent from a settlement infrastructure to an
account owner/requestor to provide all intra-balance movement instructions satisfying the selection
criteria, as defined within the query, returning current attributes and latest status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementQueryResponseV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. ReportOrError
Provides information on report or error resulting from the originating query message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
190 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00159.md) | 190–190 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00160.md) | 191–193 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00161.md) | 194–195 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00162.md) | 196–196 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.1 Identification &lt;Id&gt; / 10.4.1.3 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00163.md) | 197–197 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00164.md) | 198–198 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.3 ReportGeneralDetails &lt;RptGnlDtls&gt; / 10.4.3.1 QueryReference &lt;QryRef&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00165.md) | 199–201 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00166.md) | 202–204 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00167.md) | 205–205 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.2 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00168.md) | 206–206 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.4 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00169.md) | 207–207 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.4 StatusAndReason &lt;StsAndRsn&gt; / 10.4.4.1.4.2 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00170.md) | 208–208 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00171.md) | 209–211 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.1 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00172.md) | 212–212 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.3 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00173.md) | 213–213 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.4 StatusAndReason &lt;StsAndRsn&gt; / 10.4.4.1.5.4.2 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00174.md) | 214–214 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.5 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00175.md) | 215–215 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00176.md) | 216–217 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00177.md) | 218–218 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.1 BalanceFrom &lt;BalFr&gt; / 10.4.4.1.5.11.1.1 Type &lt;Tp&gt; / 10.4.4.1.5.11.1.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00178.md) | 219–219 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.1 BalanceFrom &lt;BalFr&gt; / 10.4.4.1.5.11.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 10.4.4.1.5.11.1.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00179.md) | 220–220 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.2 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00180.md) | 221–221 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.2 BalanceTo &lt;BalTo&gt; / 10.4.4.1.5.11.2.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00181.md) | 222–222 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.2 BalanceTo &lt;BalTo&gt; / 10.4.4.1.5.11.2.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 10.4.4.1.5.11.2.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00182.md) | 223–223 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.5 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00183.md) | 224–224 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.9 StatusDate &lt;StsDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00184.md) | 225–225 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.11 Linkages &lt;Lnkgs&gt; / 10.4.4.1.5.11.11.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00185.md) | 226–226 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.11 Linkages &lt;Lnkgs&gt; / 10.4.4.1.5.11.11.3 Reference &lt;Ref&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00186.md) | 227–227 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.11 Linkages &lt;Lnkgs&gt; / 10.4.4.1.5.11.11.3 Reference &lt;Ref&gt; / 10.4.4.1.5.11.11.3.3 IntraBalanceMovementIdentification &lt;IntraBalMvmntId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00187.md) | 228–228 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.1 Movements &lt;Mvmnts&gt; / 10.4.4.1.5 Movement &lt;Mvmnt&gt; / 10.4.4.1.5.11 MovementDetails &lt;MvmntDtls&gt; / 10.4.4.1.5.11.12 Priority &lt;Prty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00188.md) | 229–229 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.2 OperationalError &lt;OprlErr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00189.md) | 230–230 |
| [10 camt.079.001.02 IntraBalanceMovementQueryResponseV02 / 10.4 Message Building Blocks / 10.4.4 ReportOrError &lt;RptOrErr&gt; / 10.4.4.2 OperationalError &lt;OprlErr&gt; / 10.4.4.2.2 Description &lt;Desc&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00190.md) | 231–231 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000359-central-counterparty.md) | participant | src-000359 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000359-central-securities-depositories-csd.md) | participant | src-000359 |
| [Central Securities Depositories](../../../../../shared/reference/participants/participant-src-000359-central-securities-depositories.md) | participant | src-000359 |
| [Central Securities Depository](../../../../../shared/reference/participants/participant-src-000359-central-securities-depository.md) | participant | src-000359 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | participant | src-000359 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | participant | src-000359 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000359-national-central-bank-ncb.md) | participant | src-000359 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000359-national-central-bank.md) | participant | src-000359 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000359-payment-bank.md) | participant | src-000359 |
| [Servicing/Executing Party Instructing Party](../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | participant | src-000359 |
| [Servicing/Executing Party](../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | participant | src-000359 |
| [Settlement Infrastructure Direct Participant](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure-direct-participant.md) | participant | src-000359 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md) | participant | src-000359 |
| [Stock Exchange](../../../../../shared/reference/participants/participant-src-000359-stock-exchange.md) | participant | src-000359 |
| [System Member](../../../../../shared/reference/participants/participant-src-000359-system-member.md) | participant | src-000359 |
| [System Transaction Administrator](../../../../../shared/reference/participants/participant-src-000359-system-transaction-administrator.md) | participant | src-000359 |
| [T2S operator](../../../../../shared/reference/participants/participant-src-000359-t2s-operator.md) | participant | src-000359 |
| [Third Party](../../../../../shared/reference/participants/participant-src-000359-third-party.md) | participant | src-000359 |
| [Movement Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p158-movement-process.md) | business-flow | src-000359 |
| [Status Advice Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p159-status-advice-process.md) | business-flow | src-000359 |
| [Confirmation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p160-confirmation-process.md) | business-flow | src-000359 |
| [Modification Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p161-modification-process.md) | business-flow | src-000359 |
| [Cancellation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p162-cancellation-process.md) | business-flow | src-000359 |
| [Modification/Cancellation Status Advice Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p164-modification-cancellation-status-advice-process.md) | business-flow | src-000359 |
| [Movement Querying Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p165-movement-querying-process.md) | business-flow | src-000359 |
| [Movement Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p166-movement-reporting-process.md) | business-flow | src-000359 |
| [Modification/Cancellation Query and Report Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p169-modification-cancellation-query-and-report-process.md) | business-flow | src-000359 |
| [Pending Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p170-pending-reporting-process.md) | business-flow | src-000359 |
| [Posting Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p171-posting-reporting-process.md) | business-flow | src-000359 |
| [External Scenario](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p189-external-scenario.md) | business-flow | src-000359 |
| [Internal Scenario](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) | business-flow | src-000359 |
| [Intra-Balance Movement Modification/Cancellation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p197-intra-balance-movement-modification-cancellation-process.md) | business-flow | src-000359 |
| [Push Mode](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) | business-flow | src-000359 |
| [Pull Mode](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p204-pull-mode.md) | business-flow | src-000359 |
| [Intra-Balance Movement Pending/Posting Report Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p208-intra-balance-movement-pending-posting-report-process.md) | business-flow | src-000359 |
| [Intra-Balance Movement Query/Response Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p211-intra-balance-movement-query-response-process.md) | business-flow | src-000359 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
