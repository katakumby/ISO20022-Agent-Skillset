---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.23 AdditionalInformation <AddtlInf>"]
file_pages: [1360, 1361, 1362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.23 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1360 to 1362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1360

```text
38.4.15.4.1.23  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the tax efficient product.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
38.4.15.4.2  GeneralInvestment <GnlInvstmt>
Presence: [1..1]
Definition: Portfolio is a general investment.
GeneralInvestment <GnlInvstmt> contains the following elements (see "GeneralInvestment2" on
page 4509 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] ± 4509
   OwnershipType <OwnrshTp> [0..1] CodeSet 4509
   CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 4511
   EstimatedValue <EstmtdVal> [0..1] ± 4511
   AdditionalInformation <AddtlInf> [0..*] ± 4511
38.4.15.4.3  Pension <Pnsn>
Presence: [1..1]
Definition: Portfolio is a pension policy, plan or scheme.
Impacted by: C9 "BlockTransferRetirementAgeProtectionRule", C10
"BlockTransferTaxFreeCashProtectionRule", C36 "PensionOrderTypeGuideline", C37
"RetirementAgeRule", C38 "RingFencedDrawdownAssets1Rule", C39
"RingFencedDrawdownAssets2Rule", C43 "TaxFreeCashAmountRule", C44
"TaxFreeCashAndValueRule", C47 "TransferScopeTrancheIdentification1Rule"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1360 May 2026
```

## File page 1361

```text
Pension <Pnsn> contains the following Pension5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  1363
     Identifier <Idr> [1..1] Text 1364
     SubIdentifier <SubIdr> [0..1] Text 1364
     AdditionalInformation <AddtlInf> [0..1] ± 1364
   Type <Tp> [1..1]  1364
{Or     Code <Cd> [1..1] CodeSet 1364
Or}     Proprietary <Prtry> [1..1] ± 1365
   TransferScope <TrfScp> [0..1] ± 1366
   TaxReference <TaxRef> [0..*] ± 1366
   DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1366
   DrawdownStatus <DrwdwnSts> [0..1] ± 1366
   DrawdownType <DrwdwnTp> [0..1] ± 1367
   NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1367
   EstimatedValue <EstmtdVal> [0..1] ± 1367
   BlockTransfer <BlckTrf> [0..1] Indicator 1367
   BlockTransferReference <BlckTrfRef> [0..1] Text 1368
   TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1368
   TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1368
   ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1368
   RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1368
   RetirementAge <RtrmntAge> [0..1] Quantity 1369
   Sharing <Shrg> [0..1] Indicator 1369
   LumpSumType <LumpSumTp> [0..*] ± 1369
   PensionOrder <PnsnOrdr> [0..*] ± 1369
   RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1369
   MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1370
   SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1370
   NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1370
   LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1370
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1361 May 2026
```

## File page 1362

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1370
   BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1371
   NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1371
   AdditionalInformation <AddtlInf> [0..*] ± 1371
Constraints
• BlockTransferRetirementAgeProtectionRule
If BlockTransfer is "false" or "0" (No), then RetirementAgeProtection is not allowed.
If BlockTransfer is "true" or "1" (Yes), then RetirementAgeProtection may be present.
On Condition
    /BlockTransfer is equal to value 'false'
 Or    /BlockTransfer is equal to value '0'
Following Must be True
    /RetirementAgeProtection Must be absent
• BlockTransferTaxFreeCashProtectionRule
If BlockTransfer is "false" or "0" (No), then TaxFreeCashProtection is not allowed.
If BlockTransfer is "true" or "1" (Yes), then TaxFreeCashProtection may be present.
On Condition
    /BlockTransfer is equal to value 'false'
 Or    /BlockTransfer is equal to value '0'
Following Must be True
    /TaxFreeCashProtection Must be absent
• PensionOrderTypeGuideline
A pension policy, plan or scheme cannot have both an earmark and a sharing order.
If PensionOrder/Type/Code/SHAR is present, then PensionOrder/Type/Code/EARM is not allowed.
If PensionOrder/Type/Code/EARM is present, then PensionOrder/Type/Code/SHAR is not allowed.
• RetirementAgeRule
If RetirementAgeProtection is "false" or "0" (No), then RetirementAge is not allowed.
If RetirementAgeProtection is "true" or "1" (Yes), then RetirementAge may be present.
On Condition
    /RetirementAgeProtection is equal to value 'false'
 Or    /RetirementAgeProtection is equal to value '0'
Following Must be True
    /RetirementAge Must be absent
• RingFencedDrawdownAssets1Rule
If DrawdownStatus/Code/NONE (None) is present, then RingFencedDrawdownAssets is not allowed.
On Condition
    /DrawdownStatus/Code is equal to value 'None'
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1362 May 2026
```

