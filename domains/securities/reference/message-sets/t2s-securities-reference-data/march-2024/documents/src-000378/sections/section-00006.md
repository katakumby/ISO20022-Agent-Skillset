---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["2 reda.006.001.01 SecurityCreationRequestV01", "2.4 Message Building Blocks"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 2.4 Message Building Blocks

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
C7 DescriptionUsageRule
Description must be used alone as the last resort.
C8 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C9 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C10 MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
C11 NextCallableDateAndCallableIndicatorRule
If CallableIndicator is present, then NextCalldate must be present.
C12 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C13 PutableDateAndPutableIndicatorRule
If PutableIndicator is present, then PutableDate must be present.
C14 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 481 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 481
   CreationDateTime <CreDtTm> [0..1] DateTime 481
2.4.2 Security <Scty>
Presence: [1..1]
Definition: Represents the financial instruments details.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities - Securities Reference Data 10 March 2024
```

