---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.025.001.02"
message_family: "acmt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02"
source_ids: ["src-000351"]
source_locations: [{"source_id": "src-000351", "heading": "2 acmt.025.001.02 AccountQueryListV02", "file_pages": [4, 47]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["august-2026"]
---

# acmt.025.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000351 — 2 acmt.025.001.02 AccountQueryListV02

[src-000351](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`; file pp4–47; publication august-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000351, 2 acmt.025.001.02 AccountQueryListV02, Functionality, file p4.**

This message is a query message with specification of requested accounts, and requested
characteristics.
Outline
The AccountQueryListV02 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. References
Set of elements for the identification of the message and related references.
B. From
Identifies the business sender of the message, if it is not the account owner or account servicing
financial institution.
C. AccountServicerIdentification
Unique and unambiguous identifier of a financial institution, as assigned under an internationally
recognised or proprietary identification scheme.
.
D. Organisation
Organised structure that is set up for a particular purpose, for example, a business, government
body, department, charity, or financial institution.
E. AccountSearchCriteria
Contains the criteria that must be used to select the requested accounts.
F. AccountReturnCriteria
Contains the characteristics of the selected accounts that must be returned.
G. DigitalSignature
Contains the signature with its components, namely signed info, signature value, key info and the
object.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 4 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 acmt.025.001.02 AccountQueryListV02](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00004.md) | 4–4 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.2 Structure](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00005.md) | 5–8 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.3 Constraints](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00006.md) | 9–9 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.1 References &lt;Refs&gt; / 2.4.1.2 ProcessIdentification &lt;PrcId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00007.md) | 10–10 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.2 From &lt;Fr&gt; / 2.4.2.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00008.md) | 11–11 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.2 From &lt;Fr&gt; / 2.4.2.3 Other &lt;Othr&gt; / 2.4.2.3.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00009.md) | 12–12 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.3 AccountServicerIdentification &lt;AcctSvcrId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00010.md) | 13–13 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.1 FullLegalName &lt;FullLglNm&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00011.md) | 14–14 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.3 CountryOfOperation &lt;CtryOfOpr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00012.md) | 15–15 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.6 BusinessAddress &lt;BizAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00013.md) | 16–16 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.7 LegalAddress &lt;LglAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00014.md) | 17–17 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.8 BillingAddress &lt;BllgAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00015.md) | 18–18 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.9 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00016.md) | 19–19 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.9 OrganisationIdentification &lt;OrgId&gt; / 2.4.4.9.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00017.md) | 20–20 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.9 OrganisationIdentification &lt;OrgId&gt; / 2.4.4.9.3 Other &lt;Othr&gt; / 2.4.4.9.3.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00018.md) | 21–21 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.11 TreasuryManager &lt;TrsrMgr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00019.md) | 22–22 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.12 MainMandateHolder &lt;MainMndtHldr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00020.md) | 23–23 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.13 Sender &lt;Sndr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00021.md) | 24–24 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.4 Organisation &lt;Org&gt; / 2.4.4.14 LegalRepresentative &lt;LglRprtv&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00022.md) | 25–25 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00023.md) | 26–27 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00024.md) | 28–28 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.2 Name &lt;Nm&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00025.md) | 29–29 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.6 Proxy &lt;Prxy&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00026.md) | 30–30 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.10 MaximumMonthlyReceivedValue &lt;MaxMnthlyRcvdVal&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00027.md) | 31–31 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.18 MinimumCeilingNotificationAmount &lt;MinClngNtfctnAmt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00028.md) | 32–32 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.20 StatementFrequencyAndFormat &lt;StmtFrqcyAndFrmt&gt; / 2.4.5.20.2 CommunicationMethod &lt;ComMtd&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00029.md) | 33–33 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.20 StatementFrequencyAndFormat &lt;StmtFrqcyAndFrmt&gt; / 2.4.5.20.3 DeliveryAddress &lt;DlvryAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00030.md) | 34–34 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.21 Restriction &lt;Rstrctn&gt; / 2.4.5.21.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00031.md) | 35–35 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.22 ClosingDate &lt;ClsgDt&gt; / 2.4.5.22.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00032.md) | 36–36 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.23 OpeningDate &lt;OpngDt&gt; / 2.4.5.23.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00033.md) | 37–37 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.24 ReferenceAccountIdentification &lt;RefAcctId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00034.md) | 38–38 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.26 AccountOwner &lt;AcctOwnr&gt; / 2.4.5.26.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00035.md) | 39–39 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.5 AccountSearchCriteria &lt;AcctSchCrit&gt; / 2.4.5.26 AccountOwner &lt;AcctOwnr&gt; / 2.4.5.26.3 Other &lt;Othr&gt; / 2.4.5.26.3.2 SchemeName &lt;SchmeNm&gt; / 2.4.5.26.3.2.1 Code &lt;Cd&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00036.md) | 40–40 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.6 AccountReturnCriteria &lt;AcctRtrCrit&gt; / 2.4.6.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00037.md) | 41–41 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.6 AccountReturnCriteria &lt;AcctRtrCrit&gt; / 2.4.6.3 Status &lt;Sts&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00038.md) | 42–42 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.6 AccountReturnCriteria &lt;AcctRtrCrit&gt; / 2.4.6.8 MonthlyTransactionNumber &lt;MnthlyTxNb&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00039.md) | 43–43 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.6 AccountReturnCriteria &lt;AcctRtrCrit&gt; / 2.4.6.13 StatementCycle &lt;StmtCycl&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00040.md) | 44–44 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.6 AccountReturnCriteria &lt;AcctRtrCrit&gt; / 2.4.6.19 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00041.md) | 45–45 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.7 DigitalSignature &lt;DgtlSgntr&gt; / 2.4.7.2 Signature &lt;Sgntr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00042.md) | 46–46 |
| [2 acmt.025.001.02 AccountQueryListV02 / 2.4 Message Building Blocks / 2.4.8 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00043.md) | 47–47 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000350-account-owner.md) | participant | src-000350 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000350-account-servicer.md) | participant | src-000350 |
| [Central Database System](../../../../../shared/reference/participants/participant-src-000350-central-database-system.md) | participant | src-000350 |
| [Central Securities Depository (CSD)](../../../../../shared/reference/participants/participant-src-000350-central-securities-depository-csd.md) | participant | src-000350 |
| [Central Security Depository (CSD)](../../../../../shared/reference/participants/participant-src-000350-central-security-depository-csd.md) | participant | src-000350 |
| [Collateral Management System](../../../../../shared/reference/participants/participant-src-000350-collateral-management-system.md) | participant | src-000350 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000350-executing-servicing-party.md) | participant | src-000350 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000350-instructing-party.md) | participant | src-000350 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000350-market-infrastructure.md) | participant | src-000350 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000350-national-central-bank.md) | participant | src-000350 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000350-payment-bank.md) | participant | src-000350 |
| [Account Query List](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p123-account-query-list.md) | business-flow | src-000350 |
| [Cash Account Audit Trail Query](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p124-cash-account-audit-trail-query.md) | business-flow | src-000350 |
| [Cash Account Activity Advice](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p125-cash-account-activity-advice.md) | business-flow | src-000350 |
| [Account Query List - Account List Response process](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p130-account-query-list-account-list-response-process.md) | business-flow | src-000350 |
| [Cash Account Activity Advice process](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p135-cash-account-activity-advice-process.md) | business-flow | src-000350 |
| [Cash Account Audit Trail Query/Response process](../../message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p140-cash-account-audit-trail-query-response-process.md) | business-flow | src-000350 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
