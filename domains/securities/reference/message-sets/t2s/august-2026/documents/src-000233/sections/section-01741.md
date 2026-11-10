---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["68 reda.075.001.01 EligibleSecuritiesDeletionRequestV01", "68.4 Message Building Blocks"]
file_pages: [2391, 2392]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.075.001.01"]
---

# 68.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2391 to 2392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2391

```text
C7 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C8 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
68.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
68.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
68.4.2 EligibleSecurity <ElgblScty>
Presence: [1..*]
Definition: Represents securities defined eligible for auto-collateralisation.
EligibleSecurity <ElgblScty> contains the following EligibleSecurity5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..*] ± C4, C5,
C6, C7,
C8
2391
   CollateralisationCurrency <CollstnCcy> [0..1] CodeSet C1 2393
   EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 2393
   PartyIdentification <PtyId> [1..1]  2393
{Or     OrganisationIdentification <OrgId> [1..1] ± 2393
Or}     CombinedIdentification <CmbndId> [1..1] ± 2394
68.4.2.1  SecurityIdentification <SctyId>
Presence: [1..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities 2391 August 2026
```

## File page 2392

```text
Definition: Identification of a security by an ISIN.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C6 "ISINGuideline", C7
"ISINPresenceRule", C8 "OtherIdentificationPresenceRule"
SecurityIdentification <SctyId> contains the following elements (see "SecurityIdentification19" on
page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities 2392 August 2026
```

