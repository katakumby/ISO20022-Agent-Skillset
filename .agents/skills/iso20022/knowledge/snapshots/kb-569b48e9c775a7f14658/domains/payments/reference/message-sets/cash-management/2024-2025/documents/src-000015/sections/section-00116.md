---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.4 AccountEntrySearch <AcctNtrySch>", "4.4.2.2.2.2.4.1 AccountIdentification <AcctId>", "4.4.2.2.2.2.4.1.3 NotContainText <NCTTxt>"]
file_pages: [187]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.4.1.3 NotContainText <NCTTxt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 187 to 187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 187

```text
4.4.2.2.2.2.4.1.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.4.2  EntryAmount <NtryAmt>
Presence: [0..*]
Definition: Specifies the entry amount(s) on which the query is performed.
EntryAmount <NtryAmt> contains one of the following elements (see
"ActiveOrHistoricAmountRange2Choice" on page 792 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ImpliedCurrencyAndAmountRange
<ImpldCcyAndAmtRg>
[1..1] ± 792
Or}   CurrencyAndAmountRange <CcyAndAmtRg> [1..1] ± 792
4.4.2.2.2.2.4.3  EntryAmountCurrency <NtryAmtCcy>
Presence: [0..*]
Definition: Currency of the entry amount.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
4.4.2.2.2.2.4.4  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
4.4.2.2.2.2.4.5  EntryStatus <NtrySts>
Presence: [0..*]
Definition: Status of an entry on the books of the account servicer.
Datatype: "EntryStatus1Code" on page 851
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 187 February 2025
```

