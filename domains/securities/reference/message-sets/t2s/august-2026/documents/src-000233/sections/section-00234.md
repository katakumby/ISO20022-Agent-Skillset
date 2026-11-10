---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.9 InvoiceTotals <InvcTtls>", "15.4.2.1.9.4 PaymentDueDate <PmtDueDt>"]
file_pages: [311, 312, 313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.9.4 PaymentDueDate <PmtDueDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 311 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 311

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
15.4.2.1.9.4  PaymentDueDate <PmtDueDt>
Presence: [1..1]
Definition: Due date for the payment of the invoice.
Datatype: "ISODate" on page 3319
15.4.2.1.9.5  CashAccount <CshAcct>
Presence: [0..1]
Definition: Cash account from which the fees are paid.
CashAccount <CshAcct> contains one of the following elements (see "AccountIdentification4Choice"
on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
15.4.2.1.10  ServiceCategoryTotals <SvcCtgyTtls>
Presence: [0..*]
Definition: Specifies totals related to the service category.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 311 August 2026
```

## File page 312

```text
ServiceCategoryTotals <SvcCtgyTtls> contains the following ServiceCategoryTotals8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..1]  314
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 314
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 314
   ParentAccountIdentification <PrntAcctId> [0..1]  315
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 315
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 315
   BilledCustomerIdentification <BlldCstmrId> [0..1] ± 315
   Tax <Tax> [0..*]  316
     Rate <Rate> [1..1] Rate 316
     Description <Desc> [0..1] Text 316
     TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 316
     TaxExemption <TaxXmptn> [0..*]  317
       ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 317
       Reason <Rsn> [0..1] Text 317
     Amount <Amt> [1..1] Amount C1, C4 318
     ChargesAndFees <ChrgsAndFees> [0..*]  318
       Type <Tp> [0..1] Text 318
       Description <Desc> [0..1] Text 318
       Rate <Rate> [0..1] Rate 319
       Amount <Amt> [0..1] Amount C1, C4 319
   TotalInvoiceAmount <TtlInvcAmt> [1..1]  319
     Amount <Amt> [1..1] Amount C1, C4 319
     ForeignExchange <FX> [0..1] ± 320
   ServiceCategory <SvcCtgy> [1..1]  320
{Or     Code <Cd> [1..1] CodeSet 320
Or}     Proprietary <Prtry> [1..1] Text 320
   ServiceItemTotals <SvcItmTtls> [0..*]  320
     ItemType <ItmTp> [1..1] Text 321
     Description <Desc> [0..1] Text 321
     Quantity <Qty> [1..1] Quantity 321
     UnitPrice <UnitPric> [0..1] Amount C1, C4 322
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 312 August 2026
```

## File page 313

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Tax <Tax> [0..*]  322
       Rate <Rate> [1..1] Rate 323
       Description <Desc> [0..1] Text 323
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 323
       TaxExemption <TaxXmptn> [0..*]  323
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 323
         Reason <Rsn> [0..1] Text 324
       Amount <Amt> [1..1] Amount C1, C4 324
       ChargesAndFees <ChrgsAndFees> [0..*]  324
         Type <Tp> [0..1] Text 325
         Description <Desc> [0..1] Text 325
         Rate <Rate> [0..1] Rate 325
         Amount <Amt> [0..1] Amount C1, C4 325
     TotalInvoiceAmount <TtlInvcAmt> [1..1]  325
       Amount <Amt> [1..1] Amount C1, C4 326
       ForeignExchange <FX> [0..1] ± 326
   ServiceItemCorrection <SvcItmCrrctn> [0..*]  326
     ItemType <ItmTp> [1..1] Text 327
     Description <Desc> [0..1] Text 327
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 328
     Quantity <Qty> [1..1] Quantity 328
     UnitPrice <UnitPric> [0..1] Amount C1, C4 328
     Tax <Tax> [0..*]  328
       Rate <Rate> [1..1] Rate 329
       Description <Desc> [0..1] Text 329
       TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 329
       TaxExemption <TaxXmptn> [0..*]  330
         ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 330
         Reason <Rsn> [0..1] Text 330
       Amount <Amt> [1..1] Amount C1, C4 330
       ChargesAndFees <ChrgsAndFees> [0..*]  331
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 313 August 2026
```

