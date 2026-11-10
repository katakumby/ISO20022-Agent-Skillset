---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.5 Portfolio <Prtfl>", "35.4.14.5.3 Pension <Pnsn>", "35.4.14.5.3.2 Type <Tp>", "35.4.14.5.3.2.2 Proprietary <Prtry>"]
file_pages: [983]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.5.3.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 983 to 983.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 983

```text
CodeName Name Definition
OTPM MandatoryOccupationalPension Pension is a mandatory occupational
pension. This is known as an Obligatory
Occupation Pension (OTP) in some
markets.
OCDC OccupationalDefinedContribution Pension plan is an occupational defined
contribution plan.
PPNS PersonalPension Pension is a personal pension plan.
EPKA PersonalPensionAccount Pension is a personal pension account.
This is known as Employee Pension
Kapital (EPK) in some markets.
ITPO PrivateOccupationalPension Pension is a private occupational
pension. This is known as an industrial
and trade supplementary pension (ITP)
in some markets.
REAN RetirementAnnuity Pension plan is a retirement annuity.
SC32 Section32 Pension type covered by section 32.
S32A Section32A Pension type covered by section 32A.
SIPP SelfInvestedPersonalPension Pension is a self-invested personal
pension plan.
SSAS SmallSelfAdministeredScheme Pension is a small self-administered
pension scheme.
NWRP NonWrapperPension Indicates that the party does not operate
the pension wrapper.
35.4.14.5.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of pension policy, plan or scheme expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
35.4.14.5.3.3  TransferScope <TrfScp>
Presence: [0..1]
Definition: Scope of the pension policy, plan or scheme transfer.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 983 May 2026
```

