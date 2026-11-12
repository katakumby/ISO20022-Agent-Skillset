---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.8 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.8 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 161 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
CodeName Name Definition
DBIT Debit Operation is a decrease.
4.4.2.2.2.2.3.8  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..*]
Definition: Specifies the interbank settlement amount(s) on which the query is performed.
InterbankSettlementAmount <IntrBkSttlmAmt> contains one of the following elements (see
"ActiveAmountRange3Choice" on page 791 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ImpliedCurrencyAndAmountRange
<ImpldCcyAndAmtRg>
[1..1] ± 791
Or}   CurrencyAndAmountRange <CcyAndAmtRg> [1..1] ± 791
4.4.2.2.2.2.3.9  InterbankSettlementAmountCurrency <IntrBkSttlmAmtCcy>
Presence: [0..*]
Definition: Currency in which the interbank settlement amount is expressed.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
4.4.2.2.2.2.3.10  PaymentMethod <PmtMtd>
Presence: [0..*]
Definition: Indicates the message or event from which an instruction has been initiated.
PaymentMethod <PmtMtd> contains one of the following PaymentOrigin1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FINMessageType <FINMT> [1..1] Text 161
Or   XMLMessageName <XMLMsgNm> [1..1] Text 162
Or   Proprietary <Prtry> [1..1] Text 162
Or}   Instrument <Instrm> [1..1] CodeSet 162
4.4.2.2.2.2.3.10.1  FINMessageType <FINMT>
Presence: [1..1]
Definition: Specifies that the payment was included in a SWIFT FIN format message, for example, MT
103.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 161 February 2025
```

