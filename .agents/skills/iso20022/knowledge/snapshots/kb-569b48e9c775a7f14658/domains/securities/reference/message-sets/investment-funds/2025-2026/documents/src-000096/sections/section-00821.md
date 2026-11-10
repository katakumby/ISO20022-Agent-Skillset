---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks"]
file_pages: [1127, 1128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1127 to 1128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1127

```text
If TaxFreeCashProtection is "false" or "0" (Yes), then TaxFreeCashAmount and
ValueOfPensionPolicyOrPlanOrScheme may be present.
C52 TotalAmountYearToDateRule
TotalAmountYearToDate must be equal to the sum of EquityComponent and CashComponent
if present.
C53 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
C54 TransferScopeTrancheIdentification1Rule
If TransferScope/Code/SDDT (DrawdownTranche) is not present, then
DrawdownTrancheIdentification is not allowed.
If TransferScope/Code/SDDT (DrawdownTranche) is present, then
DrawdownTrancheIdentification may be present.
36.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
36.4.1 MessageReference <MsgRef>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageReference <MsgRef> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
36.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1127 May 2026
```

## File page 1128

```text
36.4.3 PreviousReference <PrvsRef>
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
36.4.4 RelatedReference <RltdRef>
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
36.4.5 PrimaryIndividualInvestor <PmryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the primary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C48 "SocialSecurityNumberGuideline"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1128 May 2026
```

