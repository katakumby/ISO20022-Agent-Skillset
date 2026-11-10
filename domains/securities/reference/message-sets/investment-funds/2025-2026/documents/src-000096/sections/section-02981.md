---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.7 OrderStatus <OrdrSts>", "56.4.3.3.7.2 Cancelled <Canc>"]
file_pages: [4178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.7.2 Cancelled <Canc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4178 to 4178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4178

```text
Datatype: "OrderStatus4Code" on page 5333
CodeName Name Definition
PACK Accepted Order is accepted and is ready for
execution (execution is the moment
when pricing is applied).
COSE AlreadyExecuted Order is already executed and
confirmation has been sent.
STNP SentToNextParty Order has been sent to the next party,
eg, the next intermediary.
RECE Received Order has been received, ie, technical
validation of the message is ok, and the
message is now at the receiving side.
SETT Settled Order is settled. The cash is credited or
debited.
CPNP CommunicationProblemNextParty Communication problems with the next
party.
CNFC ConfirmationAmendment Order confirmation cancellation has
been sent and will be followed by a
confirmation amendment, or a
confirmation amendment has been sent.
DONE DoneForDay Order has been partially filled, and is
done for the day, ie, no further
executions will take place today.
DONF PartiallyDone Order has been partially filled and will
not be filled further.
OPOD Open Order is open.
IACO InvalidAgentConfirmation Order confirmation received from agent
is invalid.
56.4.3.3.7.2  Cancelled <Canc>
Presence: [1..1]
Definition: Status of the switch order is cancelled. This status is used for an order that has been
accepted or that has been entered in an order book but that can not be executed.
Impacted by: C3 "AdditionaInformationRule", C5 "CancelledElementRule"
Cancelled <Canc> contains the following elements (see "CancelledStatusReason16" on page 5200 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1]  5200
{Or     Code <Cd> [1..1] CodeSet 5200
Or     Proprietary <Prtry> [1..1] ± 5201
Or}     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5201
   AdditionalInformation <AddtlInf> [0..1] Text 5201
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4178 May 2026
```

