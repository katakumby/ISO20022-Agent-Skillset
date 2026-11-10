---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.3 PreviousReference <PrvsRef>"]
file_pages: [1325, 1326, 1327]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.3 PreviousReference <PrvsRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1325 to 1327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1325

```text
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
38.4.3 PreviousReference <PrvsRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
38.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
38.4.5 BusinessFlowDirectionType <BizFlowDrctnTp>
Presence: [0..1]
Definition: Business flow direction (assets to be delivered or received).
Datatype: "BusinessFlowDirectionType1Code" on page 5278
CodeName Name Definition
ADLV AssetstoBeDelivered Assets to be delivered.
ARCV AssetsToBeReceived Assets to be received.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1325 May 2026
```

## File page 1326

```text
38.4.6 PrimaryIndividualInvestor <PmryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the primary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C41 "SocialSecurityNumberGuideline"
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
38.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C41 "SocialSecurityNumberGuideline"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1326 May 2026
```

## File page 1327

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
38.4.8 OtherIndividualInvestor <OthrIndvInvstr>
Presence: [0..*]
Definition: Information identifying the other individual investors, for example, name, address, social
security number and date of birth.
Impacted by: C41 "SocialSecurityNumberGuideline"
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
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1327 May 2026
```

