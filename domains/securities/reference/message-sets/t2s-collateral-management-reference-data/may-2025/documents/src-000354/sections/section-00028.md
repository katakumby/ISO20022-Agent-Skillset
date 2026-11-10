---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["5 reda.027.001.01 CloseLinkCreationRequestV01", "5.4 Message Building Blocks"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.027.001.01"]
---

# 5.4 Message Building Blocks

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
C7 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C8 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 68 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 68
   CreationDateTime <CreDtTm> [0..1] DateTime 68
5.4.2 CloseLink <ClsLk>
Presence: [1..1]
Definition: Represents a linkage between issuer/debtor/guarantor and its counterparty.
CloseLink <ClsLk> contains the following CloseLink5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..*] ± C3, C4,
C5, C6,
C7
32
   PartyIdentification <PtyId> [1..1]  33
{Or     OrganisationIdentification <OrgId> [1..1] ± 34
Or}     CombinedIdentification <CmbndId> [1..1] ± 34
   CreditProviderIdentification <CdtPrvdrId> [0..1]  34
{Or     OrganisationIdentification <OrgId> [1..1] ± 35
Or}     CombinedIdentification <CmbndId> [1..1] ± 35
5.4.2.1  SecurityIdentification <SctyId>
Presence: [1..*]
Definition: Identification of a security by an ISIN.
Approved by the Securities SEG on 17 April 2025. reda.027.001.01 CloseLinkCreationRequestV01
Target2-Securities - Collateral Management Reference Data 32 May 2025
```

