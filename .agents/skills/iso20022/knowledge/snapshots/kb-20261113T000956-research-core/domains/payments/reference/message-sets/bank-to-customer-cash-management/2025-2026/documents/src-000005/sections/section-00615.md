---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.5 TotalTransactions6", "6.1.15.5.4 TotalEntriesPerBankTransactionCode <TtlNtriesPerBkTxCd>", "6.1.15.5.4.1 NumberOfEntries <NbOfNtries>"]
file_pages: [848]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.5.4.1 NumberOfEntries <NbOfNtries>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 848 to 848.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 848

```text
TotalEntriesPerBankTransactionCode <TtlNtriesPerBkTxCd> contains the following
TotalsPerBankTransactionCode5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 848
   Sum <Sum> [0..1] Quantity 848
   TotalNetEntry <TtlNetNtry> [0..1] ± 848
   CreditEntries <CdtNtries> [0..1] ± 848
   DebitEntries <DbtNtries> [0..1] ± 849
   ForecastIndicator <FcstInd> [0..1] Indicator 849
   BankTransactionCode <BkTxCd> [1..1] ± C11,
C14
849
   Availability <Avlbty> [0..*] ± 850
   Date <Dt> [0..1] ± 850
6.1.15.5.4.1  NumberOfEntries <NbOfNtries>
Presence: [0..1]
Definition: Number of individual entries for the bank transaction code.
Datatype: "Max15NumericText" on page 915
6.1.15.5.4.2  Sum <Sum>
Presence: [0..1]
Definition: Total of all individual entries included in the report.
Datatype: "DecimalNumber" on page 912
6.1.15.5.4.3  TotalNetEntry <TtlNetNtry>
Presence: [0..1]
Definition: Total debit or credit amount that is the result of the netted amounts for all debit and credit
entries per bank transaction code.
TotalNetEntry <TtlNetNtry> contains the following elements (see "AmountAndDirection35" on
page 805 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Quantity 805
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 805
6.1.15.5.4.4  CreditEntries <CdtNtries>
Presence: [0..1]
Definition: Number of individual credit entries for the bank transaction code.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
848 March 2026
```

