---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.17 RequestedNAVCurrency <ReqdNAVCcy>"]
file_pages: [3878, 3879]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.17 RequestedNAVCurrency <ReqdNAVCcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3878 to 3879.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3878

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
55.4.5.19.17  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
55.4.5.19.18  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and taxes that are taken into consideration for the transaction,
so that the total difference between the net amount and gross amount is known, without taking into
account equalisation.
Impacted by: C23 "NonStandardSLAReferenceRule", C36 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3878 May 2026
```

## File page 3879

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C2, C8 3880
   TotalFees <TtlFees> [0..1] Amount C2, C8 3881
   TotalTaxes <TtlTaxs> [0..1] Amount C2, C8 3881
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3881
   IndividualFee <IndvFee> [0..*]  C5 3882
     Type <Tp> [1..1]  3882
{Or       Code <Cd> [1..1] CodeSet 3883
Or}       Proprietary <Prtry> [1..1] ± 3884
     Basis <Bsis> [0..1]  3884
{Or       Code <Cd> [1..1] CodeSet 3884
Or}       Proprietary <Prtry> [1..1] ± 3885
     StandardAmount <StdAmt> [0..1] Amount C2, C8 3885
     StandardRate <StdRate> [0..1] Rate 3885
     DiscountDetails <DscntDtls> [0..1]  C15 3886
       Amount <Amt> [0..1] Amount C2, C8 3886
       Rate <Rate> [0..1] Rate 3887
       Basis <Bsis> [0..1]  3887
{Or         Code <Cd> [1..1] CodeSet 3887
Or}         Proprietary <Prtry> [1..1] ± 3887
     AppliedAmount <ApldAmt> [0..1] Amount C2, C8 3888
     AppliedRate <ApldRate> [0..1] Rate 3888
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 3888
     RecipientIdentification <RcptId> [0..1] ± 3888
     InformativeIndicator <InftvInd> [1..1] Indicator 3889
   IndividualTax <IndvTax> [0..*] ± 3889
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  3889
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3890
       ISIN <ISIN> [0..1] IdentifierSet 3892
       OtherIdentification <OthrId> [0..*]  3892
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3879 May 2026
```

