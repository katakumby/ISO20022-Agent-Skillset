---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.4 CashSettlementDetails <CshSttlmDtls>", "34.4.4.19.4.2 ChequeDetails <ChqDtls>", "34.4.4.19.4.2.4 DrawerIdentification <DrwrId>"]
file_pages: [927, 928]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.4.2.4 DrawerIdentification <DrwrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 927 to 928.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 927

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
34.4.4.19.4.2.4  DrawerIdentification <DrwrId>
Presence: [0..1]
Definition: Account owner that issues the cheque ordering the drawee bank to pay a specific amount,
upon demand, to the payee.
DrawerIdentification <DrwrId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
34.4.4.20  BenefitCrystallisationEvent <BnftCrstllstnEvt>
Presence: [0..*]
Definition: Information about the realisation of benefits taken from a pension.
BenefitCrystallisationEvent <BnftCrstllstnEvt> contains the following elements (see
"BenefitCrystallisationEvent2" on page 4799 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventTypeNumber <EvtTpNb> [0..1] Text 4799
   EventTypeName <EvtTpNm> [0..1] Text 4799
   EventDate <EvtDt> [0..1] Date 4799
   CrystallisationAmount <CrstllstnAmt> [0..1] Amount C1 4800
   PercentageOfAllowance <PctgOfAllwnc> [0..1] Rate 4800
   LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 4800
   AdditionalInformation <AddtlInf> [0..*] ± 4800
34.4.4.21  DrawdownTranche <DrwdwnTrch>
Presence: [0..*]
Definition: Details of a drawdown tranche.
Impacted by: C5 "BeneficiaryDetailsRule"
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 927 May 2026
```

## File page 928

```text
DrawdownTranche <DrwdwnTrch> contains the following Drawdown04 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 929
   TrancheType <TrchTp> [1..1] ± 929
   ApplicableRules <AplblRules> [0..1]  929
{Or     Code <Cd> [1..1] CodeSet 930
Or}     Proprietary <Prtry> [1..1] ± 930
   InvestorTaxReference <InvstrTaxRef> [0..1]  930
     Type <Tp> [0..1]  930
{Or       Code <Cd> [1..1] CodeSet 931
Or}       Proprietary <Prtry> [1..1] ± 931
     Reference <Ref> [1..1] Text 931
   PercentageOfTotalTransferValue <PctgOfTtlTrfVal> [0..1] Rate 931
   TotalAmountNetDrawdown <TtlAmtNetDrwdwn> [0..1] Amount C1 931
   AdditionalFundsDesignated <AddtlFndsDsgntd> [0..1] Indicator 932
   PensionCommencementLumpSumRemaining
<PnsnCmcmntLumpSumRmng>
[0..1] Amount C1 932
   PensionCommencementLumpSumDate
<PnsnCmcmntLumpSumDt>
[0..1] Date 932
   MultiplePensionCommencementLumpSums
<MltplPnsnCmcmntLumpSums>
[0..1] Indicator 932
   LifetimeAllowance <LftmAllwnc> [0..1] Rate 933
   RecipientOfDrawdownIndicator <RcptOfDrwdwnInd> [0..1] Indicator 933
   BeneficiaryDetails <BnfcryDtls> [0..1]  933
     BeneficiaryType <BnfcryTp> [0..1]  933
{Or       Code <Cd> [1..1] CodeSet 933
Or}       Proprietary <Prtry> [1..1] ± 934
     DeathUnderLimit <DthUdrLmt> [0..1] Indicator 934
     DateOfDeath <DtOfDth> [0..1] Date 934
     DateDesignatedToBeneficiary <DtDsgntdToBnfcry> [0..1] Date 934
     AdditionalInformation <AddtlInf> [0..*] ± 934
   CappedLimits <CapdLmts> [0..1]  935
     StartDate <StartDt> [0..1] Date 935
     IncomeLimitCurrentPeriod <IncmLmtCurPrd> [0..1] Amount C1 935
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 928 May 2026
```

