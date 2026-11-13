---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.7 Charges <Chrgs>"]
file_pages: [386]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.7 Charges <Chrgs>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 386 to 386.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 386

```text
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
Following Must be True
    /Domain Must be present
 Or    /Proprietary Must be present
• FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily code
is not allowed.
3.4.2.15.18.2.7  Charges <Chrgs>
Presence: [0..1]
Definition: Provides information on the charges, pre-advised or included in the entry amount.
Usage: This component (on transaction level) can be used in case the booking is for a single
transaction, and charges are included in the entry amount. It can also be used in case individual charge
amounts are applied to individual transactions in case of a batch or aggregate amount booking.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
386 March 2026
```

