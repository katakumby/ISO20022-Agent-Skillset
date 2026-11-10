---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["47 reda.027.001.01 CloseLinkCreationRequestV01", "47.4 Message Building Blocks"]
file_pages: [2189]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.027.001.01"]
---

# 47.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2189 to 2189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2189

```text
C7 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C8 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
47.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
47.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
47.4.2 CloseLink <ClsLk>
Presence: [1..1]
Definition: Represents a linkage between issuer/debtor/guarantor and its counterparty.
CloseLink <ClsLk> contains the following CloseLink5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..*] ± C3, C4,
C5, C6,
C7
2189
   PartyIdentification <PtyId> [1..1]  2190
{Or     OrganisationIdentification <OrgId> [1..1] ± 2191
Or}     CombinedIdentification <CmbndId> [1..1] ± 2191
   CreditProviderIdentification <CdtPrvdrId> [0..1]  2191
{Or     OrganisationIdentification <OrgId> [1..1] ± 2192
Or}     CombinedIdentification <CmbndId> [1..1] ± 2192
47.4.2.1  SecurityIdentification <SctyId>
Presence: [1..*]
Definition: Identification of a security by an ISIN.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.027.001.01 CloseLinkCreationRequestV01
Target2-Securities 2189 August 2026
```

