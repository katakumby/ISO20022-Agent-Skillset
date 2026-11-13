---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.029.001.01"
message_family: "semt.029"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.029.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "file_pages": [2612, 2641]}, {"source_id": "src-000381", "heading": "3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "file_pages": [57, 86]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.029.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 74 semt.029.001.01 IntraPositionMovementQueryResponseV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2612–2641; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 74 semt.029.001.01 IntraPositionMovementQueryResponseV01, Functionality, file p2612.**

The IntraPositionMovementQueryResponse message is sent from a settlement infrastructure to an
account owner/requestor to provide all intra-position movement instructions satisfying the selection
criteria, as defined within the query, returning current attributes and latest status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementQueryResponseV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. Movements
Identifies the intra-position movements.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2612 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01907.md) | 2612–2612 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01908.md) | 2613–2614 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01909.md); [Constraints continuation C20–C25 (file p2617)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01910.md#file-page-2617) | 2615–2616 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01910.md) | 2617–2617 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 74.4.2.1 QueryReference &lt;QryRef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01911.md) | 2618–2618 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01912.md) | 2619–2621 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01913.md) | 2622–2622 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.3 StatusAndReason &lt;StsAndRsn&gt; / 74.4.3.3.2 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01914.md) | 2623–2623 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01915.md) | 2624–2625 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01916.md) | 2626–2626 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.2 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01917.md) | 2627–2627 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.3 StatusAndReason &lt;StsAndRsn&gt; / 74.4.3.4.3.3 Settled &lt;Sttld&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01918.md) | 2628–2628 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.6 MarketInfrastructureTransactionIdentification &lt;MktInfrstrctrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01919.md) | 2629–2630 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01920.md) | 2631–2631 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.4 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01921.md) | 2632–2633 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.5 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01922.md) | 2634–2634 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.7 PreviouslySettledQuantity &lt;PrevslySttldQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01923.md) | 2635–2635 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.10 EffectiveSettlementDate &lt;FctvSttlmDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01924.md) | 2636–2636 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.13 Linkages &lt;Lnkgs&gt; / 74.4.3.4.10.13.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01925.md) | 2637–2637 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.13 Linkages &lt;Lnkgs&gt; / 74.4.3.4.10.13.3 Reference &lt;Ref&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01926.md) | 2638–2638 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.13 Linkages &lt;Lnkgs&gt; / 74.4.3.4.10.13.3 Reference &lt;Ref&gt; / 74.4.3.4.10.13.3.3 IntraBalanceMovementIdentification &lt;IntraBalMvmntId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01927.md) | 2639–2639 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.14 SecuritiesSubBalanceIdentification &lt;SctiesSubBalId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01928.md) | 2640–2640 |
| [74 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 74.4 Message Building Blocks / 74.4.3 Movements &lt;Mvmnts&gt; / 74.4.3.4 Movement &lt;Mvmnt&gt; / 74.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 74.4.3.4.10.17 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01929.md) | 2641–2641 |

## src-000381 — 3 semt.029.001.01 IntraPositionMovementQueryResponseV01

[src-000381](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp57–86; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 3 semt.029.001.01 IntraPositionMovementQueryResponseV01, Functionality, file p57.**

The IntraPositionMovementQueryResponse message is sent from a settlement infrastructure to an
account owner/requestor to provide all intra-position movement instructions satisfying the selection
criteria, as defined within the query, returning current attributes and latest status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementQueryResponseV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. Movements
Identifies the intra-position movements.
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 57 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00043.md) | 57–57 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00044.md) | 58–59 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00045.md); [Constraints continuation C20–C25 (file p62)](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00046.md#file-page-62) | 60–61 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00046.md) | 62–62 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 3.4.2.1 QueryReference &lt;QryRef&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00047.md) | 63–63 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00048.md) | 64–66 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00049.md) | 67–67 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.3 StatusAndReason &lt;StsAndRsn&gt; / 3.4.3.3.2 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00050.md) | 68–68 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00051.md) | 69–70 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00052.md) | 71–71 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.2 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00053.md) | 72–72 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.3 StatusAndReason &lt;StsAndRsn&gt; / 3.4.3.4.3.3 Settled &lt;Sttld&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00054.md) | 73–73 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.6 MarketInfrastructureTransactionIdentification &lt;MktInfrstrctrTxId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00055.md) | 74–75 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00056.md) | 76–76 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.4 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00057.md) | 77–78 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.5 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00058.md) | 79–79 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.7 PreviouslySettledQuantity &lt;PrevslySttldQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00059.md) | 80–80 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.10 EffectiveSettlementDate &lt;FctvSttlmDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00060.md) | 81–81 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.13 Linkages &lt;Lnkgs&gt; / 3.4.3.4.10.13.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00061.md) | 82–82 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.13 Linkages &lt;Lnkgs&gt; / 3.4.3.4.10.13.3 Reference &lt;Ref&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00062.md) | 83–83 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.13 Linkages &lt;Lnkgs&gt; / 3.4.3.4.10.13.3 Reference &lt;Ref&gt; / 3.4.3.4.10.13.3.3 IntraBalanceMovementIdentification &lt;IntraBalMvmntId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00063.md) | 84–84 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.14 SecuritiesSubBalanceIdentification &lt;SctiesSubBalId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00064.md) | 85–85 |
| [3 semt.029.001.01 IntraPositionMovementQueryResponseV01 / 3.4 Message Building Blocks / 3.4.3 Movements &lt;Mvmnts&gt; / 3.4.3.4 Movement &lt;Mvmnt&gt; / 3.4.3.4.10 MovementDetails &lt;MvmntDtls&gt; / 3.4.3.4.10.17 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00065.md) | 86–86 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000380-central-counterparty.md) | participant | src-000380 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md) | participant | src-000380 |
| [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md) | participant | src-000380 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md) | participant | src-000380 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | participant | src-000380 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md) | participant | src-000380 |
| [T2S Operator](../../../../../shared/reference/participants/participant-src-000380-t2s-operator.md) | participant | src-000380 |
| [Query Report Process](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p253-query-report-process.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md) | business-flow | src-000380 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
