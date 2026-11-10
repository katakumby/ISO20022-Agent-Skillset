---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.8 OtherIndividualInvestor <OthrIndvInvstr>"]
file_pages: [1130]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.8 OtherIndividualInvestor <OthrIndvInvstr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1130 to 1130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1130

```text
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
36.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C48 "SocialSecurityNumberGuideline"
SecondaryIndividualInvestor <ScndryIndvInvstr> contains the following elements (see
"IndividualPerson8" on page 5079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5079
   GivenName <GvnNm> [1..1] Text 5079
   NamePrefix <NmPrfx> [0..1] CodeSet 5079
   NameSuffix <NmSfx> [0..1] Text 5080
   Gender <Gndr> [0..1] CodeSet 5080
   BirthDate <BirthDt> [0..1] Date 5080
   SocialSecurityNumber <SclSctyNb> [0..1] Text 5080
   IndividualInvestorAddress <IndvInvstrAdr> [1..1] ± 5080
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
36.4.8 OtherIndividualInvestor <OthrIndvInvstr>
Presence: [0..*]
Definition: Information identifying the other individual investors, for example, name, address, social
security number and date of birth.
Impacted by: C48 "SocialSecurityNumberGuideline"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1130 May 2026
```

