---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.5 TotalTransactions6", "6.1.15.5.4 TotalEntriesPerBankTransactionCode <TtlNtriesPerBkTxCd>", "6.1.15.5.4.5 DebitEntries <DbtNtries>"]
file_pages: [849]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.5.4.5 DebitEntries <DbtNtries>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 849 to 849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 849

```text
CreditEntries <CdtNtries> contains the following elements (see "NumberAndSumOfTransactions1" on
page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 857
   Sum <Sum> [0..1] Quantity 857
6.1.15.5.4.5  DebitEntries <DbtNtries>
Presence: [0..1]
Definition: Number of individual debit entries for the bank transaction code.
DebitEntries <DbtNtries> contains the following elements (see "NumberAndSumOfTransactions1" on
page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfEntries <NbOfNtries> [0..1] Text 857
   Sum <Sum> [0..1] Quantity 857
6.1.15.5.4.6  ForecastIndicator <FcstInd>
Presence: [0..1]
Definition: Indicates whether the bank transaction code is related to booked or forecast items.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
6.1.15.5.4.7  BankTransactionCode <BkTxCd>
Presence: [1..1]
Definition: Set of elements used to fully identify the type of underlying transaction resulting in an entry.
Impacted by: C11 "DomainOrProprietaryRule", C14 "FamilyAndSubFamilyRule"
BankTransactionCode <BkTxCd> contains the following elements (see
"BankTransactionCodeStructure4" on page 821 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Domain <Domn> [0..1] ± 821
   Proprietary <Prtry> [0..1]  821
     Code <Cd> [1..1] Text 822
     Issuer <Issr> [0..1] Text 822
Constraints
• DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
849 March 2026
```

