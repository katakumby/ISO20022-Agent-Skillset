---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.064.001.01"
message_family: "camt.064"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"
source_ids: ["src-000233", "src-000363"]
source_locations: [{"source_id": "src-000233", "heading": "5 camt.064.001.01 LimitUtilisationJournalQueryV01", "file_pages": [68, 72]}, {"source_id": "src-000363", "heading": "2 camt.064.001.01 LimitUtilisationJournalQueryV01", "file_pages": [4, 8]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "february-2025"]
---

# camt.064.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 5 camt.064.001.01 LimitUtilisationJournalQueryV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp68–72; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 5 camt.064.001.01 LimitUtilisationJournalQueryV01, Functionality, file p68.**

The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a
directly connected system participant (the central securities depository participant granted direct
access, like a bank or a central counter party) and the central system. Its purpose is to query
information regarding the journal of transaction impacting the utilisation of limits that have been defined
by the system participant.
Outline
The LimitUtilisationJournalQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements used to provide information on the header of the message.
B. SearchCriteria
Provides criteria in the form of business attributes to define result set.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 camt.064.001.01 LimitUtilisationJournalQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00034.md) | 68–68 |
| [5 camt.064.001.01 LimitUtilisationJournalQueryV01 / 5.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00035.md) | 69–69 |
| [5 camt.064.001.01 LimitUtilisationJournalQueryV01 / 5.4 Message Building Blocks / 5.4.2 SearchCriteria &lt;SchCrit&gt; / 5.4.2.1 LimitType &lt;LmtTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00036.md) | 70–70 |
| [5 camt.064.001.01 LimitUtilisationJournalQueryV01 / 5.4 Message Building Blocks / 5.4.2 SearchCriteria &lt;SchCrit&gt; / 5.4.2.4 LimitCurrency &lt;LmtCcy&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00037.md) | 71–71 |
| [5 camt.064.001.01 LimitUtilisationJournalQueryV01 / 5.4 Message Building Blocks / 5.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00038.md) | 72–72 |

## src-000363 — 2 camt.064.001.01 LimitUtilisationJournalQueryV01

[src-000363](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`; file pp4–8; publication february-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000363, 2 camt.064.001.01 LimitUtilisationJournalQueryV01, Functionality, file p4.**

The LimitUtilisationJournalQuery message is exchanged between a central securities depository or a
directly connected system participant (the central securities depository participant granted direct
access, like a bank or a central counter party) and the central system. Its purpose is to query
information regarding the journal of transaction impacting the utilisation of limits that have been defined
by the system participant.
Outline
The LimitUtilisationJournalQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements used to provide information on the header of the message.
B. SearchCriteria
Provides criteria in the form of business attributes to define result set.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 camt.064.001.01 LimitUtilisationJournalQueryV01](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00004.md) | 4–4 |
| [2 camt.064.001.01 LimitUtilisationJournalQueryV01 / 2.3 Constraints](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00005.md) | 5–5 |
| [2 camt.064.001.01 LimitUtilisationJournalQueryV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.1 LimitType &lt;LmtTp&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00006.md) | 6–6 |
| [2 camt.064.001.01 LimitUtilisationJournalQueryV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.4 LimitCurrency &lt;LmtCcy&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00007.md) | 7–7 |
| [2 camt.064.001.01 LimitUtilisationJournalQueryV01 / 2.4 Message Building Blocks / 2.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00008.md) | 8–8 |

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
