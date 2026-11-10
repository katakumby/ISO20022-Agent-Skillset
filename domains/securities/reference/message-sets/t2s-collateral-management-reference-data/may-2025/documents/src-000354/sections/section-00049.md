---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01", "8.4 Message Building Blocks"]
file_pages: [53, 54]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.075.001.01"]
---

# 8.4 Message Building Blocks

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 53 to 54.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
C7 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C8 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 68 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 68
   CreationDateTime <CreDtTm> [0..1] DateTime 68
8.4.2 EligibleSecurity <ElgblScty>
Presence: [1..*]
Definition: Represents securities defined eligible for auto-collateralisation.
EligibleSecurity <ElgblScty> contains the following EligibleSecurity5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..*] ± C4, C5,
C6, C7,
C8
53
   CollateralisationCurrency <CollstnCcy> [0..1] CodeSet C1 55
   EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 55
   PartyIdentification <PtyId> [1..1]  55
{Or     OrganisationIdentification <OrgId> [1..1] ± 55
Or}     CombinedIdentification <CmbndId> [1..1] ± 56
8.4.2.1  SecurityIdentification <SctyId>
Presence: [1..*]
Approved by the Securities SEG on 17 April 2025. reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities - Collateral Management Reference Data 53 May 2025
```

## File page 54

```text
Definition: Identification of a security by an ISIN.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C6 "ISINGuideline", C7
"ISINPresenceRule", C8 "OtherIdentificationPresenceRule"
SecurityIdentification <SctyId> contains the following elements (see "SecurityIdentification19" on
page 63 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 64
   OtherIdentification <OthrId> [0..*]  64
     Identification <Id> [1..1] Text 64
     Suffix <Sfx> [0..1] Text 64
     Type <Tp> [1..1] ± 64
   Description <Desc> [0..1] Text 65
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
Approved by the Securities SEG on 17 April 2025. reda.075.001.01
EligibleSecuritiesDeletionRequestV01
Target2-Securities - Collateral Management Reference Data 54 May 2025
```

