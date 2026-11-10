---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks"]
file_pages: [4287]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4287 to 4287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4287

```text
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C4 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C5 MessageNameAndReferenceGuideline
If Reference/RelatedReference/MessageName or Reference/OtherReference/MessageName is
present, it must contain 502 or must start with setr.047, setr.049, setr.051, setr.053, setr.055,
setr.058 and Reference/RelatedReference/Reference must contain the message reference of a
message in this list.
This constraint is defined at the MessageDefinition level.
C6 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C7 OtherReferenceGuideline
OtherReference should be used to reference an order confirmation cancellation 'message' sent
in a proprietary way or used for a system reference. If OtherReference is present,
OtherReference/MessageName must contain 'fax' or 'phone' or 'email', etc.
This constraint is defined at the MessageDefinition level.
C8 ReasonElementRule
Either Reason or AdditionalInformation must be present. Both may be present.
C9 SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
64.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
64.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4287 May 2026
```

