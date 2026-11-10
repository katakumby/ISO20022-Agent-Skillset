---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.4 Message Building Blocks"]
file_pages: [4306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4306 to 4306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4306

```text
C3 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C4 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C5 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C6 OtherReferenceGuideline
RequestDetails/Reference/OtherReference should be used to reference an order instruction or
cancellation 'message' sent in a proprietary way or used for a system reference. If
RequestDetails/Reference/OtherReference is present, RequestDetails/Reference/
OtherReference/MessageName must contain 'fax' or 'phone' or 'email', etc.
This constraint is defined at the MessageDefinition level.
C7 PreviousReferenceGuideline
If RequestDetails/Reference/PreviousReference/MessageName is present, it must contain 502
or must start with setr.047, setr.049, setr.051, setr.053, or setr.055 and RequestDetails/
Reference/PreviousReference/Reference must contain the reference of a message in this list.
This constraint is defined at the MessageDefinition level.
C8 ReferenceElementRule
One of the elements (Reference, RelatedReference, OrderReference) must be present.
C9 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
65.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
65.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4306 May 2026
```

