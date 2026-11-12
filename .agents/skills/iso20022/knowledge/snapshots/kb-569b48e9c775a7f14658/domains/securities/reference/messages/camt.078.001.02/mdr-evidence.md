---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.078.001.02"
message_family: "camt.078"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.078.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "16 camt.078.001.02 IntraBalanceMovementQueryV02", "file_pages": [341, 380]}, {"source_id": "src-000360", "heading": "9 camt.078.001.02 IntraBalanceMovementQueryV02", "file_pages": [150, 189]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.078.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 16 camt.078.001.02 IntraBalanceMovementQueryV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp341–380; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 16 camt.078.001.02 IntraBalanceMovementQueryV02, Functionality, file p341.**

The IntraBalanceMovementQuery message is sent from an account owner/requestor to a settlement
infrastructure to query intra-balance movement instructions, along with their current status, based on a
set of search criteria.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementQueryV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement instruction query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 341 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00262.md) | 341–341 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00263.md) | 342–344 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00264.md) | 345–345 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00265.md) | 346–346 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.1 Identification &lt;Id&gt; / 16.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00266.md) | 347–347 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00267.md) | 348–351 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00268.md) | 352–355 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.1 References &lt;Refs&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00269.md) | 356–356 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.1 References &lt;Refs&gt; / 16.4.2.2.1.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00270.md) | 357–357 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.2 Status &lt;Sts&gt; / 16.4.2.2.2.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00271.md) | 358–358 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.2 Status &lt;Sts&gt; / 16.4.2.2.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00272.md) | 359–359 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.2 Status &lt;Sts&gt; / 16.4.2.2.2.2 DatePeriod &lt;DtPrd&gt; / 16.4.2.2.2.2.1 Date &lt;Dt&gt; / 16.4.2.2.2.2.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00273.md) | 360–360 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.2 Status &lt;Sts&gt; / 16.4.2.2.2.2 DatePeriod &lt;DtPrd&gt; / 16.4.2.2.2.2.2 DateTime &lt;DtTm&gt; / 16.4.2.2.2.2.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00274.md) | 361–361 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.3 CashAccount &lt;CshAcct&gt; / 16.4.2.2.3.2 ContainText &lt;CTTxt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00275.md) | 362–362 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00276.md) | 363–363 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt; / 16.4.2.2.6.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00277.md) | 364–364 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt; / 16.4.2.2.6.1 BalanceFrom &lt;BalFr&gt; / 16.4.2.2.6.1.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00278.md) | 365–365 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt; / 16.4.2.2.6.1 BalanceFrom &lt;BalFr&gt; / 16.4.2.2.6.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00279.md) | 366–366 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt; / 16.4.2.2.6.1 BalanceFrom &lt;BalFr&gt; / 16.4.2.2.6.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 16.4.2.2.6.1.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00280.md) | 367–367 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt; / 16.4.2.2.6.2 BalanceTo &lt;BalTo&gt; / 16.4.2.2.6.2.1 Type &lt;Tp&gt; / 16.4.2.2.6.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00281.md) | 368–368 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.6 BalanceType &lt;BalTp&gt; / 16.4.2.2.6.2 BalanceTo &lt;BalTo&gt; / 16.4.2.2.6.2.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 16.4.2.2.6.2.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00282.md) | 369–369 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.7 CashSubBalanceIdentification &lt;CshSubBalId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00283.md) | 370–370 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.10 SettlementCurrency &lt;SttlmCcy&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00284.md) | 371–371 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.11 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 16.4.2.2.11.1 Date &lt;Dt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00285.md) | 372–372 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.11 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 16.4.2.2.11.1 Date &lt;Dt&gt; / 16.4.2.2.11.1.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00286.md) | 373–373 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.11 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 16.4.2.2.11.2 DateTime &lt;DtTm&gt; / 16.4.2.2.11.2.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00287.md) | 374–374 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.12 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 16.4.2.2.12.1 Date &lt;Dt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00288.md) | 375–375 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.12 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 16.4.2.2.12.1 Date &lt;Dt&gt; / 16.4.2.2.12.1.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00289.md) | 376–376 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.12 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 16.4.2.2.12.2 DateTime &lt;DtTm&gt; / 16.4.2.2.12.2.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00290.md) | 377–377 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.15 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00291.md) | 378–378 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.15 CreationDateTime &lt;CreDtTm&gt; / 16.4.2.2.15.1 Date &lt;Dt&gt; / 16.4.2.2.15.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00292.md) | 379–379 |
| [16 camt.078.001.02 IntraBalanceMovementQueryV02 / 16.4 Message Building Blocks / 16.4.2 QueryDefinition &lt;QryDef&gt; / 16.4.2.2 SearchCriteria &lt;SchCrit&gt; / 16.4.2.2.15 CreationDateTime &lt;CreDtTm&gt; / 16.4.2.2.15.2 DateTime &lt;DtTm&gt; / 16.4.2.2.15.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00293.md) | 380–380 |

## src-000360 — 9 camt.078.001.02 IntraBalanceMovementQueryV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp150–189; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 9 camt.078.001.02 IntraBalanceMovementQueryV02, Functionality, file p150.**

The IntraBalanceMovementQuery message is sent from an account owner/requestor to a settlement
infrastructure to query intra-balance movement instructions, along with their current status, based on a
set of search criteria.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementQueryV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement instruction query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
150 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00127.md) | 150–150 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00128.md) | 151–153 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00129.md) | 154–154 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00130.md) | 155–155 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.1 Identification &lt;Id&gt; / 9.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00131.md) | 156–156 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00132.md) | 157–160 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00133.md) | 161–164 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.1 References &lt;Refs&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00134.md) | 165–165 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.1 References &lt;Refs&gt; / 9.4.2.2.1.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00135.md) | 166–166 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.2 Status &lt;Sts&gt; / 9.4.2.2.2.1 Type &lt;Tp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00136.md) | 167–167 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.2 Status &lt;Sts&gt; / 9.4.2.2.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00137.md) | 168–168 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.2 Status &lt;Sts&gt; / 9.4.2.2.2.2 DatePeriod &lt;DtPrd&gt; / 9.4.2.2.2.2.1 Date &lt;Dt&gt; / 9.4.2.2.2.2.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00138.md) | 169–169 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.2 Status &lt;Sts&gt; / 9.4.2.2.2.2 DatePeriod &lt;DtPrd&gt; / 9.4.2.2.2.2.2 DateTime &lt;DtTm&gt; / 9.4.2.2.2.2.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00139.md) | 170–170 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.3 CashAccount &lt;CshAcct&gt; / 9.4.2.2.3.2 ContainText &lt;CTTxt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00140.md) | 171–171 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00141.md) | 172–172 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt; / 9.4.2.2.6.1 BalanceFrom &lt;BalFr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00142.md) | 173–173 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt; / 9.4.2.2.6.1 BalanceFrom &lt;BalFr&gt; / 9.4.2.2.6.1.1 Type &lt;Tp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00143.md) | 174–174 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt; / 9.4.2.2.6.1 BalanceFrom &lt;BalFr&gt; / 9.4.2.2.6.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00144.md) | 175–175 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt; / 9.4.2.2.6.1 BalanceFrom &lt;BalFr&gt; / 9.4.2.2.6.1.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 9.4.2.2.6.1.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00145.md) | 176–176 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt; / 9.4.2.2.6.2 BalanceTo &lt;BalTo&gt; / 9.4.2.2.6.2.1 Type &lt;Tp&gt; / 9.4.2.2.6.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00146.md) | 177–177 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.6 BalanceType &lt;BalTp&gt; / 9.4.2.2.6.2 BalanceTo &lt;BalTo&gt; / 9.4.2.2.6.2.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 9.4.2.2.6.2.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00147.md) | 178–178 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.7 CashSubBalanceIdentification &lt;CshSubBalId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00148.md) | 179–179 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.10 SettlementCurrency &lt;SttlmCcy&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00149.md) | 180–180 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.11 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 9.4.2.2.11.1 Date &lt;Dt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00150.md) | 181–181 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.11 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 9.4.2.2.11.1 Date &lt;Dt&gt; / 9.4.2.2.11.1.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00151.md) | 182–182 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.11 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 9.4.2.2.11.2 DateTime &lt;DtTm&gt; / 9.4.2.2.11.2.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00152.md) | 183–183 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.12 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 9.4.2.2.12.1 Date &lt;Dt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00153.md) | 184–184 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.12 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 9.4.2.2.12.1 Date &lt;Dt&gt; / 9.4.2.2.12.1.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00154.md) | 185–185 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.12 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 9.4.2.2.12.2 DateTime &lt;DtTm&gt; / 9.4.2.2.12.2.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00155.md) | 186–186 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.15 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00156.md) | 187–187 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.15 CreationDateTime &lt;CreDtTm&gt; / 9.4.2.2.15.1 Date &lt;Dt&gt; / 9.4.2.2.15.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00157.md) | 188–188 |
| [9 camt.078.001.02 IntraBalanceMovementQueryV02 / 9.4 Message Building Blocks / 9.4.2 QueryDefinition &lt;QryDef&gt; / 9.4.2.2 SearchCriteria &lt;SchCrit&gt; / 9.4.2.2.15 CreationDateTime &lt;CreDtTm&gt; / 9.4.2.2.15.2 DateTime &lt;DtTm&gt; / 9.4.2.2.15.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00158.md) | 189–189 |

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
