---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.4 Status <Sts>", "4.4.2.2.2.2.3.4.3 ProprietaryStatusReason <PrtryStsRsn>"]
file_pages: [160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.4.3 ProprietaryStatusReason <PrtryStsRsn>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 160 to 160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 160

```text
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 801 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 802
   ToDateTime <ToDtTm> [1..1] DateTime 802
4.4.2.2.2.2.3.4.3  ProprietaryStatusReason <PrtryStsRsn>
Presence: [0..1]
Definition: Defines the reason that has been used by the system to reject the transaction.
Datatype: "Max4AlphaNumericText" on page 890
4.4.2.2.2.2.3.5  InstructedAmount <InstdAmt>
Presence: [0..*]
Definition: Specifies the instructed amount(s) on which the query is performed.
InstructedAmount <InstdAmt> contains one of the following elements (see
"ActiveOrHistoricAmountRange2Choice" on page 792 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ImpliedCurrencyAndAmountRange
<ImpldCcyAndAmtRg>
[1..1] ± 792
Or}   CurrencyAndAmountRange <CcyAndAmtRg> [1..1] ± 792
4.4.2.2.2.2.3.6  InstructedAmountCurrency <InstdAmtCcy>
Presence: [0..*]
Definition: Currency in which the instructed amount is expressed.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
4.4.2.2.2.2.3.7  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the payment instruction is a debit or a credit.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 160 February 2025
```

