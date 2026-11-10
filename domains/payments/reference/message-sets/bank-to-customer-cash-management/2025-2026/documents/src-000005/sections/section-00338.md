---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.24 UnderlyingAllocation <UndrlygAllcn>"]
file_pages: [490]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.24 UnderlyingAllocation <UndrlygAllcn>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 490 to 490.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 490

```text
3.4.2.15.18.2.24  UnderlyingAllocation <UndrlygAllcn>
Presence: [0..*]
Definition: Provides information on the underlying allocations that make up the payment.
Usage: Only used by the Securities industry.
Impacted by: C31 "UnderlyingAllocationGuideline"
UnderlyingAllocation <UndrlygAllcn> contains the following TransactionAllocation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C6 490
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 490
   Account <Acct> [1..1] ± C20,
C18
491
   Purpose <Purp> [1..1] ± 491
   Reference <Ref> [1..1] Text 492
   RelatedReferences <RltdRefs> [0..*] ± 492
Constraints
• UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
3.4.2.15.18.2.24.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the allocation.
Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.15.18.2.24.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the allocation is a debit or credit.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
490 March 2026
```

