---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.13 ForeignExchangeDetails <FXDtls>", "47.4.4.8.13.4 QuotationDate <QtnDt>"]
file_pages: [2589, 2590, 2591, 2592]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.13.4 QuotationDate <QtnDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2589 to 2592.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2589

```text
1 x CUR1 = nnn x CUR2,
where:
CUR1 is the unit currency
CUR2 is the quoted currency
nnn is the exchange rate.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Datatype: "BaseOneRate" on page 5401
47.4.4.8.13.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 5388
47.4.4.8.13.5  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes a foreign exchange rate.
QuotingInstitution <QtgInstn> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
47.4.4.8.14  LetterIntentReference <LttrInttRef>
Presence: [0..1]
Definition: Reference of a letter of intent program, in which sales commissions are reduced based on
the aggregate of a customer's actual purchase and anticipated purchases, over a specific period of
time, and as agreed by the customer. A letter of intent program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
47.4.4.8.15  AccumulationRightReference <AcmltnRghtRef>
Presence: [0..1]
Definition: Reference of an accumulation right program, in which sales commissions are based on a
customer's present purchases of shares and the aggregate quantity previously purchased by the
customer. An accumulation rights program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
47.4.4.8.16  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and tax to be applied to the net amount.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2589 May 2026
```

## File page 2590

```text
Impacted by: C19 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2590 May 2026
```

## File page 2591

```text
TransactionOverhead <TxOvrhd> contains the following FeeAndTax2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2593
   IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
2593
     Type <Tp> [1..1]  2594
{Or       Code <Cd> [1..1] CodeSet 2594
Or}       Proprietary <Prtry> [1..1] ± 2595
     Basis <Bsis> [0..1]  2595
{Or       Code <Cd> [1..1] CodeSet 2596
Or}       Proprietary <Prtry> [1..1] ± 2596
     StandardAmount <StdAmt> [0..1] Amount C3, C10 2596
     StandardRate <StdRate> [0..1] Rate 2597
     DiscountDetails <DscntDtls> [0..1]  C16 2597
       Amount <Amt> [0..1] Amount C3, C10 2597
       Rate <Rate> [0..1] Rate 2598
       Basis <Bsis> [0..1]  2598
{Or         Code <Cd> [1..1] CodeSet 2598
Or}         Proprietary <Prtry> [1..1] ± 2599
     RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 2599
     RequestedRate <ReqdRate> [0..1] Rate 2599
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 2600
     RecipientIdentification <RcptId> [0..1] ± 2600
   IndividualTax <IndvTax> [0..*]  2600
     Type <Tp> [1..1]  2601
{Or       Code <Cd> [1..1] CodeSet 2601
Or}       Proprietary <Prtry> [1..1] ± 2603
     Tax <Tax> [0..1]  2603
{Or       Amount <Amt> [1..1] Amount C3, C10 2603
Or}       Rate <Rate> [1..1] Rate 2604
     Country <Ctry> [0..1] CodeSet C8 2604
     ExemptionIndicator <XmptnInd> [1..1] Indicator 2604
     ExemptionReason <XmptnRsn> [0..1]  2604
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2591 May 2026
```

## File page 2592

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 2604
Or}       Proprietary <Prtry> [1..1] ± 2607
     RecipientIdentification <RcptId> [0..1] ± 2607
     TaxCalculationDetails <TaxClctnDtls> [0..1]  2608
       Basis <Bsis> [1..1]  2608
{Or         Code <Cd> [1..1] CodeSet 2608
Or}         Proprietary <Prtry> [1..1] ± 2608
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  2609
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2609
       ISIN <ISIN> [0..1] IdentifierSet 2611
       OtherIdentification <OthrId> [0..*]  2611
         Identification <Id> [1..1] Text 2611
         Suffix <Sfx> [0..1] Text 2611
         Type <Tp> [1..1]  2611
{Or           Code <Cd> [1..1] CodeSet 2612
Or}           Proprietary <Prtry> [1..1] Text 2613
       Description <Desc> [0..1] Text 2613
     Quantity <Qty> [1..1]  2614
{Or       Quantity <Qty> [1..1] ± C15 2614
Or}       ProprietaryQuantity <PrtryQty> [1..1]  2614
         Quantity <Qty> [1..1] Quantity 2615
         QuantityType <QtyTp> [1..1] Text 2615
         Issuer <Issr> [1..1] Text 2615
         SchemeName <SchmeNm> [0..1] Text 2615
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2615
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2592 May 2026
```

