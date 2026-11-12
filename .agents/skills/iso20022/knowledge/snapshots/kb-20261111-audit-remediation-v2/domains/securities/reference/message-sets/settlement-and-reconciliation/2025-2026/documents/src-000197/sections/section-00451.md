---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.12 CashParties <CshPties>", "20.4.12.4 CreditorAgent <CdtrAgt>"]
file_pages: [695, 696, 697]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.12.4 CreditorAgent <CdtrAgt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 695 to 697.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 695

```text
Creditor <Cdtr> contains the following elements (see "PartyIdentificationAndAccount223" on
page 1695 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1696
   LEI <LEI> [0..1] IdentifierSet 1696
   AlternateIdentification <AltrnId> [0..1] ± 1696
   CashAccount <CshAcct> [0..1] ± 1696
   ChargesAccount <ChrgsAcct> [0..1] ± 1696
   CommissionAccount <ComssnAcct> [0..1] ± 1697
   TaxAccount <TaxAcct> [0..1] ± 1697
   AdditionalInformation <AddtlInf> [0..1] ± C5 1697
20.4.12.4  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the creditor.
CreditorAgent <CdtrAgt> contains the following elements (see "PartyIdentificationAndAccount224" on
page 1692 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1692
{Or     BICFI <BICFI> [1..1] IdentifierSet C8 1692
Or     NameAndAddress <NmAndAdr> [1..1] ± 1693
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1693
   LEI <LEI> [0..1] IdentifierSet 1693
   AlternateIdentification <AltrnId> [0..1] ± 1693
   CashAccount <CshAcct> [0..1] ± 1694
   ChargesAccount <ChrgsAcct> [0..1] ± 1694
   CommissionAccount <ComssnAcct> [0..1] ± 1694
   TaxAccount <TaxAcct> [0..1] ± 1695
   AdditionalInformation <AddtlInf> [0..1] ± C5 1695
20.4.13 SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Amount effectively settled and which will be credited to/debited from the account owner's
cash account. It may differ from the instructed settlement amount based on market tolerance level.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 695 March 2026
```

## File page 696

```text
SettledAmount <SttldAmt> contains the following elements (see "AmountAndDirection94" on
page 1365 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 1365
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 1366
   BrokerageAmountIndicator <BrkrgAmtInd> [0..1] Indicator 1366
   ResearchFeeIndicator <RsrchFeeInd> [0..1] Indicator 1366
   Amount <Amt> [1..1] Amount C1, C9 1366
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1367
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1367
   ForeignExchangeDetails <FXDtls> [0..1] ± 1367
   ValueDate <ValDt> [0..1] ± 1368
20.4.14 OtherAmounts <OthrAmts>
Presence: [0..1]
Definition: Other amounts than the settlement amount.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 696 March 2026
```

## File page 697

```text
OtherAmounts <OthrAmts> contains the following elements (see "OtherAmounts46" on page 1347 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1348
   ChargesFees <ChrgsFees> [0..1] ± 1349
   CountryNationalFederalTax <CtryNtlFdrlTax> [0..1] ± 1349
   TradeAmount <TradAmt> [0..1] ± 1349
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] ± 1350
   IssueDiscountAllowance <IsseDscntAllwnc> [0..1] ± 1350
   PaymentLevyTax <PmtLevyTax> [0..1] ± 1350
   LocalTax <LclTax> [0..1] ± 1351
   LocalTaxCountrySpecific <LclTaxCtrySpcfc> [0..1] ± 1351
   LocalBrokerCommission <LclBrkrComssn> [0..1] ± 1351
   Margin <Mrgn> [0..1] ± 1352
   Other <Othr> [0..1] ± 1352
   RegulatoryAmount <RgltryAmt> [0..1] ± 1352
   ShippingAmount <ShppgAmt> [0..1] ± 1353
   SpecialConcession <SpclCncssn> [0..1] ± 1353
   StampDuty <StmpDty> [0..1] ± 1353
   StockExchangeTax <StockXchgTax> [0..1] ± 1354
   TransferTax <TrfTax> [0..1] ± 1354
   TransactionTax <TxTax> [0..1] ± 1354
   ValueAddedTax <ValAddedTax> [0..1] ± 1355
   WithholdingTax <WhldgTax> [0..1] ± 1355
   NetGainLoss <NetGnLoss> [0..1] ± 1355
   ConsumptionTax <CsmptnTax> [0..1] ± 1356
   AccruedCapitalisationAmount <AcrdCptlstnAmt> [0..1] ± 1356
   BookValue <BookVal> [0..1] ± 1356
   CollateralMonitorAmount <CollMntrAmt> [0..1] ± 1357
   ResearchFee <RsrchFee> [0..1] ± 1357
   NetworkFee <NtwkFee> [0..1] ± 1357
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 697 March 2026
```

