---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.5 PrimaryIndividualInvestor <PmryIndvInvstr>"]
file_pages: [962, 963]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.5 PrimaryIndividualInvestor <PmryIndvInvstr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 962 to 963.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 962

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
35.4.5 PrimaryIndividualInvestor <PmryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the primary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C43 "SocialSecurityNumberGuideline"
PrimaryIndividualInvestor <PmryIndvInvstr> contains the following elements (see
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
35.4.6 SecondaryIndividualInvestor <ScndryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C43 "SocialSecurityNumberGuideline"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 962 May 2026
```

## File page 963

```text
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
35.4.7 OtherIndividualInvestor <OthrIndvInvstr>
Presence: [0..*]
Definition: Information identifying the other individual investors, for example, name, address, social
security number and date of birth.
Impacted by: C43 "SocialSecurityNumberGuideline"
OtherIndividualInvestor <OthrIndvInvstr> contains the following elements (see "IndividualPerson8"
on page 5079 for details)
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 963 May 2026
```

