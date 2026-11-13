---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.46 PreferredContactMethod2Code"]
file_pages: [870]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.46 PreferredContactMethod2Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 870 to 870.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 870

```text
CodeName Name Definition
MATD Matched Transaction has been matched with a
corresponding transaction by the
clearing agent.
AUTD Authorised Transaction has been authorised by the
transaction administrator or authorised
party.
INVD Invalid Transaction is invalid.
UMAC Unmatched Clearing agent attempted to match the
transaction with a corresponding
transaction but failed.
STLE SettlementEligible Transaction is eligible for future
settlement.
STLM SettlementMature Transaction is eligible for immediate
settlement.
SSPD Suspended Transaction has been suspended by the
clearing agent.
PCAN PendingCancellation Clearing agent has received a
cancellation request for the transaction,
and needs either a matching request for
cancellation from the counterparty or a
confirmation from an authorised party.
PSTL PendingSettlement Transaction is eligible for settlement, but
is pending.
PFST PendingFailingSettlement Transaction eligible for immediate
settlement, has failed to settle.
SMLR SenderMultilateralLimitRelated Transaction causes the 'Sender
multilateral limit' to be exceeded and
cannot currently be processed.
RMLR ReceiverMultilateralLimitRelated Transaction causes the 'Receiver
multilateral limit' to be exceeded and
cannot currently be processed.
SRBL SenderReceiverBilateralLimitRelated Transaction causes the bilateral limit
fixed between Sender and Receiver to
be exceeded and cannot currently be
processed.
AVLB HeldForServiceAvailability Specifies that the message is queued to
the receiving payment system and is
awaiting processing because the
receiving payment system is not
operational (open) at that point in time.
SRML SenderReceiverMultilateralLimitRelated Transaction causes the multilateral limits
fixed between Sender and Receiver to
be exceeded by the total amount of
submitted payments at the end of the
day and cannot currently be processed.
37.2.2.46  PreferredContactMethod2Code
Definition: Preferred method used to reach the individual contact within an organisation.
Type: CodeSet
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 870 February 2025
```

