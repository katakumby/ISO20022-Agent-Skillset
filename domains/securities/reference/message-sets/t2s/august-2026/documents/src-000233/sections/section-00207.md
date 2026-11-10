---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.8 AccountInvoiceTotals <AcctInvcTtls>", "15.4.2.1.8.2 InvoiceTotals <InvcTtls>", "15.4.2.1.8.2.4 PaymentDueDate <PmtDueDt>"]
file_pages: [282, 283, 284]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.8.2.4 PaymentDueDate <PmtDueDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 282 to 284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 282

```text
ForeignExchange <FX> contains the following elements (see "ForeignExchangeTerms24" on
page 2955 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 2955
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 2955
   ExchangeRate <XchgRate> [1..1] Rate 2956
   ResultingAmount <RsltgAmt> [0..1] Amount C1, C4 2956
15.4.2.1.8.2.4  PaymentDueDate <PmtDueDt>
Presence: [1..1]
Definition: Due date for the payment of the invoice.
Datatype: "ISODate" on page 3319
15.4.2.1.8.2.5  CashAccount <CshAcct>
Presence: [0..1]
Definition: Cash account from which the fees are paid.
CashAccount <CshAcct> contains one of the following elements (see "AccountIdentification4Choice"
on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
15.4.2.1.8.3  ServiceCategoryTotals <SvcCtgyTtls>
Presence: [1..*]
Definition: Specifies totals related to the service category.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 282 August 2026
```

## File page 283

```text
ServiceCategoryTotals <SvcCtgyTtls> contains the following ServiceCategoryTotals7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BilledCustomerIdentification <BlldCstmrId> [0..1] ± 285
   Tax <Tax> [0..*]  285
     Rate <Rate> [1..1] Rate 285
     Description <Desc> [0..1] Text 286
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 286
     TaxExemption <TaxXmptn> [0..*]  286
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 286
       Reason <Rsn> [0..1] Text 287
     Amount <Amt> [1..1] Amount C1, C4 287
     ChargesAndFees <ChrgsAndFees> [0..*]  287
       Type <Tp> [0..1] Text 288
       Description <Desc> [0..1] Text 288
       Rate <Rate> [0..1] Rate 288
       Amount <Amt> [0..1] Amount C1, C4 288
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  288
     Amount <Amt> [1..1] Amount C1, C4 289
     ForeignExchange <FX> [0..1] ± 289
   ServiceCategory <SvcCtgy> [1..1]  289
{Or     Code <Cd> [1..1] CodeSet 290
Or}     Proprietary <Prtry> [1..1] Text 290
   ServiceItemTotals <SvcItmTtls> [0..*]  290
     ItemType <ItmTp> [1..1] Text 291
     Description <Desc> [0..1] Text 291
     Quantity <Qty> [1..1] Quantity 292
     BalanceCurrency <BalCcy> [0..1] CodeSet C1 292
     UnitPrice <UnitPric> [0..1] Amount C1, C4 292
     Tax <Tax> [0..*]  292
       Rate <Rate> [1..1] Rate 293
       Description <Desc> [0..1] Text 293
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 293
       TaxExemption <TaxXmptn> [0..*]  294
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 283 August 2026
```

## File page 284

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 294
         Reason <Rsn> [0..1] Text 294
       Amount <Amt> [1..1] Amount C1, C4 294
       ChargesAndFees <ChrgsAndFees> [0..*]  295
         Type <Tp> [0..1] Text 295
         Description <Desc> [0..1] Text 295
         Rate <Rate> [0..1] Rate 295
         Amount <Amt> [0..1] Amount C1, C4 295
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  296
       Amount <Amt> [1..1] Amount C1, C4 296
       ForeignExchange <FX> [0..1] ± 296
   ServiceItemCorrection <SvcItmCrrctn> [0..*]  297
     ItemType <ItmTp> [1..1] Text 298
     Description <Desc> [0..1] Text 298
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 299
     Quantity <Qty> [1..1] Quantity 299
     BalanceCurrency <BalCcy> [0..1] CodeSet C1 299
     UnitPrice <UnitPric> [0..1] Amount C1, C4 299
     Tax <Tax> [0..*]  300
       Rate <Rate> [1..1] Rate 300
       Description <Desc> [0..1] Text 300
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 300
       TaxExemption <TaxXmptn> [0..*]  301
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 301
         Reason <Rsn> [0..1] Text 301
       Amount <Amt> [1..1] Amount C1, C4 301
       ChargesAndFees <ChrgsAndFees> [0..*]  302
         Type <Tp> [0..1] Text 302
         Description <Desc> [0..1] Text 302
         Rate <Rate> [0..1] Rate 302
         Amount <Amt> [0..1] Amount C1, C4 302
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 284 August 2026
```

