---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.5 TotalTransactions6", "6.1.15.5.1 TotalEntries <TtlNtries>", "6.1.15.5.1.3 TotalNetEntry <TtlNetNtry>"]
file_pages: [847]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.5.1.3 TotalNetEntry <TtlNetNtry>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 847 to 847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 847

```text
Definition: Total of all individual entries included in the report.
Datatype: "DecimalNumber" on page 912
6.1.15.5.1.3  TotalNetEntry <TtlNetNtry>
Presence: [0..1]
Definition: Resulting debit or credit amount of the netted amounts for all debit and credit entries.
TotalNetEntry <TtlNetNtry> contains the following elements (see "AmountAndDirection35" on
page 805 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Quantity 805
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 805
6.1.15.5.2  TotalCreditEntries <TtlCdtNtries>
Presence: [0..1]
Definition: Specifies the total number and sum of credit entries.
TotalCreditEntries <TtlCdtNtries> contains the following elements (see
"NumberAndSumOfTransactions1" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 857
   Sum <Sum> [0..1] Quantity 857
6.1.15.5.3  TotalDebitEntries <TtlDbtNtries>
Presence: [0..1]
Definition: Specifies the total number and sum of debit entries.
TotalDebitEntries <TtlDbtNtries> contains the following elements (see
"NumberAndSumOfTransactions1" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 857
   Sum <Sum> [0..1] Quantity 857
6.1.15.5.4  TotalEntriesPerBankTransactionCode <TtlNtriesPerBkTxCd>
Presence: [0..*]
Definition: Specifies the total number and sum of entries per bank transaction code.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
847 March 2026
```

