---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.002.001.12"
message_family: "semt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.002.001.12"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "file_pages": [19, 77]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.002.001.12 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 2 semt.002.001.12 SecuritiesBalanceCustodyReportV12

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp19–77; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 2 semt.002.001.12 SecuritiesBalanceCustodyReportV12, Functionality, file p19.**

Scope
An account servicer sends a SecuritiesBalanceCustodyReport to an account owner to provide, at a
moment in time, the quantity and identification of the financial instruments that the account servicer
holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants, or
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer, or
- a transfer agent acting on behalf of a fund manager or an account owner's designated agent.
Usage
The message can also include availability and the location of holdings to facilitate trading and minimise
settlement issues. The message reports all information per financial instrument, that is, when a financial
instrument is held at multiple places of safekeeping, the total holdings for all locations can be provided.
The message should be sent at a frequency agreed bi-laterally between the account servicer and the
account owner. The message may be provided on a trade date, contractual or settlement date basis.
There may be one or more intermediary parties, for example, an intermediary or a concentrator
between the account owner and account servicer.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesBalanceCustodyReportV12 MessageDefinition is composed of 10
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 19 March 2026

**src-000197, 2 semt.002.001.12 SecuritiesBalanceCustodyReportV12, Functionality, file p20.**

B. StatementGeneralDetails
Provides general information on the report.
C. AccountOwner
Party that legally owns the account.
D. AccountServicer
Party that manages the account on behalf of the account owner, that is manages the registration
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
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 20 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00005.md) | 19–20 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00006.md) | 21–23 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00007.md) | 24–27 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00008.md) | 28–28 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00009.md) | 29–29 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.5 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00010.md) | 30–30 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00011.md) | 31–32 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00012.md) | 33–33 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.2 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00013.md) | 34–36 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.3 InvestmentFundsFinancialInstrumentAttributes &lt;InvstmtFndsFinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00014.md) | 37–37 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.4 ValuationHaircutDetails &lt;ValtnHrcutDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00015.md) | 38–38 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.7 NotAvailableBalance &lt;NotAvlblBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00016.md) | 39–39 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.10 PriceDetails &lt;PricDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00017.md) | 40–40 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.13 AccountBaseCurrencyAmounts &lt;AcctBaseCcyAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00018.md) | 41–41 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.15 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00019.md) | 42–42 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.17 AdditionalBalanceBreakdown &lt;AddtlBalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00020.md) | 43–43 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.1 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00021.md) | 44–44 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.2 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00022.md) | 45–45 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.4 AggregateBalance &lt;AggtBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00023.md) | 46–46 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.6 NotAvailableBalance &lt;NotAvlblBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00024.md) | 47–47 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.9 DaysAccrued &lt;DaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00025.md) | 48–48 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.12 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00026.md) | 49–49 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.14 BalanceBreakdown &lt;BalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00027.md) | 50–50 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.8 BalanceForAccount &lt;BalForAcct&gt; / 2.4.8.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.8.18.16 HoldingAdditionalDetails &lt;HldgAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00028.md) | 51–54 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00029.md) | 55–55 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.4 ActivityIndicator &lt;ActvtyInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00030.md) | 56–57 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00031.md) | 58–58 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.2 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00032.md) | 59–60 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.3 InvestmentFundsFinancialInstrumentAttributes &lt;InvstmtFndsFinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00033.md) | 61–61 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.4 ValuationHaircutDetails &lt;ValtnHrcutDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00034.md) | 62–62 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.7 NotAvailableBalance &lt;NotAvlblBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00035.md) | 63–63 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.10 PriceDetails &lt;PricDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00036.md) | 64–64 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.13 AccountBaseCurrencyAmounts &lt;AcctBaseCcyAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00037.md) | 65–65 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.15 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00038.md) | 66–66 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.17 AdditionalBalanceBreakdown &lt;AddtlBalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00039.md) | 67–67 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.1 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00040.md) | 68–68 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.2 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00041.md) | 69–69 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.4 AggregateBalance &lt;AggtBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00042.md) | 70–70 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.6 NotAvailableBalance &lt;NotAvlblBal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00043.md) | 71–71 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.9 DaysAccrued &lt;DaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00044.md) | 72–72 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.12 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00045.md) | 73–73 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.15 AdditionalBalanceBreakdown &lt;AddtlBalBrkdwn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00046.md) | 74–74 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.9 SubAccountDetails &lt;SubAcctDtls&gt; / 2.4.9.5 BalanceForSubAccount &lt;BalForSubAcct&gt; / 2.4.9.5.18 BalanceAtSafekeepingPlace &lt;BalAtSfkpgPlc&gt; / 2.4.9.5.18.16 HoldingAdditionalDetails &lt;HldgAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00047.md) | 75–75 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.10 AccountBaseCurrencyTotalAmounts &lt;AcctBaseCcyTtlAmts&gt; / 2.4.10.1 TotalHoldingsValueOfPage &lt;TtlHldgsValOfPg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00048.md) | 76–76 |
| [2 semt.002.001.12 SecuritiesBalanceCustodyReportV12 / 2.4 Message Building Blocks / 2.4.10 AccountBaseCurrencyTotalAmounts &lt;AcctBaseCcyTtlAmts&gt; / 2.4.10.4 TotalEligibleCollateralValue &lt;TtlElgblCollVal&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00049.md) | 77–77 |

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
