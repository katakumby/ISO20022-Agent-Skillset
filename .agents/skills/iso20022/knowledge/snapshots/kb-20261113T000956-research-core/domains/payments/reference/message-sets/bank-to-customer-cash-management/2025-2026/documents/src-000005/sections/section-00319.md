---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.17 RelatedPrice <RltdPric>", "3.4.2.15.18.2.17.1 DealPrice <DealPric>"]
file_pages: [470]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.17.1 DealPrice <DealPric>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 470 to 470.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 470

```text
RelatedPrice <RltdPric> contains one of the following TransactionPrice4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DealPrice <DealPric> [1..1] ± 470
Or}   Proprietary <Prtry> [1..*]  470
     Type <Tp> [1..1] Text 470
     Price <Pric> [1..1] Amount C2, C6 470
3.4.2.15.18.2.17.1  DealPrice <DealPric>
Presence: [1..1]
Definition: Specifies the price of the traded financial instrument.
This is the deal price of the individual trade transaction.
If there is only one trade transaction for the execution of the trade, then the deal price could equal the
executed trade price (unless, for example, the price includes commissions or rounding, or some other
factor has been applied to the deal price or the executed trade price, or both).
DealPrice <DealPric> contains the following elements (see "Price7" on page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 879
   Value <Val> [1..1] ± 879
3.4.2.15.18.2.17.2  Proprietary <Prtry>
Presence: [1..*]
Definition: Proprietary price specification related to the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryPrice2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 470
   Price <Pric> [1..1] Amount C2, C6 470
3.4.2.15.18.2.17.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of price.
Datatype: "Max35Text" on page 916
3.4.2.15.18.2.17.2.2  Price <Pric>
Presence: [1..1]
Definition: Proprietary price specification related to the underlying transaction.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
470 March 2026
```

