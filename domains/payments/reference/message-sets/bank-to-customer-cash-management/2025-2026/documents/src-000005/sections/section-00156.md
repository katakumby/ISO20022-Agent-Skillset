---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.24 UnderlyingAllocation <UndrlygAllcn>"]
file_pages: [230]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.24 UnderlyingAllocation <UndrlygAllcn>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 230 to 230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 230

```text
2.4.2.15.18.2.24  UnderlyingAllocation <UndrlygAllcn>
Presence: [0..*]
Definition: Provides information on the underlying allocations that make up the payment.
Usage: Only used by the Securities industry.
Impacted by: C31 "UnderlyingAllocationGuideline"
UnderlyingAllocation <UndrlygAllcn> contains the following TransactionAllocation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C6 230
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 230
   Account <Acct> [1..1] ± C20,
C18
231
   Purpose <Purp> [1..1] ± 231
   Reference <Ref> [1..1] Text 232
   RelatedReferences <RltdRefs> [0..*] ± 232
Constraints
• UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
2.4.2.15.18.2.24.1  Amount <Amt>
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
2.4.2.15.18.2.24.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the allocation is a debit or credit.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
230 March 2026
```

