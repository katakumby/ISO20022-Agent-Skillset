---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.16 TransactionOverhead <TxOvrhd>"]
file_pages: [3950, 3951]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.16 TransactionOverhead <TxOvrhd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3950 to 3951.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3950

```text
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
55.4.5.20.16  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and taxes that are taken into consideration for the transaction,
so that the total difference between the net amount and gross amount is known, without taking into
account equalisation.
Impacted by: C23 "NonStandardSLAReferenceRule", C36 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3950 May 2026
```

## File page 3951

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C2, C8 3952
   TotalFees <TtlFees> [0..1] Amount C2, C8 3953
   TotalTaxes <TtlTaxs> [0..1] Amount C2, C8 3953
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3953
   IndividualFee <IndvFee> [0..*]  C5 3954
     Type <Tp> [1..1]  3954
{Or       Code <Cd> [1..1] CodeSet 3955
Or}       Proprietary <Prtry> [1..1] ± 3956
     Basis <Bsis> [0..1]  3956
{Or       Code <Cd> [1..1] CodeSet 3956
Or}       Proprietary <Prtry> [1..1] ± 3957
     StandardAmount <StdAmt> [0..1] Amount C2, C8 3957
     StandardRate <StdRate> [0..1] Rate 3957
     DiscountDetails <DscntDtls> [0..1]  C15 3958
       Amount <Amt> [0..1] Amount C2, C8 3958
       Rate <Rate> [0..1] Rate 3959
       Basis <Bsis> [0..1]  3959
{Or         Code <Cd> [1..1] CodeSet 3959
Or}         Proprietary <Prtry> [1..1] ± 3959
     AppliedAmount <ApldAmt> [0..1] Amount C2, C8 3960
     AppliedRate <ApldRate> [0..1] Rate 3960
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 3960
     RecipientIdentification <RcptId> [0..1] ± 3960
     InformativeIndicator <InftvInd> [1..1] Indicator 3961
   IndividualTax <IndvTax> [0..*] ± 3961
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  3961
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3962
       ISIN <ISIN> [0..1] IdentifierSet 3964
       OtherIdentification <OthrId> [0..*]  3964
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3951 May 2026
```

