---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["2 reda.045.001.01 SecurityCSDLinkCreationRequestV01", "2.4 Message Building Blocks"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01"]
---

# 2.4 Message Building Blocks

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C6 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C7 IssuanceAccountOrBlockChainAddress1Rule
If IssuanceAccount is present, IssuanceBlockChainAddressOrWallet must be absent.
C8 IssuanceAccountOrBlockChainAddress2Rule
If IssuanceBlockChainAddressOrWallet is present, IssuanceAccount must be absent.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C10 SecuritiesAccountOrBlockChainAddress3Rule
Either IssuanceAccount or IssuanceBlockChainAddressOrWallet must be present but not both.
C11 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 65 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 66
   CreationDateTime <CreDtTm> [0..1] DateTime 66
Approved by the Securities SEG on 21 November 2024. reda.045.001.01
SecurityCSDLinkCreationRequestV01
Target2-Securities - Link Reference Data 8 December 2024
```

