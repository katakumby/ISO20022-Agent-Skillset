---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.14 Charges <Chrgs>"]
file_pages: [334]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.14 Charges <Chrgs>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 334 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 334

```text
AmountDetails <AmtDtls> contains the following elements (see "AmountAndCurrencyExchange4" on
page 802 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructedAmount <InstdAmt> [0..1] ± 802
   TransactionAmount <TxAmt> [0..1] ± 803
   CounterValueAmount <CntrValAmt> [0..1] ± 803
   AnnouncedPostingAmount <AnncdPstngAmt> [0..1] ± 804
   ProprietaryAmount <PrtryAmt> [0..*] ± 804
3.4.2.15.14  Charges <Chrgs>
Presence: [0..1]
Definition: Provides information on the charges, pre-advised or included in the entry amount.
Usage: This component is used on entry level in case of batch or aggregate bookings.
Charges <Chrgs> contains the following Charges15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt> [0..1] Amount C2, C6 334
   Record <Rcrd> [0..*]  335
     Amount <Amt> [1..1] Amount C2, C6 335
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 336
     ChargeIncludedIndicator <ChrgInclInd> [0..1] Indicator 336
     Type <Tp> [0..1]  336
{Or       Code <Cd> [1..1] CodeSet 336
Or}       Proprietary <Prtry> [1..1] ± 337
     Rate <Rate> [0..1] Rate 337
     Bearer <Br> [0..1] CodeSet 337
     Agent <Agt> [0..1] ± 337
     Tax <Tax> [0..1]  338
       Identification <Id> [0..1] Text 338
       Rate <Rate> [0..1] Rate 338
       Amount <Amt> [0..1] Amount C2, C6 339
3.4.2.15.14.1  TotalChargesAndTaxAmount <TtlChrgsAndTaxAmt>
Presence: [0..1]
Definition: Total of all charges and taxes applied to the entry.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
334 March 2026
```

