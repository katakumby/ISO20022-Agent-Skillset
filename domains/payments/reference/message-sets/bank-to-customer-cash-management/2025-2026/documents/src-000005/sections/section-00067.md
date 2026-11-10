---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.9 RelatedParties <RltdPties>"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.9 RelatedParties <RltdPties>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
Usage: This component (on transaction level) can be used if the booking is for a single transaction, and
interest amount is included in the entry amount. It can also be used if individual interest amounts are
applied to individual transactions in the case of a batch or aggregate amount booking.
Interest <Intrst> contains the following elements (see "TransactionInterest4" on page 852 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalInterestAndTaxAmount <TtlIntrstAndTaxAmt> [0..1] Amount C1, C5 852
   Record <Rcrd> [0..*]  853
     Amount <Amt> [1..1] Amount C1, C5 853
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 854
     Type <Tp> [0..1]  854
{Or       Code <Cd> [1..1] CodeSet 854
Or}       Proprietary <Prtry> [1..1] Text 854
     Rate <Rate> [0..1]  854
       Type <Tp> [1..1] ± 855
       ValidityRange <VldtyRg> [0..1] ± 855
     FromToDate <FrToDt> [0..1] ± 855
     Reason <Rsn> [0..1] Text 855
     Tax <Tax> [0..1]  856
       Identification <Id> [0..1] Text 856
       Rate <Rate> [0..1] Rate 856
       Amount <Amt> [0..1] Amount C1, C5 856
2.4.2.15.18.2.9  RelatedParties <RltdPties>
Presence: [0..1]
Definition: Set of elements used to identify the parties related to the underlying transaction.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
132 March 2026
```

