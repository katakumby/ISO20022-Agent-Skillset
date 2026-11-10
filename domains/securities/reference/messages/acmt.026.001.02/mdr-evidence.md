---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.026.001.02"
message_family: "acmt.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02"
source_ids: ["src-000351"]
source_locations: [{"source_id": "src-000351", "heading": "3 acmt.026.001.02 AccountListReportV02", "file_pages": [48, 107]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["august-2026"]
---

# acmt.026.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000351 — 3 acmt.026.001.02 AccountListReportV02

[src-000351](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`; file pp48–107; publication august-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000351, 3 acmt.026.001.02 AccountListReportV02, Functionality, file p48.**

This message is sent in response to a query message, and contains the list of requested accounts, with
requested characteristics.
Outline
The AccountListReportV02 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. References
Set of elements for the identification of the message and related references.
B. AccountServicerIdentification
Unique and unambiguous identifier of a financial institution, as assigned under an internationally
recognised or proprietary identification scheme.
C. Organisation
Organised structure that is set up for a particular purpose, for example, a business, government
body, department, charity, or financial institution.
D. ReportOrError
Contains the requested report, or the error that occurred during processing.
E. DigitalSignature
Contains the signature with its components, namely signed info, signature value, key info and the
object.
F. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 48 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 acmt.026.001.02 AccountListReportV02](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00044.md) | 48–48 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.2 Structure](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00045.md) | 49–52 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.3 Constraints](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00046.md) | 53–53 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00047.md) | 54–54 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.1 References &lt;Refs&gt; / 3.4.1.1 RequestType &lt;ReqTp&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00048.md) | 55–55 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.1 References &lt;Refs&gt; / 3.4.1.4 AcknowledgedMessageIdentification &lt;AckdMsgId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00049.md) | 56–56 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00050.md) | 57–57 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.1 FullLegalName &lt;FullLglNm&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00051.md) | 58–58 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.3 CountryOfOperation &lt;CtryOfOpr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00052.md) | 59–59 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.6 BusinessAddress &lt;BizAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00053.md) | 60–60 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.7 LegalAddress &lt;LglAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00054.md) | 61–61 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.8 BillingAddress &lt;BllgAdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00055.md) | 62–62 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.9 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00056.md) | 63–63 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.9 OrganisationIdentification &lt;OrgId&gt; / 3.4.3.9.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00057.md) | 64–64 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.9 OrganisationIdentification &lt;OrgId&gt; / 3.4.3.9.3 Other &lt;Othr&gt; / 3.4.3.9.3.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00058.md) | 65–65 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.11 TreasuryManager &lt;TrsrMgr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00059.md) | 66–66 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.12 MainMandateHolder &lt;MainMndtHldr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00060.md) | 67–67 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.13 Sender &lt;Sndr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00061.md) | 68–68 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.3 Organisation &lt;Org&gt; / 3.4.3.14 LegalRepresentative &lt;LglRprtv&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00062.md) | 69–69 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00063.md) | 70–73 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.1 Error &lt;Err&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00064.md) | 74–74 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00065.md) | 75–78 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00066.md) | 79–80 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00067.md) | 81–81 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.5 Currency &lt;Ccy&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00068.md) | 82–82 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.11 AccountPurpose &lt;AcctPurp&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00069.md) | 83–83 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.14 StatementFrequencyAndFormat &lt;StmtFrqcyAndFrmt&gt; / 3.4.4.2.1.14.2 CommunicationMethod &lt;ComMtd&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00070.md) | 84–84 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.14 StatementFrequencyAndFormat &lt;StmtFrqcyAndFrmt&gt; / 3.4.4.2.1.14.2 CommunicationMethod &lt;ComMtd&gt; / 3.4.4.2.1.14.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00071.md) | 85–85 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.16 Restriction &lt;Rstrctn&gt; / 3.4.4.2.1.16.1 RestrictionType &lt;RstrctnTp&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00072.md) | 86–86 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.1 Account &lt;Acct&gt; / 3.4.4.2.1.16 Restriction &lt;Rstrctn&gt; / 3.4.4.2.1.16.3 ValidUntil &lt;VldUntil&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00073.md) | 87–87 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.3 ContractDates &lt;CtrctDts&gt; / 3.4.4.2.3.1 TargetGoLiveDate &lt;TrgtGoLiveDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00074.md) | 88–88 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.3 ContractDates &lt;CtrctDts&gt; / 3.4.4.2.3.6 RemovalIndicator &lt;RmvlInd&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00075.md) | 89–89 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00076.md) | 90–90 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.2 ApplicableChannel &lt;AplblChanl&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00077.md) | 91–91 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.5 MandateHolder &lt;MndtHldr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00078.md) | 92–92 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.5 MandateHolder &lt;MndtHldr&gt; / 3.4.4.2.4.5.1 PartyOrGroup &lt;PtyOrGrp&gt; / 3.4.4.2.4.5.1.2 Party &lt;Pty&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00079.md) | 93–93 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.5 MandateHolder &lt;MndtHldr&gt; / 3.4.4.2.4.5.1 PartyOrGroup &lt;PtyOrGrp&gt; / 3.4.4.2.4.5.1.2 Party &lt;Pty&gt; / 3.4.4.2.4.5.1.2.2 Certificate &lt;Cert&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00080.md) | 94–94 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.5 MandateHolder &lt;MndtHldr&gt; / 3.4.4.2.4.5.2 SignatureOrder &lt;SgntrOrdr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00081.md) | 95–95 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.5 MandateHolder &lt;MndtHldr&gt; / 3.4.4.2.4.5.3 Authorisation &lt;Authstn&gt; / 3.4.4.2.4.5.3.1 MaximumAmountByTransaction &lt;MaxAmtByTx&gt; / 3.4.4.2.4.5.3.1.2 NotLimited &lt;NotLtd&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00082.md) | 96–96 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.5 MandateHolder &lt;MndtHldr&gt; / 3.4.4.2.4.5.3 Authorisation &lt;Authstn&gt; / 3.4.4.2.4.5.3.2 MaximumAmountByPeriod &lt;MaxAmtByPrd&gt; / 3.4.4.2.4.5.3.2.2 NumberOfDays &lt;NbOfDays&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00083.md) | 97–97 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.4 Mandate &lt;Mndt&gt; / 3.4.4.2.4.7 StartDate &lt;StartDt&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00084.md) | 98–98 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.6 BalanceTransferAccount &lt;BalTrfAcct&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00085.md) | 99–99 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.6 BalanceTransferAccount &lt;BalTrfAcct&gt; / 3.4.4.2.6.2 Currency &lt;Ccy&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00086.md) | 100–100 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.8 AccountOwner &lt;AcctOwnr&gt; / 3.4.4.2.8.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00087.md) | 101–101 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.8 AccountOwner &lt;AcctOwnr&gt; / 3.4.4.2.8.3 Other &lt;Othr&gt; / 3.4.4.2.8.3.1 Identification &lt;Id&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00088.md) | 102–102 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.10 Group &lt;Grp&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00089.md) | 103–103 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.4 ReportOrError &lt;RptOrErr&gt; / 3.4.4.2 AccountReport &lt;AcctRpt&gt; / 3.4.4.2.10 Group &lt;Grp&gt; / 3.4.4.2.10.2 Party &lt;Pty&gt; / 3.4.4.2.10.2.2 Certificate &lt;Cert&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00090.md) | 104–104 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.5 DigitalSignature &lt;DgtlSgntr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00091.md) | 105–105 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.5 DigitalSignature &lt;DgtlSgntr&gt; / 3.4.5.2 Signature &lt;Sgntr&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00092.md) | 106–106 |
| [3 acmt.026.001.02 AccountListReportV02 / 3.4 Message Building Blocks / 3.4.6 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00093.md) | 107–107 |

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
