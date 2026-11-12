---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.1 OrderDetailsReport <OrdrDtlsRpt>", "56.4.3.1.2 OrderStatus <OrdrSts>", "56.4.3.1.2.1 Status <Sts>"]
file_pages: [4129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.1.2.1 Status <Sts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4129 to 4129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4129

```text
OrderStatus <OrdrSts> contains one of the following OrderStatus8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] CodeSet 4129
Or   Cancelled <Canc> [1..1] ± C3, C5 4130
Or   ConditionallyAccepted <CondlyAccptd> [1..1] ± 4130
Or   Rejected <Rjctd> [1..10]  C18 4131
     Reason <Rsn> [0..1]  4131
{Or       Code <Cd> [1..1] CodeSet 4131
Or}       Proprietary <Prtry> [1..1] ± 4134
     AdditionalInformation <AddtlInf> [0..1] Text 4134
Or   Suspended <Sspd> [1..1] ± 4134
Or}   PartiallySettled <PrtlySttld> [1..1] ± 4134
56.4.3.1.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of all the orders in the order message. There is no reason attached.
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
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4129 May 2026
```

