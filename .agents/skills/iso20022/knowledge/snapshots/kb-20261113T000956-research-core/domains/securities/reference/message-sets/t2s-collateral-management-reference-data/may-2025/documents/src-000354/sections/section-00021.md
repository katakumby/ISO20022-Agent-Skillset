---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "4.4 Message Building Blocks"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 4.4 Message Building Blocks

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 68 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 68
   CreationDateTime <CreDtTm> [0..1] DateTime 68
4.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>
Presence: [1..1]
Definition: Represents a party to be identified as eligible for the instructing party.
EligibleCounterpartCSD <ElgblCntrptCSD> contains the following EligibleCounterpart3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuerIdentification <IssrId> [1..1]  25
{Or     OrganisationIdentification <OrgId> [1..1] ± 25
Or}     CombinedIdentification <CmbndId> [1..1] ± 25
   EligibleCounterpartIdentification <ElgblCntrptId> [1..1]  25
{Or     OrganisationIdentification <OrgId> [1..1] ± 26
Or}     CombinedIdentification <CmbndId> [1..1] ± 26
   ValidFrom <VldFr> [1..1] Date 26
   ValidTo <VldTo> [0..1] Date 26
   EligibilityType <ElgbltyTp> [1..1] CodeSet 26
   EligibilityIdentification <ElgbltyId> [1..1]  27
{Or     Country <Ctry> [1..1] CodeSet C2 27
Or     FinancialInstrumentIdentification <FinInstrmId> [1..1] IdentifierSet 27
Or}     IssuerCSDIdentification <IssrCSDId> [1..1]  28
{Or       OrganisationIdentification <OrgId> [1..1] ± 28
Or}       CombinedIdentification <CmbndId> [1..1] ± 28
Approved by the Securities SEG on 17 April 2025. reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities - Collateral Management Reference Data 24 May 2025
```

