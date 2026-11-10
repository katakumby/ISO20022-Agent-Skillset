---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.2 Structure"]
file_pages: [241, 242, 243, 244, 245, 246, 247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 241 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 241

```text
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BllgRpt> [1..1]  
   MessageHeader <MsgHdr> [1..1]  249
     MessageIdentification <MsgId> [1..1] Text 249
     CreationDateTime <CreDtTm> [0..1] DateTime 249
     RequestType <ReqTp> [0..1]  249
{Or       PaymentControl <PmtCtrl> [1..1] CodeSet 250
Or       Enquiry <Enqry> [1..1] CodeSet 250
Or}       Proprietary <Prtry> [1..1] ± 250
     OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 250
   BillingReportOrError <BllgRptOrErr> [1..1]  251
{Or     BillingReport <BllgRpt> [1..1]  259
       RegulatoryData <RgltryData> [1..1]  266
         Invoicer <Invcr> [1..1] ± 266
         Invoicee <Invcee> [1..1] ± 267
         InvoiceLegalStatement <InvcLglStmt> [0..1] Text 268
         PaymentMethod <PmtMtd> [0..1]  269
{Or           Code <Cd> [1..1] CodeSet 269
Or}           Proprietary <Prtry> [1..1] Text 269
       Service <Svc> [0..1]  269
         SystemIdentification <SysId> [1..1] ± 269
         SystemCurrency <SysCcy> [0..1] CodeSet C1 270
       InvoiceDate <InvcDt> [1..1] Date 270
       BillingIdentification <BllgId> [1..1] Text 270
       BillingPeriod <BllgPrd> [1..1] ± 270
       ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 270
       PartyIdentification <PtyId> [0..1] ± 271
       AccountInvoiceTotals <AcctInvcTtls> [0..*]  271
         AccountIdentification <AcctId> [1..1]  274
{Or           SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 275
Or}           CashAccountIdentification <CshAcctId> [1..1] ± 275
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 241 August 2026
```

## File page 242

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         InvoiceTotals <InvcTtls> [1..1]  275
           Tax <Tax> [0..*]  276
             Rate <Rate> [1..1] Rate 277
             Description <Desc> [0..1] Text 277
             TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 277
             TaxExemption <TaxXmptn> [0..*]  278
               ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 278
               Reason <Rsn> [0..1] Text 278
             Amount <Amt> [1..1] Amount C1, C4 278
             ChargesAndFees <ChrgsAndFees> [0..*]  279
               Type <Tp> [0..1] Text 279
               Description <Desc> [0..1] Text 279
               Rate <Rate> [0..1] Rate 279
               Amount <Amt> [0..1] Amount C1, C4 279
           Adjustment <Adjstmnt> [0..1]  280
             Direction <Drctn> [1..1] CodeSet 280
             Amount <Amt> [1..1] Amount C1, C4 280
           TotalInvoiceAmount <TtlInvcAmt> [1..1]  281
             Amount <Amt> [1..1] Amount C1, C4 281
             ForeignExchange <FX> [0..1] ± 281
           PaymentDueDate <PmtDueDt> [1..1] Date 282
           CashAccount <CshAcct> [0..1] ± 282
         ServiceCategoryTotals <SvcCtgyTtls> [1..*]  282
           BilledCustomerIdentification <BlldCstmrId> [0..1] ± 285
           Tax <Tax> [0..*]  285
             Rate <Rate> [1..1] Rate 285
             Description <Desc> [0..1] Text 286
             TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 286
             TaxExemption <TaxXmptn> [0..*]  286
               ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 286
               Reason <Rsn> [0..1] Text 287
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 242 August 2026
```

## File page 243

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or             Code <Cd> [1..1] CodeSet 290
Or}             Proprietary <Prtry> [1..1] Text 290
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
                 ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 294
                 Reason <Rsn> [0..1] Text 294
               Amount <Amt> [1..1] Amount C1, C4 294
               ChargesAndFees <ChrgsAndFees> [0..*]  295
                 Type <Tp> [0..1] Text 295
                 Description <Desc> [0..1] Text 295
                 Rate <Rate> [0..1] Rate 295
                 Amount <Amt> [0..1] Amount C1, C4 295
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 243 August 2026
```

## File page 244

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
             TotalInvoiceAmount <TtlInvcAmt> [1..1]  303
               Amount <Amt> [1..1] Amount C1, C4 303
               ForeignExchange <FX> [0..1] ± 303
       InvoiceTotals <InvcTtls> [0..1]  304
         Tax <Tax> [0..*]  305
           Rate <Rate> [1..1] Rate 306
           Description <Desc> [0..1] Text 306
           TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 306
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 244 August 2026
```

## File page 245

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           TaxExemption <TaxXmptn> [0..*]  307
             ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 307
             Reason <Rsn> [0..1] Text 307
           Amount <Amt> [1..1] Amount C1, C4 307
           ChargesAndFees <ChrgsAndFees> [0..*]  308
             Type <Tp> [0..1] Text 308
             Description <Desc> [0..1] Text 308
             Rate <Rate> [0..1] Rate 308
             Amount <Amt> [0..1] Amount C1, C4 308
         Adjustment <Adjstmnt> [0..1]  309
           Direction <Drctn> [1..1] CodeSet 309
           Amount <Amt> [1..1] Amount C1, C4 309
         TotalInvoiceAmount <TtlInvcAmt> [1..1]  310
           Amount <Amt> [1..1] Amount C1, C4 310
           ForeignExchange <FX> [0..1] ± 310
         PaymentDueDate <PmtDueDt> [1..1] Date 311
         CashAccount <CshAcct> [0..1] ± 311
       ServiceCategoryTotals <SvcCtgyTtls> [0..*]  311
         AccountIdentification <AcctId> [0..1]  314
{Or           SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 314
Or}           CashAccountIdentification <CshAcctId> [1..1] ± 314
         ParentAccountIdentification <PrntAcctId> [0..1]  315
{Or           SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 315
Or}           CashAccountIdentification <CshAcctId> [1..1] ± 315
         BilledCustomerIdentification <BlldCstmrId> [0..1] ± 315
         Tax <Tax> [0..*]  316
           Rate <Rate> [1..1] Rate 316
           Description <Desc> [0..1] Text 316
           TaxableAmount <TaxblAmt> [1..1] Amount C1, C4 316
           TaxExemption <TaxXmptn> [0..*]  317
             ExemptedAmount <XmptdAmt> [1..1] Amount C1, C4 317
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 245 August 2026
```

## File page 246

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           Code <Cd> [1..1] CodeSet 320
Or}           Proprietary <Prtry> [1..1] Text 320
         ServiceItemTotals <SvcItmTtls> [0..*]  320
           ItemType <ItmTp> [1..1] Text 321
           Description <Desc> [0..1] Text 321
           Quantity <Qty> [1..1] Quantity 321
           UnitPrice <UnitPric> [0..1] Amount C1, C4 322
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 246 August 2026
```

## File page 247

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
               Type <Tp> [0..1] Text 331
               Description <Desc> [0..1] Text 331
               Rate <Rate> [0..1] Rate 331
               Amount <Amt> [0..1] Amount C1, C4 331
           TotalInvoiceAmount <TtlInvcAmt> [1..1]  332
             Amount <Amt> [1..1] Amount C1, C4 332
             ForeignExchange <FX> [0..1] ± 332
Or     CancellationReport <CxlRpt> [1..1]  333
       RegulatoryData <RgltryData> [0..1]  333
         Invoicer <Invcr> [1..1] ± 334
         Invoicee <Invcee> [1..1] ± 335
         InvoiceLegalStatement <InvcLglStmt> [0..1] Text 336
         PaymentMethod <PmtMtd> [0..1]  337
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 247 August 2026
```

