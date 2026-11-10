---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "36.4.15.5.1.23 AdditionalInformation <AddtlInf>"]
file_pages: [1168, 1169, 1170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1.23 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1168 to 1170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1168

```text
36.4.15.5.1.23  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the tax efficient product.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
36.4.15.5.2  GeneralInvestment <GnlInvstmt>
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
36.4.15.5.3  Pension <Pnsn>
Presence: [1..1]
Definition: Portfolio is a pension policy, plan or scheme.
Impacted by: C10 "BlockTransferRetirementAgeProtectionRule", C11
"BlockTransferTaxFreeCashProtectionRule", C42 "PensionOrderTypeGuideline", C43
"RetirementAgeRule", C44 "RingFencedDrawdownAssets1Rule", C45
"RingFencedDrawdownAssets2Rule", C50 "TaxFreeCashAmountRule", C51
"TaxFreeCashAndValueRule", C54 "TransferScopeTrancheIdentification1Rule"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1168 May 2026
```

## File page 1169

```text
Pension <Pnsn> contains the following Pension5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  1171
     Identifier <Idr> [1..1] Text 1172
     SubIdentifier <SubIdr> [0..1] Text 1172
     AdditionalInformation <AddtlInf> [0..1] ± 1172
   Type <Tp> [1..1]  1172
{Or     Code <Cd> [1..1] CodeSet 1172
Or}     Proprietary <Prtry> [1..1] ± 1173
   TransferScope <TrfScp> [0..1] ± 1174
   TaxReference <TaxRef> [0..*] ± 1174
   DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1174
   DrawdownStatus <DrwdwnSts> [0..1] ± 1174
   DrawdownType <DrwdwnTp> [0..1] ± 1175
   NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1175
   EstimatedValue <EstmtdVal> [0..1] ± 1175
   BlockTransfer <BlckTrf> [0..1] Indicator 1175
   BlockTransferReference <BlckTrfRef> [0..1] Text 1176
   TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1176
   TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1176
   ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1176
   RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1176
   RetirementAge <RtrmntAge> [0..1] Quantity 1177
   Sharing <Shrg> [0..1] Indicator 1177
   LumpSumType <LumpSumTp> [0..*] ± 1177
   PensionOrder <PnsnOrdr> [0..*] ± 1177
   RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1177
   MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1178
   SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1178
   NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1178
   LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1178
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1169 May 2026
```

## File page 1170

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1178
   BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1179
   NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1179
   AdditionalInformation <AddtlInf> [0..*] ± 1179
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
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1170 May 2026
```

