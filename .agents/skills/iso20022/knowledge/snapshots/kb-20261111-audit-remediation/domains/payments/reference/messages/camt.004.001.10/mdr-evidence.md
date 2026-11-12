---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.004.001.10"
message_family: "camt.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "3 camt.004.001.10 ReturnAccountV10", "file_pages": [48, 97]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.004.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 3 camt.004.001.10 ReturnAccountV10

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp48–97; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 3 camt.004.001.10 ReturnAccountV10, Functionality, file p48.**

Scope
The ReturnAccount message is sent by the transaction administrator to a member.
It is used to provide information on the details of one or more accounts held at the transaction
administrator, including information on the balances.
The Return Account message can be sent as a response to a related GetAccount message (pull mode)
or initiated by the transaction administrator (push mode). The push of information can take place either
at prearranged times or as a warning or alarm when a problem has occurred.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the account(s) that the transaction administrator maintains for the
member.
For example, this may be necessary in order to perform the appropriate liquidity management and the
necessary funds transfers between accounts.
The member can request information about accounts through a series of criteria, corresponding to the
known information stored at the transaction administrator.
The query can concern one or more specific accounts, accounts of a particular identification, or a
particular type. The purpose of the query may be to obtain one or more types of balance.
The transaction administrator may also send a ReturnAccount message with pre-defined information, at
times previously agreed with the member, or to warn the member about a particular problem that may
have arisen and which needs attention.
The message from the transaction administrator can contain information based on the following
elements:
- account identification
- account name
- account type (this is used when the account identification represents, for example, a group of
accounts)
- currency of the account (this is used for example when the account identification represents a group of
account in various currencies, or when it is a multi-currency account with one single identifier)
- type of balance (if not present in the GetAccount message, all balances will be reported)
- bilateral or multilateral limits
- related counterparty (when the limit or balance is bilateral)
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 48 February 2025

**src-000015, 3 camt.004.001.10 ReturnAccountV10, Functionality, file p49.**

- balance value date (if not present in the GetAccount message, the ReturnAccount message will
contain the latest available balance)
- number of payments to the additional account information on the generic design of the Get/Return
messages can be found in the section How to Use the Cash Management Messages.
Outline
The ReturnAccountV10 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on accounts.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 49 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 camt.004.001.10 ReturnAccountV10](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00028.md) | 48–49 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00029.md) | 50–51 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00030.md); [Constraints continuation C2–C11 (file p53)](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00031.md#file-page-53) | 52–52 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00031.md) | 53–53 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00032.md) | 54–56 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00033.md) | 57–59 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00034.md) | 60–62 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00035.md) | 63–65 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.1 Name &lt;Nm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00036.md) | 66–66 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.4 Proxy &lt;Prxy&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00037.md) | 67–67 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.5 CurrentMultilateralLimit &lt;CurMulLmt&gt; / 3.4.2.1.2.1.5.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00038.md) | 68–68 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.7 Servicer &lt;Svcr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00039.md) | 69–69 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.8 MultilateralBalance &lt;MulBal&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00040.md) | 70–70 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.9 CurrentBilateralLimit &lt;CurBilLmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00041.md) | 71–71 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.9 CurrentBilateralLimit &lt;CurBilLmt&gt; / 3.4.2.1.2.1.9.1 CounterpartyIdentification &lt;CtrPtyId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00042.md) | 72–72 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.9 CurrentBilateralLimit &lt;CurBilLmt&gt; / 3.4.2.1.2.1.9.2 LimitAmount &lt;LmtAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00043.md) | 73–73 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.9 CurrentBilateralLimit &lt;CurBilLmt&gt; / 3.4.2.1.2.1.9.4 BilateralBalance &lt;BilBal&gt; / 3.4.2.1.2.1.9.4.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00044.md) | 74–78 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.9 CurrentBilateralLimit &lt;CurBilLmt&gt; / 3.4.2.1.2.1.9.4 BilateralBalance &lt;BilBal&gt; / 3.4.2.1.2.1.9.4.3 Type &lt;Tp&gt; / 3.4.2.1.2.1.9.4.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00045.md) | 79–79 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.9 CurrentBilateralLimit &lt;CurBilLmt&gt; / 3.4.2.1.2.1.9.4 BilateralBalance &lt;BilBal&gt; / 3.4.2.1.2.1.9.4.4 Status &lt;Sts&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00046.md) | 80–81 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.1 Amount &lt;Amt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00047.md) | 82–82 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.4 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00048.md) | 83–83 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.5 AssociatedPoolAccount &lt;AssoctdPoolAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00049.md) | 84–84 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.8 ValidityPeriod &lt;VldtyPrd&gt; / 3.4.2.1.2.1.10.8.1 FromDate &lt;FrDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00050.md) | 85–85 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.11 LinkSetIdentification &lt;LkSetId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00051.md) | 86–86 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.14 ExecutionType &lt;ExctnTp&gt; / 3.4.2.1.2.1.10.14.1 Time &lt;Tm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00052.md) | 87–87 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.16 CreditorAccount &lt;CdtrAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00053.md) | 88–88 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.17 Debtor &lt;Dbtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00054.md) | 89–89 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00055.md) | 90–90 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 3.4.2.1.2.1.10.19.1 SetPredefinedOrder &lt;SetPrdfndOrdr&gt; / 3.4.2.1.2.1.10.19.1.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00056.md) | 91–91 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 3.4.2.1.2.1.10.19.2 PendingPredefinedOrder &lt;PdgPrdfndOrdr&gt; / 3.4.2.1.2.1.10.19.2.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00057.md) | 92–92 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 3.4.2.1.2.1.10.19.3 SetStandingOrder &lt;SetStgOrdr&gt; / 3.4.2.1.2.1.10.19.3.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00058.md) | 93–93 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.1 Account &lt;Acct&gt; / 3.4.2.1.2.1.10 StandingOrder &lt;StgOrdr&gt; / 3.4.2.1.2.1.10.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 3.4.2.1.2.1.10.19.4 PendingStandingOrder &lt;PdgStgOrdr&gt; / 3.4.2.1.2.1.10.19.4.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00059.md) | 94–94 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.1 AccountReport &lt;AcctRpt&gt; / 3.4.2.1.2 AccountOrError &lt;AcctOrErr&gt; / 3.4.2.1.2.2 BusinessError &lt;BizErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00060.md) | 95–95 |
| [3 camt.004.001.10 ReturnAccountV10 / 3.4 Message Building Blocks / 3.4.2 ReportOrError &lt;RptOrErr&gt; / 3.4.2.2 OperationalError &lt;OprlErr&gt; / 3.4.2.2.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00061.md) | 96–97 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [ACH](../../../../../shared/reference/participants/participant-src-000014-ach.md) | participant | src-000014 |
| [Automated Clearing House (ACH)](../../../../../shared/reference/participants/participant-src-000014-automated-clearing-house-ach.md) | participant | src-000014 |
| [Cash Provider](../../../../../shared/reference/participants/participant-src-000014-cash-provider.md) | participant | src-000014 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000014-central-securities-depositories-csd.md) | participant | src-000014 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000014-corporate.md) | participant | src-000014 |
| [CSD](../../../../../shared/reference/participants/participant-src-000014-csd.md) | participant | src-000014 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | participant | src-000014 |
| [Real Time Gross Settlement System (RTGS)](../../../../../shared/reference/participants/participant-src-000014-real-time-gross-settlement-system-rtgs.md) | participant | src-000014 |
| [RTGS](../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | participant | src-000014 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000014-settlement-agent.md) | participant | src-000014 |
| [System Member](../../../../../shared/reference/participants/participant-src-000014-system-member.md) | participant | src-000014 |
| [System / Transaction Administrator](../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | participant | src-000014 |
| [Transaction Administrator/System](../../../../../shared/reference/participants/participant-src-000014-transaction-administrator-system.md) | participant | src-000014 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- CASH-FLOWS -->
## Operational Cash Management flows

- [Get/Return Account](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p261-get-return-account.md)
- [Get/Return Account Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p266-get-return-account-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
