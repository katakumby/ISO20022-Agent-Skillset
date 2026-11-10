---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.5 TotalTransactions6", "6.1.15.5.4 TotalEntriesPerBankTransactionCode <TtlNtriesPerBkTxCd>", "6.1.15.5.4.8 Availability <Avlbty>"]
file_pages: [850]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.5.4.8 Availability <Avlbty>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 850 to 850.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 850

```text
Following Must be True
    /Domain Must be present
 Or    /Proprietary Must be present
• FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily code
is not allowed.
6.1.15.5.4.8  Availability <Avlbty>
Presence: [0..*]
Definition: Set of elements used to indicate when the booked amount of money will become available,
that is can be accessed and starts generating interest.
Availability <Avlbty> contains the following elements (see "CashAvailability1" on page 824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [1..1]  824
{Or     NumberOfDays <NbOfDays> [1..1] Text 825
Or}     ActualDate <ActlDt> [1..1] Date 825
   Amount <Amt> [1..1] Amount C1, C5 825
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 825
6.1.15.5.4.9  Date <Dt>
Presence: [0..1]
Definition: Indicates the date (and time) of the transaction summary.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 826 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 826
Or}   DateTime <DtTm> [1..1] DateTime 826
6.1.15.6  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 851
   Envelope <Envlp> [1..1] (External Schema) 851
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
850 March 2026
```

