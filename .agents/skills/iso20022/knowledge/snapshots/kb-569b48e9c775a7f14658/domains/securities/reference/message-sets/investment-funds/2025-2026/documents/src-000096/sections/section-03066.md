---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.1 MessageDefinition Functionality"]
file_pages: [4283, 4284]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4283 to 4284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4283

```text
64 setr.057.001.03
OrderConfirmationStatusReportV03
64.1 MessageDefinition Functionality
Scope
The OrderConfirmationStatusReport message is sent by an instructing party, for example, an
investment manager or its authorised representative, to the executing party, for example, a transfer
agent, to report the status of an order confirmation or an order confirmation amendment.
Usage
The OrderConfirmationStatusReport message is used to report on the status of one or more individual:
- subscription confirmations,
- subscription confirmation amendments,
- redemption confirmations,
- redemption confirmation amendments,
- switch order confirmations,
- switch order confirmation amendments.
One of the following statuses can be reported:
- confirmation rejected, or,
- amendment rejected, or,
- sent to next party, or,
- communication problem with next party, or,
- confirmation accepted, or,
- confirmation received.
It is likely that the OrderConfirmationStatusReport is only sent by the order instructing party to the order
executing party to reject an order confirmation or to reject an order confirmation amendment, although if
an intermediary party is used, the statuses sent to next party and communication problem with next
party are also likely be used. The statuses confirmation accepted and confirmation received would only
be used in the event the order executing party sends a RequestForOrderConfirmationStatusReport
message and one of the other statuses does not apply.
If the status being reported is either confirmation rejected or amendment rejected, then a reason for the
rejection must be given.
The individual order confirmation or confirmation amendment for which the status is given is identified
with its order reference. The message identification of the message in which the individual order
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4283 May 2026
```

## File page 4284

```text
confirmation or confirmation amendment was conveyed may also be quoted in RelatedReference, but
this is not recommended.
Outline
The OrderConfirmationStatusReportV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. Reference
Reference to the message or communication that was previously received.
C. IndividualOrderConfirmationDetailsReport
Status report details of an individual order confirmation.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4284 May 2026
```

