---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["46 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "46.4 Message Building Blocks"]
file_pages: [2181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.026.001.01"]
---

# 46.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2181 to 2181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2181

```text
46.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
46.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
46.4.2 EligibleCounterpartCSD <ElgblCntrptCSD>
Presence: [1..1]
Definition: Represents a party to be identified as eligible for the instructing party.
EligibleCounterpartCSD <ElgblCntrptCSD> contains the following EligibleCounterpart3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IssuerIdentification <IssrId> [1..1]  2182
{Or     OrganisationIdentification <OrgId> [1..1] ± 2182
Or}     CombinedIdentification <CmbndId> [1..1] ± 2182
   EligibleCounterpartIdentification <ElgblCntrptId> [1..1]  2182
{Or     OrganisationIdentification <OrgId> [1..1] ± 2183
Or}     CombinedIdentification <CmbndId> [1..1] ± 2183
   ValidFrom <VldFr> [1..1] Date 2183
   ValidTo <VldTo> [0..1] Date 2183
   EligibilityType <ElgbltyTp> [1..1] CodeSet 2183
   EligibilityIdentification <ElgbltyId> [1..1]  2184
{Or     Country <Ctry> [1..1] CodeSet C2 2184
Or     FinancialInstrumentIdentification <FinInstrmId> [1..1] IdentifierSet 2184
Or}     IssuerCSDIdentification <IssrCSDId> [1..1]  2185
{Or       OrganisationIdentification <OrgId> [1..1] ± 2185
Or}       CombinedIdentification <CmbndId> [1..1] ± 2185
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.026.001.01
EligibleCounterpartCSDCreationRequestV01
Target2-Securities 2181 August 2026
```

