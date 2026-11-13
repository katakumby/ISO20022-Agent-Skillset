---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "7.4.2.41.39 UnderlyingAllocation <UndrlygAllcn>", "7.4.2.41.39.1 Amount <Amt>"]
file_pages: [1012]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.41.39.1 Amount <Amt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1012 to 1012.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1012

```text
UnderlyingAllocation <UndrlygAllcn> contains the following TransactionAllocation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C9 1012
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1012
   Account <Acct> [1..1] ± C16,
C15
1013
   Purpose <Purp> [1..1] ± 1013
   Reference <Ref> [1..1] Text 1013
   RelatedReferences <RltdRefs> [0..*] ± 1014
Constraints
• UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
7.4.2.41.39.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the allocation.
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.2.41.39.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the allocation is a debit or credit.
Datatype: "CreditDebitCode" on page 1227
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
1012 March 2026
```

