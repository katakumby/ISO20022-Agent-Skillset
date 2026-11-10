---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05"]
file_pages: [4109, 4110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56 setr.016.001.05 OrderInstructionStatusReportV05

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4109 to 4110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4109

```text
56 setr.016.001.05
OrderInstructionStatusReportV05
56.1 MessageDefinition Functionality
Scope
The OrderInstructionStatusReport message is sent by an executing party, for example, a transfer agent,
to the instructing party, for example, an investment manager or its authorised representative, to report
the status of an order from the time the executing party receives the order until the time the order is
executed.
Usage
The OrderInstructionStatusReport message is used to report on the status of a subscription, redemption
or a switch order.
The OrderInstructionStatusReport message may be used to give the status of:
- one order message by using OrderDetailsReport or,
- one or more individual order instructions by using IndividualOrderDetailsReport, or
- one or more switch orders by using SwitchOrderDetailsReport.
If the OrderInstructionStatusReport message is used to report the status of an individual order, then
IndividualOrderDetailsReport is used and the order reference of the individual order is quoted in
OrderReference. The message identification of the message in which the individual order was
conveyed may also be quoted in RelatedReference but this is not recommended.
If the OrderInstructionStatusReport message is used to report the status of a switch order, then
SwitchOrderDetailsReport is used and the order reference of the switch order is quoted in
OrderReference. The message identification of the message in which the switch order was conveyed
may also be quoted in RelatedReference but this is not recommended.
If the OrderInstructionStatusReport message is used to report the status of an entire order message, for
example, the SubscriptionBulkOrder, or a SubscriptionOrder containing several orders, then
OrderDetailsReport is used and the message identification of the order message is quoted in
RelatedReference. All the orders within the message must have the same status.
One of the following statuses can be reported:
- an accepted status, or,
- an already executed status, or,
- a sent to next party status, or,
- a received status, or,
- a settled status, or,
- a communication problem with next party status, or,
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4109 May 2026
```

## File page 4110

```text
- a confirmation amendment status, or,
- a done for the day status, or,
- a partially done status, or,
- an open status, or,
- a cancelled status, or
- a conditionally accepted status, or,
- a rejected status, or,
- a suspended status, or,
- a partially settled status, or,
- an in-repair status (only for an individual or switch order).
For a switch order, the OrderInstructionStatusReport message provides the status of the whole switch
order, that is, it is not possible to accept one leg and to reject the other leg: the entire switch order has
to be rejected. In order to identify the legs within the switch that are causing the problem, the leg is
identified in either the RedemptionLegIdentification or SubscriptionLegIdentification elements.
When the OrderInstructionStatusReport is used to give the status of an individual or a switch order, the
following can be specified:
- repaired conditions (for a switch, this is at the level of a leg),
- information related to the order, for example, settlement amount, number of units, expected trade
date.
Outline
The OrderInstructionStatusReportV05 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. Reference
Reference to the message or communication that was previously received.
C. StatusReport
Status of the order.
D. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4110 May 2026
```

