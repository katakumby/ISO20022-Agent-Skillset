---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12"]
file_pages: [78, 79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3 semt.003.001.12 SecuritiesBalanceAccountingReportV12

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 78 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
3 semt.003.001.12
SecuritiesBalanceAccountingReportV12
3.1 MessageDefinition Functionality
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
```

## File page 79

```text
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
```

