---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.021.001.01"
message_family: "reda.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.021.001.01"
source_ids: ["src-000233", "src-000372"]
source_locations: [{"source_id": "src-000233", "heading": "41 reda.021.001.01 SecuritiesAccountReportV01", "file_pages": [2124, 2139]}, {"source_id": "src-000372", "heading": "5 reda.021.001.01 SecuritiesAccountReportV01", "file_pages": [32, 47]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2019"]
---

# reda.021.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 41 reda.021.001.01 SecuritiesAccountReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp2124–2139; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 41 reda.021.001.01 SecuritiesAccountReportV01, Functionality, file p2124.**

The SecuritiesAccountReport message sent by the executing party to an instructing party to provide the
details of the securities account details as requested in the query.
Outline
The SecuritiesAccountReportV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the report message.
B. Pagination
Provides details on the page number of the message.
C. ReportOrError
Provides information on report or error resulting from the originating query message.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2124 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [41 reda.021.001.01 SecuritiesAccountReportV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01505.md) | 2124–2124 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01506.md) | 2125–2125 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01507.md) | 2126–2126 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01508.md) | 2127–2128 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01509.md) | 2129–2129 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.1 SecuritiesAccountIdentification &lt;SctiesAcctId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01510.md) | 2130–2130 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01511.md) | 2131–2131 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01512.md) | 2132–2132 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 41.4.3.1.2.1.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01513.md) | 2133–2133 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 41.4.3.1.2.1.4 NegativePosition &lt;NegPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01514.md) | 2134–2134 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 41.4.3.1.2.1.5 Type &lt;Tp&gt; / 41.4.3.1.2.1.5.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01515.md) | 2135–2135 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 41.4.3.1.2.1.7 PartyType &lt;PtyTp&gt; / 41.4.3.1.2.1.7.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01516.md) | 2136–2136 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 41.4.3.1.2.1.9 Restriction &lt;Rstrctn&gt; / 41.4.3.1.2.1.9.2 ValidTo &lt;VldTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01517.md) | 2137–2137 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 41.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 41.4.3.1.2.2 BusinessError &lt;BizErr&gt; / 41.4.3.1.2.2.1 Error &lt;Err&gt; / 41.4.3.1.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01518.md) | 2138–2138 |
| [41 reda.021.001.01 SecuritiesAccountReportV01 / 41.4 Message Building Blocks / 41.4.3 ReportOrError &lt;RptOrErr&gt; / 41.4.3.2 OperationalError &lt;OprlErr&gt; / 41.4.3.2.1 Error &lt;Err&gt; / 41.4.3.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01519.md) | 2139–2139 |

## src-000372 — 5 reda.021.001.01 SecuritiesAccountReportV01

[src-000372](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`; file pp32–47; publication december-2019. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000372, 5 reda.021.001.01 SecuritiesAccountReportV01, Functionality, file p32.**

The SecuritiesAccountReport message sent by the executing party to an instructing party to provide the
details of the securities account details as requested in the query.
Outline
The SecuritiesAccountReportV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Point to point reference elements, as assigned by the instructing party, to unambiguously identify
the report message.
B. Pagination
Provides details on the page number of the message.
C. ReportOrError
Provides information on report or error resulting from the originating query message.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities - Securities Account Reference Data 32 December 2019

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 reda.021.001.01 SecuritiesAccountReportV01](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00029.md) | 32–32 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.2 Structure](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00030.md) | 33–33 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.3 Constraints](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00031.md) | 34–34 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00032.md) | 35–36 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00033.md) | 37–37 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.1 SecuritiesAccountIdentification &lt;SctiesAcctId&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00034.md) | 38–38 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00035.md) | 39–39 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00036.md) | 40–40 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 5.4.3.1.2.1.1 OpeningDate &lt;OpngDt&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00037.md) | 41–41 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 5.4.3.1.2.1.4 NegativePosition &lt;NegPos&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00038.md) | 42–42 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 5.4.3.1.2.1.5 Type &lt;Tp&gt; / 5.4.3.1.2.1.5.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00039.md) | 43–43 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 5.4.3.1.2.1.7 PartyType &lt;PtyTp&gt; / 5.4.3.1.2.1.7.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00040.md) | 44–44 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.1 SecuritiesAccount &lt;SctiesAcct&gt; / 5.4.3.1.2.1.9 Restriction &lt;Rstrctn&gt; / 5.4.3.1.2.1.9.2 ValidTo &lt;VldTo&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00041.md) | 45–45 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.1 SecuritiesAccountReport &lt;SctiesAcctRpt&gt; / 5.4.3.1.2 SecuritiesAccountOrError &lt;SctiesAcctOrErr&gt; / 5.4.3.1.2.2 BusinessError &lt;BizErr&gt; / 5.4.3.1.2.2.1 Error &lt;Err&gt; / 5.4.3.1.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00042.md) | 46–46 |
| [5 reda.021.001.01 SecuritiesAccountReportV01 / 5.4 Message Building Blocks / 5.4.3 ReportOrError &lt;RptOrErr&gt; / 5.4.3.2 OperationalError &lt;OprlErr&gt; / 5.4.3.2.1 Error &lt;Err&gt; / 5.4.3.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-securities-account-reference-data/december-2019/documents/src-000372/sections/section-00043.md) | 47–47 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Bank](../../../../../shared/reference/participants/participant-src-000371-bank.md) | participant | src-000371 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000371-central-securities-depositories-csd.md) | participant | src-000371 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000371-corporate.md) | participant | src-000371 |
| [CSD](../../../../../shared/reference/participants/participant-src-000371-csd.md) | participant | src-000371 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000371-executing-servicing-party.md) | participant | src-000371 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000371-instructing-party.md) | participant | src-000371 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000371-market-data-provider.md) | participant | src-000371 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000371-market-infrastructure.md) | participant | src-000371 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000371-national-central-bank-ncb.md) | participant | src-000371 |
| [Create Securities Account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p152-create-securities-account.md) | business-flow | src-000371 |
| [Delete Securities Account](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p155-delete-securities-account.md) | business-flow | src-000371 |
| [Query](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md) | business-flow | src-000371 |
| [Generate Statement](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p157-generate-statement.md) | business-flow | src-000371 |
| [Creation Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p162-creation-process.md) | business-flow | src-000371 |
| [Modification Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p164-modification-process.md) | business-flow | src-000371 |
| [Deletion Process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p166-deletion-process.md) | business-flow | src-000371 |
| [Query/Query Response process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p169-query-query-response-process.md) | business-flow | src-000371 |
| [Statement process](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p172-statement-process.md) | business-flow | src-000371 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- SECACCOUNT-FLOWS -->
## Securities account reference flows

- [Query securities account data or audit trail](../../message-sets/t2s-securities-account-reference-data/december-2019/flows/flow-src-000371-p156-query.md)
