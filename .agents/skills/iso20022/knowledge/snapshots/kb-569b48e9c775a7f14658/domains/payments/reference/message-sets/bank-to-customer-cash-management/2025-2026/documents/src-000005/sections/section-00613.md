---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.5 TotalTransactions6", "6.1.15.5.1 TotalEntries <TtlNtries>"]
file_pages: [846]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.5.1 TotalEntries <TtlNtries>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 846 to 846.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 846

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalEntries <TtlNtries> [0..1]  846
     NumberOfEntries <NbOfNtries> [0..1] Text 846
     Sum <Sum> [0..1] Quantity 846
     TotalNetEntry <TtlNetNtry> [0..1] ± 847
   TotalCreditEntries <TtlCdtNtries> [0..1] ± 847
   TotalDebitEntries <TtlDbtNtries> [0..1] ± 847
   TotalEntriesPerBankTransactionCode
<TtlNtriesPerBkTxCd>
[0..*]  847
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
6.1.15.5.1  TotalEntries <TtlNtries>
Presence: [0..1]
Definition: Specifies the total number and sum of debit and credit entries.
TotalEntries <TtlNtries> contains the following NumberAndSumOfTransactions4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 846
   Sum <Sum> [0..1] Quantity 846
   TotalNetEntry <TtlNetNtry> [0..1] ± 847
6.1.15.5.1.1  NumberOfEntries <NbOfNtries>
Presence: [0..1]
Definition: Number of individual entries included in the report.
Datatype: "Max15NumericText" on page 915
6.1.15.5.1.2  Sum <Sum>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
846 March 2026
```

