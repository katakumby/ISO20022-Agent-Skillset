---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.9 Availability <Avlbty>"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.9 Availability <Avlbty>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
2.4.2.15.9  Availability <Avlbty>
Presence: [0..*]
Definition: Indicates when the booked amount of money will become available, that is can be accessed
and starts generating interest.
Usage: This type of information is used in the US and is linked to particular instruments such as
cheques.
Example: When a cheque is deposited, it will be booked on the deposit day, but the amount of money
will only be accessible as of the indicated availability day (according to national banking regulations).
Availability <Avlbty> contains the following elements (see "CashAvailability1" on page 824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1]  824
{Or     NumberOfDays <NbOfDays> [1..1] Text 825
Or}     ActualDate <ActlDt> [1..1] Date 825
   Amount <Amt> [1..1] Amount C1, C5 825
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 825
2.4.2.15.10  BankTransactionCode <BkTxCd>
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
Following Must be True
    /Domain Must be present
 Or    /Proprietary Must be present
• FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily code
is not allowed.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
72 March 2026
```

