---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.065.001.01"
message_family: "camt.065"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01"
source_ids: ["src-000233", "src-000363"]
source_locations: [{"source_id": "src-000233", "heading": "6 camt.065.001.01 LimitUtilisationJournalReportV01", "file_pages": [73, 92]}, {"source_id": "src-000363", "heading": "3 camt.065.001.01 LimitUtilisationJournalReportV01", "file_pages": [9, 28]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "february-2025"]
---

# camt.065.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 6 camt.065.001.01 LimitUtilisationJournalReportV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp73–92; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 6 camt.065.001.01 LimitUtilisationJournalReportV01, Functionality, file p73.**

The LimitUtilisationJournalReport message is exchanged between the central system and a central
securities depository or a directly connected system party (the central securities depository participant
granted direct access, like a bank or central counter party) and is used to return information about the
limit. Its purpose is to report information regarding the journal of transactions impacting the utilisation of
limits that have been defined by the system participant.
Outline
The LimitUtilisationJournalReportV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Set of elements used to provide information on the header of the message.
B. Pagination
Pagination of the message.
Usage: the pagination of the message is only allowed when agreed between the parties.
C. ReportOrError
Provides information on report or error resulting from the originating query message.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 73 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00039.md) | 73–73 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00040.md) | 74–74 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00041.md) | 75–75 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00042.md) | 76–76 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00043.md) | 77–78 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00044.md) | 79–80 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.1 LimitIdentification &lt;LmtId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00045.md) | 81–81 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.1 LimitIdentification &lt;LmtId&gt; / 6.4.3.1.1.3 LimitCurrency &lt;LmtCcy&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00046.md) | 82–82 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00047.md) | 83–83 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00048.md) | 84–84 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 6.4.3.1.2.1.1 Limit &lt;Lmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00049.md) | 85–85 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 6.4.3.1.2.1.1 Limit &lt;Lmt&gt; / 6.4.3.1.2.1.1.1 Amount &lt;Amt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00050.md) | 86–86 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 6.4.3.1.2.1.1 Limit &lt;Lmt&gt; / 6.4.3.1.2.1.1.2 UtilisationAmount &lt;UtlstnAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00051.md) | 87–87 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 6.4.3.1.2.1.1 Limit &lt;Lmt&gt; / 6.4.3.1.2.1.1.3 AvailableAmount &lt;AvlblAmt&gt; / 6.4.3.1.2.1.1.3.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00052.md) | 88–88 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 6.4.3.1.2.1.3 JournalEntry &lt;JrnlNtry&gt; / 6.4.3.1.2.1.3.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00053.md) | 89–89 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 6.4.3.1.2.1.3 JournalEntry &lt;JrnlNtry&gt; / 6.4.3.1.2.1.3.7 ProcessorTransactionIdentification &lt;PrcrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00054.md) | 90–90 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.3 ReportOrError &lt;RptOrErr&gt; / 6.4.3.1 BusinessReport &lt;BizRpt&gt; / 6.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 6.4.3.1.2.2 BusinessError &lt;BizErr&gt; / 6.4.3.1.2.2.2 Description &lt;Desc&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00055.md) | 91–91 |
| [6 camt.065.001.01 LimitUtilisationJournalReportV01 / 6.4 Message Building Blocks / 6.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00056.md) | 92–92 |

## src-000363 — 3 camt.065.001.01 LimitUtilisationJournalReportV01

[src-000363](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`; file pp9–28; publication february-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000363, 3 camt.065.001.01 LimitUtilisationJournalReportV01, Functionality, file p9.**

The LimitUtilisationJournalReport message is exchanged between the central system and a central
securities depository or a directly connected system party (the central securities depository participant
granted direct access, like a bank or central counter party) and is used to return information about the
limit. Its purpose is to report information regarding the journal of transactions impacting the utilisation of
limits that have been defined by the system participant.
Outline
The LimitUtilisationJournalReportV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Set of elements used to provide information on the header of the message.
B. Pagination
Pagination of the message.
Usage: the pagination of the message is only allowed when agreed between the parties.
C. ReportOrError
Provides information on report or error resulting from the originating query message.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 9 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00009.md) | 9–9 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.2 Structure](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00010.md) | 10–10 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.3 Constraints](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00011.md) | 11–11 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00012.md) | 12–12 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00013.md) | 13–14 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00014.md) | 15–16 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.1 LimitIdentification &lt;LmtId&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00015.md) | 17–17 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.1 LimitIdentification &lt;LmtId&gt; / 3.4.3.1.1.3 LimitCurrency &lt;LmtCcy&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00016.md) | 18–18 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00017.md) | 19–19 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00018.md) | 20–20 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 3.4.3.1.2.1.1 Limit &lt;Lmt&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00019.md) | 21–21 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 3.4.3.1.2.1.1 Limit &lt;Lmt&gt; / 3.4.3.1.2.1.1.1 Amount &lt;Amt&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00020.md) | 22–22 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 3.4.3.1.2.1.1 Limit &lt;Lmt&gt; / 3.4.3.1.2.1.1.2 UtilisationAmount &lt;UtlstnAmt&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00021.md) | 23–23 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 3.4.3.1.2.1.1 Limit &lt;Lmt&gt; / 3.4.3.1.2.1.1.3 AvailableAmount &lt;AvlblAmt&gt; / 3.4.3.1.2.1.1.3.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00022.md) | 24–24 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 3.4.3.1.2.1.3 JournalEntry &lt;JrnlNtry&gt; / 3.4.3.1.2.1.3.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00023.md) | 25–25 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.1 LimitJournal &lt;LmtJrnl&gt; / 3.4.3.1.2.1.3 JournalEntry &lt;JrnlNtry&gt; / 3.4.3.1.2.1.3.7 ProcessorTransactionIdentification &lt;PrcrTxId&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00024.md) | 26–26 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.3 ReportOrError &lt;RptOrErr&gt; / 3.4.3.1 BusinessReport &lt;BizRpt&gt; / 3.4.3.1.2 LimitReport &lt;LmtRpt&gt; / 3.4.3.1.2.2 BusinessError &lt;BizErr&gt; / 3.4.3.1.2.2.2 Description &lt;Desc&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00025.md) | 27–27 |
| [3 camt.065.001.01 LimitUtilisationJournalReportV01 / 3.4 Message Building Blocks / 3.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00026.md) | 28–28 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000362-central-counterparty.md) | participant | src-000362 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000362-central-securities-depositories-csd.md) | participant | src-000362 |
| [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000362-direct-connected-participant-dcp.md) | participant | src-000362 |
| [Executing/Servicing Party (T2S in this case)](../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party-t2s-in-this-case.md) | participant | src-000362 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000362-executing-servicing-party.md) | participant | src-000362 |
| [Instructing Party (Subscriber to receive the report)](../../../../../shared/reference/participants/participant-src-000362-instructing-party-subscriber-to-receive-the-report.md) | participant | src-000362 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000362-instructing-party.md) | participant | src-000362 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000362-national-central-bank-ncb.md) | participant | src-000362 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000362-payment-bank.md) | participant | src-000362 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000362-settlement-infrastructure.md) | participant | src-000362 |
| [T2S Operator](../../../../../shared/reference/participants/participant-src-000362-t2s-operator.md) | participant | src-000362 |
| [Query Report Process](../../message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p132-query-report-process.md) | business-flow | src-000362 |
| [Pull mode](../../message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md) | business-flow | src-000362 |
| [Push mode](../../message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p143-push-mode.md) | business-flow | src-000362 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
