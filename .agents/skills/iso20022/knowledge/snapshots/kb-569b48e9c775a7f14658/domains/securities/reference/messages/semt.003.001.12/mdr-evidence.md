---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.003.001.12"
message_family: "semt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.003.001.12"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "file_pages": [78, 134]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.003.001.12 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 3 semt.003.001.12 SecuritiesBalanceAccountingReportV12

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp78–134; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 3 semt.003.001.12 SecuritiesBalanceAccountingReportV12, Functionality, file p78.**

Scope
An account servicer sends a SecuritiesBalanceAccountingReport to an account owner to provide, at a
moment in time, valuations of the portfolio together with details of each financial instrument holding.
The account servicer/owner relationship may be:
- an accounting agent acting on behalf of an account owner, or
- a transfer agent acting on behalf of a fund manager or an account owner's designated agent.
Usage
The message should be sent at a frequency agreed bi-laterally between the account servicer and the
account owner.
The message can be sent either audited or un-audited and may be provided on a trade date,
contractual or settlement date basis.
This message can only be used to list the holdings of a single (master) account. However, it is possible
to break down these holdings into one or several sub-accounts. Therefore, the message can be used to
either specify holdings at
- the main account level, or,
- the sub-account level.
This message can be used to report where the financial instruments are safe-kept, physically or
notionally. If a security is held in more than one safekeeping place, this can also be indicated.
The SecuritiesBalanceAccountingReport message should not be used for trading purposes.
There may be one or more intermediary parties, for example, an intermediary or a concentrator
between the account owner and account servicer.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 78 March 2026

**src-000197, 3 semt.003.001.12 SecuritiesBalanceAccountingReportV12, Functionality, file p79.**

The SecuritiesBalanceAccountingReportV12 MessageDefinition is composed of 11
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
Provides general information on the report.
C. AccountOwner
Party that legally owns the account.
D. AccountServicer
Party that manages the account on behalf of the account owner, that is, manages the registration
and booking of entries on the account, calculates balances on the account and provides
information about the account.
E. SafekeepingAccount
Account to or from which a securities entry is made.
F. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
G. IntermediaryInformation
Information about the party that provides services relating to financial products to investors, for
example, advice on products and placement of orders for the investment fund.
H. BalanceForAccount
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
I. SubAccountDetails
Sub-account of the safekeeping or investment account.
J. AccountBaseCurrencyTotalAmounts
Total valuation amounts provided in the base currency of the account.
K. AlternateReportingCurrencyTotalAmounts
Total valuation amounts provided in a currency other than the base currency of the account.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 79 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00050.md) | 78–79 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00051.md) | 80–82 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00052.md) | 83–86 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00053.md) | 87–87 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00054.md) | 88–88 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.4 AccountServicer &lt;AcctSvcr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00055.md) | 89–89 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.7 IntermediaryInformation &lt;IntrmyInf&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00056.md) | 90–91 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00057.md) | 92–92 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.2 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00058.md) | 93–94 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.3 InvestmentFundsFinancialInstrumentAttributes &lt;InvstmtFndsFinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00059.md) | 95–95 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.4 AdditionalDerivativeAttributes &lt;AddtlDerivAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00060.md) | 96–96 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.7 CorporateActionOptionType &lt;CorpActnOptnTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00061.md) | 97–97 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.9 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00062.md) | 98–98 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.13 AlternateReportingCurrencyAmounts &lt;AltrnRptgCcyAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00063.md) | 99–99 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.15 BalanceBreakdown &lt;BalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00064.md) | 100–100 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00065.md) | 101–101 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.1 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00066.md) | 102–102 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.2 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00067.md) | 103–103 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.4 AggregateBalance &lt;AggtBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00068.md) | 104–104 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.6 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00069.md) | 105–105 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.9 InstrumentCurrencyAmounts &lt;InstrmCcyAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00070.md) | 106–106 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.12 ExposureType &lt;XpsrTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00071.md) | 107–107 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.8.17.14 AdditionalBalanceBreakdown &lt;AddtlBalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00072.md) | 108–108 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.8 BalanceForAccount &lt;BalForAcct&gt; / 3.4.8.19 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00073.md) | 109–111 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00074.md) | 112–112 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.4 ActivityIndicator &lt;ActvtyInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00075.md) | 113–114 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00076.md) | 115–115 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.2 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00077.md) | 116–117 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.3 InvestmentFundsFinancialInstrumentAttributes &lt;InvstmtFndsFinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00078.md) | 118–118 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.4 AdditionalDerivativeAttributes &lt;AddtlDerivAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00079.md) | 119–119 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.7 CorporateActionOptionType &lt;CorpActnOptnTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00080.md) | 120–120 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.9 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00081.md) | 121–121 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.13 AlternateReportingCurrencyAmounts &lt;AltrnRptgCcyAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00082.md) | 122–122 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.15 BalanceBreakdown &lt;BalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00083.md) | 123–123 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00084.md) | 124–124 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.1 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00085.md) | 125–125 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.2 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00086.md) | 126–126 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.4 AggregateBalance &lt;AggtBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00087.md) | 127–127 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.6 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00088.md) | 128–128 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.9 InstrumentCurrencyAmounts &lt;InstrmCcyAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00089.md) | 129–129 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.12 ExposureType &lt;XpsrTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00090.md) | 130–130 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.17 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 3.4.9.5.17.14 AdditionalBalanceBreakdown &lt;AddtlBalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00091.md) | 131–131 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 3.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 3.4.9.5.19 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00092.md) | 132–132 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.10 AccountBaseCurrencyTotalAmounts &lt;AcctBaseCcyTtlAmts&gt; / 3.4.10.2 TotalHoldingsValueOfStatement &lt;TtlHldgsValOfStmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00093.md) | 133–133 |
| [3 semt.003.001.12 SecuritiesBalanceAccountingReportV12 / 3.4 Message Building Blocks / 3.4.11 AlternateReportingCurrencyTotalAmounts &lt;AltrnRptgCcyTtlAmts&gt; / 3.4.11.2 TotalHoldingsValueOfStatement &lt;TtlHldgsValOfStmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00094.md) | 134–134 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md) | participant | src-000196, src-000197, src-000198 |
| [Account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md) | participant | src-000196, src-000197, src-000198 |
| [Buy Side Party](../../../../../shared/reference/participants/settlement-reconciliation-buy-side-party.md) | participant | src-000196 |
| [Central Counterparty](../../../../../shared/reference/participants/settlement-reconciliation-central-counterparty.md) | participant | src-000196 |
| [Confirmation Party](../../../../../shared/reference/participants/settlement-reconciliation-confirmation-party.md) | participant | src-000196 |
| [CSD / ICSD](../../../../../shared/reference/participants/settlement-reconciliation-csd-icsd.md) | participant | src-000196 |
| [Executing/servicing party](../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md) | participant | src-000196 |
| [Global Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-global-settlement-agent.md) | participant | src-000196 |
| [Instructing party](../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md) | participant | src-000196 |
| [Local Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-local-settlement-agent.md) | participant | src-000196 |
| [Portfolio transfer client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md) | participant | src-000196 |
| [Third party in securities reporting](../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md) | participant | src-000196 |
| [Sell Side Party](../../../../../shared/reference/participants/settlement-reconciliation-sell-side-party.md) | participant | src-000196 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md) | participant | src-000196 |
| [Stock Exchange](../../../../../shared/reference/participants/settlement-reconciliation-stock-exchange.md) | participant | src-000196 |
| [Cancellation advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md) | business-flow | src-000196 |
| [Cancellation request](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md) | business-flow | src-000196 |
| [Instruction and confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md) | business-flow | src-000196 |
| [Partial settlement confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md) | business-flow | src-000196 |
| [Portfolio transfer](../../message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md) | business-flow | src-000196 |
| [Reconciliation and reporting: pull mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md) | business-flow | src-000196 |
| [Reconciliation and reporting: push mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md) | business-flow | src-000196 |
| [Settlement reversal advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md) | business-flow | src-000196 |
| [Transaction generation notification](../../message-sets/settlement-and-reconciliation/2025-2026/flows/transaction-generation.md) | business-flow | src-000196 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
