---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.4 AccountEntrySearch <AcctNtrySch>", "4.4.2.2.2.2.4.1 AccountIdentification <AcctId>"]
file_pages: [186]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.4.1 AccountIdentification <AcctId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 186 to 186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 186

```text
all occurrences of EntryAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator must be
absent.
On Condition
    /EntryAmount[*]/CurrencyAndAmountRange/CreditDebitIndicator is present
Following Must be True
    /CreditDebitIndicator Must be absent
• EntryAmountCreditDebitIndicator2Rule
If at least one occurrence of EntryAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is
present, then CreditDebitIndicator is not allowed.
If EntryAmount/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is not present, then
CreditDebitIndicator is optional.
On Condition
    /EntryAmount[*]/ImpliedCurrencyAndAmountRange/CreditDebitIndicator is present
Following Must be True
    /CreditDebitIndicator Must be absent
4.4.2.2.2.2.4.1  AccountIdentification <AcctId>
Presence: [0..*]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 186
Or   ContainText <CTTxt> [1..1] Text 186
Or}   NotContainText <NCTTxt> [1..1] Text 187
4.4.2.2.2.2.4.1.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 787
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
4.4.2.2.2.2.4.1.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 186 February 2025
```

