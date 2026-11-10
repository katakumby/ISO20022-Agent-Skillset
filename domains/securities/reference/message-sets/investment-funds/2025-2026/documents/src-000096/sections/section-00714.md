---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.5 Portfolio <Prtfl>", "35.4.14.5.3 Pension <Pnsn>", "35.4.14.5.3.1 Identification <Id>", "35.4.14.5.3.1.3 AdditionalInformation <AddtlInf>"]
file_pages: [982]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.5.3.1.3 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 982 to 982.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 982

```text
35.4.14.5.3.1.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the identification of the pension policy, plan or scheme.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
35.4.14.5.3.2  Type <Tp>
Presence: [0..1]
Definition: Type of pension policy, plan or scheme.
Type <Tp> contains one of the following PensionSchemeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 982
Or}   Proprietary <Prtry> [1..1] ± 983
35.4.14.5.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of pension policy, plan or scheme expressed as a code.
Datatype: "PensionSchemeType3Code" on page 5340
CodeName Name Definition
AAVC AdditionalVoluntaryContribution Pension plan is an additional voluntary
contribution plan.
DBEN DefinedBenefit Pension plan is a defined benefit plan.
EXPP ExecutivePensionPlan Pension plan is an executive pension
plan.
FAVC FreeStandingAdditionalVoluntaryContribution Pension plan is a free standing
additional voluntary contribution plan.
GPPS GroupPersonalPension Pension is a group personal pension.
SIPG GroupSelfInvestedPension Pension plan is a group self-invested
pension plan.
STKG GroupStakeholder Pension plan is a group stakeholder
pension plan.
IPST IndividualPensionWithTaxBenefit Pension is an individual pension savings
plan with a tax benefit. This is known as
an Individual Pension Schema (IPS) in
some markets.
STKI IndividualStakeholder Pension plan is an individual stakeholder
pension.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 982 May 2026
```

