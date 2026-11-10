---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "shared"
message_id: "admi.005.001.02"
message_family: "admi.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.005.001.02"
source_ids: ["src-000233", "src-000344"]
source_locations: [{"source_id": "src-000233", "heading": "2 admi.005.001.02 ReportQueryRequestV02", "file_pages": [34, 56]}, {"source_id": "src-000344", "heading": "2 admi.005.001.02 ReportQueryRequestV02", "file_pages": [4, 26]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# admi.005.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 2 admi.005.001.02 ReportQueryRequestV02

[src-000233](../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp34–56; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 2 admi.005.001.02 ReportQueryRequestV02, Functionality, file p34.**

The ReportQueryRequest message is exchanged between system member and system transaction
administrator.
It aims at querying the latest available report data of a specific report type. A report is stored and
available for query until the event occurs again report is replaced.
Outline
The ReportQueryRequestV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the report query request message.
B. ReportQueryCriteria
Definition of the report query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 34 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 admi.005.001.02 ReportQueryRequestV02](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00007.md) | 34–34 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.2 Structure](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00008.md) | 35–36 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.3 Constraints](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00009.md) | 37–37 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00010.md) | 38–39 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.1 NewQueryName &lt;NewQryNm&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00011.md) | 40–41 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.1 AccountIdentification &lt;AcctId&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00012.md) | 42–42 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.1 AccountIdentification &lt;AcctId&gt; / 2.4.2.2.1.1 Equal &lt;EQ&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00013.md) | 43–44 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.1 Type &lt;Tp&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00014.md) | 45–45 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.3 CounterpartyIdentification &lt;CtrPtyId&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00015.md) | 46–46 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.4.1 DateTime &lt;DtTm&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00016.md) | 47–47 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.4.1 DateTime &lt;DtTm&gt; / 2.4.2.2.2.4.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00017.md) | 48–48 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.4.2 Date &lt;Dt&gt; / 2.4.2.2.2.4.2.3 FromToDate &lt;FrToDt&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00018.md) | 49–49 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.5.1 DateTime &lt;DtTm&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00019.md) | 50–50 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.5.1 DateTime &lt;DtTm&gt; / 2.4.2.2.2.5.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00020.md) | 51–51 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.5.2 Date &lt;Dt&gt; / 2.4.2.2.2.5.2.3 FromToDate &lt;FrToDt&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00021.md) | 52–52 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.6 ResponsiblePartyIdentification &lt;RspnsblPtyId&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00022.md) | 53–53 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.7 DateSearch &lt;DtSch&gt; / 2.4.2.2.7.4 EqualDate &lt;EQDt&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00023.md) | 54–54 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.9 Event &lt;Evt&gt;](../../../../domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00024.md) | 55–56 |

## src-000344 — 2 admi.005.001.02 ReportQueryRequestV02

[src-000344](../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`; file pp4–26; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000344, 2 admi.005.001.02 ReportQueryRequestV02, Functionality, file p4.**

The ReportQueryRequest message is exchanged between system member and system transaction
administrator.
It aims at querying the latest available report data of a specific report type. A report is stored and
available for query until the event occurs again report is replaced.
Outline
The ReportQueryRequestV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the report query request message.
B. ReportQueryCriteria
Definition of the report query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
4 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-administration/march-2024/documents/src-000344/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 admi.005.001.02 ReportQueryRequestV02](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00004.md) | 4–4 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.2 Structure](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00005.md) | 5–6 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.3 Constraints](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00006.md) | 7–7 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00007.md) | 8–9 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00008.md) | 10–11 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00009.md) | 12–12 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.1 AccountIdentification &lt;AcctId&gt; / 2.4.2.2.1.1 Equal &lt;EQ&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00010.md) | 13–14 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.1 Type &lt;Tp&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00011.md) | 15–15 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.3 CounterpartyIdentification &lt;CtrPtyId&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00012.md) | 16–16 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.4.1 DateTime &lt;DtTm&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00013.md) | 17–17 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.4.1 DateTime &lt;DtTm&gt; / 2.4.2.2.2.4.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00014.md) | 18–18 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.4.2 Date &lt;Dt&gt; / 2.4.2.2.2.4.2.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00015.md) | 19–19 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.5.1 DateTime &lt;DtTm&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00016.md) | 20–20 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.5.1 DateTime &lt;DtTm&gt; / 2.4.2.2.2.5.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00017.md) | 21–21 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2 Balance &lt;Bal&gt; / 2.4.2.2.2.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.5.2 Date &lt;Dt&gt; / 2.4.2.2.2.5.2.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00018.md) | 22–22 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.6 ResponsiblePartyIdentification &lt;RspnsblPtyId&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00019.md) | 23–23 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.7 DateSearch &lt;DtSch&gt; / 2.4.2.2.7.4 EqualDate &lt;EQDt&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00020.md) | 24–24 |
| [2 admi.005.001.02 ReportQueryRequestV02 / 2.4 Message Building Blocks / 2.4.2 ReportQueryCriteria &lt;RptQryCrit&gt; / 2.4.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.9 Event &lt;Evt&gt;](../../message-sets/t2s-administration/march-2024/documents/src-000344/sections/section-00021.md) | 25–26 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Securities Depositories (CSD)](../../participants/participant-src-000343-central-securities-depositories-csd.md) | participant | src-000343 |
| [Executing/Servicing Party](../../participants/participant-src-000343-executing-servicing-party.md) | participant | src-000343 |
| [Instructing Party](../../participants/participant-src-000343-instructing-party.md) | participant | src-000343 |
| [National Central Bank (NCB)](../../participants/participant-src-000343-national-central-bank-ncb.md) | participant | src-000343 |
| [National Central Bank](../../participants/participant-src-000343-national-central-bank.md) | participant | src-000343 |
| [Payment Bank](../../participants/participant-src-000343-payment-bank.md) | participant | src-000343 |
| [Settlement Infrastructure Direct Participant](../../participants/participant-src-000343-settlement-infrastructure-direct-participant.md) | participant | src-000343 |
| [Settlement Infrastructure](../../participants/participant-src-000343-settlement-infrastructure.md) | participant | src-000343 |
| [System Member](../../participants/participant-src-000343-system-member.md) | participant | src-000343 |
| [System Transaction Administrator](../../participants/participant-src-000343-system-transaction-administrator.md) | participant | src-000343 |
| [T2S operator](../../participants/participant-src-000343-t2s-operator.md) | participant | src-000343 |
| [t2s-administration-clearing-member-role](../../participants/t2s-administration-clearing-member-role.md) | participant | src-000345 |
| [t2s-administration-identification-issuer-role](../../participants/t2s-administration-identification-issuer-role.md) | participant | src-000345 |
| [t2s-administration-information-party-role](../../participants/t2s-administration-information-party-role.md) | participant | src-000345 |
| [t2s-administration-system-party-role](../../participants/t2s-administration-system-party-role.md) | participant | src-000345 |
| [Report query process](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p126-report-query-process.md) | business-flow | src-000343 |
| [Resent Request Process](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p136-resent-request-process.md) | business-flow | src-000343 |
| [Receipt Acknowledgement Process](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p143-receipt-acknowledgement-process.md) | business-flow | src-000343 |
| [Report Query Request (admi.005)](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md) | business-flow | src-000343 |
| [Resend Request (admi.006)](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p154-resend-request-admi-006.md) | business-flow | src-000343 |
| [Scenario 1a](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p162-scenario-1a.md) | business-flow | src-000343 |
| [Scenario 1b](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p168-scenario-1b.md) | business-flow | src-000343 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../tracking/issues.md)


<!-- ADMIN-FLOWS -->
## Administration business flows

- [Report query request activity](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p149-report-query-request-admi-005.md)
- [Query the latest available report](../../message-sets/t2s-administration/march-2024/flows/flow-src-000343-p175-report-query-request-business-transaction-admi-005.md)
