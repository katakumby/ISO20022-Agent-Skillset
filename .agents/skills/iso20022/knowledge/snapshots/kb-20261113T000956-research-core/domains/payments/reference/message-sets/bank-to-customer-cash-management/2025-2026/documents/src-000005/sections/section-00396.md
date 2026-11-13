---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.14 Charges <Chrgs>", "4.4.2.14.14.2 Record <Rcrd>", "4.4.2.14.14.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [594]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.14.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 594 to 594.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 594

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.2.14.14.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the charges amount is a credit or a debit amount.
Usage: A zero amount is considered to be a credit.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
4.4.2.14.14.2.3  ChargeIncludedIndicator <ChrgInclInd>
Presence: [0..1]
Definition: Indicates whether the charge should be included in the amount or is added as pre-advice.
Datatype: One of the following values must be used (see "ChargeIncludedIndicator" on page 911):
• Meaning When True: Included
• Meaning When False: Pre-advised
4.4.2.14.14.2.4  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of charge.
Type <Tp> contains one of the following ChargeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 595
4.4.2.14.14.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Charge type, in a coded form.
Datatype: "ExternalChargeType1Code" on page 895
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
594 March 2026
```

