---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.24 LetterIntentReference <LttrInttRef>"]
file_pages: [2834, 2835]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.24 LetterIntentReference <LttrInttRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2834 to 2835.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2834

```text
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
49.4.5.9.24  LetterIntentReference <LttrInttRef>
Presence: [0..1]
Definition: Reference of a letter of intent program, in which sales commissions are reduced based on
the aggregate of a customer's actual purchase and anticipated purchases, over a specific period of
time, and as agreed by the customer. A letter of intent program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
49.4.5.9.25  AccumulationRightReference <AcmltnRghtRef>
Presence: [0..1]
Definition: Reference of an accumulation right program, in which sales commissions are based on a
customer's present purchases of shares and the aggregate quantity previously purchased by the
customer. An accumulation rights program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
49.4.5.9.26  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and taxes that are taken into consideration for the transaction,
so that the total difference between the net amount and gross amount is known, without taking into
account equalisation.
Impacted by: C23 "NonStandardsSLAReferenceRule", C39 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2834 May 2026
```

## File page 2835

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes45 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C10 2836
   TotalFees <TtlFees> [0..1] Amount C3, C10 2837
   TotalTaxes <TtlTaxs> [0..1] Amount C3, C10 2837
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2837
   IndividualFee <IndvFee> [0..*]  C6 2838
     Type <Tp> [1..1]  2838
{Or       Code <Cd> [1..1] CodeSet 2839
Or}       Proprietary <Prtry> [1..1] ± 2840
     Basis <Bsis> [0..1]  2840
{Or       Code <Cd> [1..1] CodeSet 2840
Or}       Proprietary <Prtry> [1..1] ± 2841
     StandardAmount <StdAmt> [0..1] Amount C3, C10 2841
     StandardRate <StdRate> [0..1] Rate 2841
     DiscountDetails <DscntDtls> [0..1]  C17 2842
       Amount <Amt> [0..1] Amount C3, C10 2842
       Rate <Rate> [0..1] Rate 2843
       Basis <Bsis> [0..1]  2843
{Or         Code <Cd> [1..1] CodeSet 2843
Or}         Proprietary <Prtry> [1..1] ± 2843
     AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2844
     AppliedRate <ApldRate> [0..1] Rate 2844
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 2844
     RecipientIdentification <RcptId> [0..1] ± 2844
     InformativeIndicator <InftvInd> [1..1] Indicator 2845
   IndividualTax <IndvTax> [0..*] ± 2845
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  2845
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2846
       ISIN <ISIN> [0..1] IdentifierSet 2848
       OtherIdentification <OthrId> [0..*]  2848
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2835 May 2026
```

