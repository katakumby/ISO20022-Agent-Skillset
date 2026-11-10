---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.1 BillingReport <BllgRpt>", "15.4.2.1.7 PartyIdentification <PtyId>"]
file_pages: [271, 272, 273]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.1.7 PartyIdentification <PtyId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 271 to 273.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 271

```text
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
15.4.2.1.7  PartyIdentification <PtyId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the billed party.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification136" on page 3060
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
15.4.2.1.8  AccountInvoiceTotals <AcctInvcTtls>
Presence: [0..*]
Definition: Specifies totals related to the invoice per account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 271 August 2026
```

## File page 272

```text
AccountInvoiceTotals <AcctInvcTtls> contains the following InvoiceTotals8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1]  274
{Or     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 275
Or}     CashAccountIdentification <CshAcctId> [1..1] ± 275
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 272 August 2026
```

## File page 273

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or       Code <Cd> [1..1] CodeSet 290
Or}       Proprietary <Prtry> [1..1] Text 290
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 273 August 2026
```

