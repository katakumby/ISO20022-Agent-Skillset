---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["3 reda.046.001.01 SecurityCSDLinkMaintenanceRequestV01", "3.4 Message Building Blocks"]
file_pages: [19]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.046.001.01"]
---

# 3.4 Message Building Blocks

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 19 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
C5 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C6 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C7 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C8 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 65 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 66
   CreationDateTime <CreDtTm> [0..1] DateTime 66
3.4.2 SecurityCSDLinkIdentification <SctyCSDLkId>
Presence: [1..1]
Definition: Provides a unique and unambiguous identification for the Security CSD Link.
Approved by the Securities SEG on 21 November 2024. reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 19 December 2024
```

