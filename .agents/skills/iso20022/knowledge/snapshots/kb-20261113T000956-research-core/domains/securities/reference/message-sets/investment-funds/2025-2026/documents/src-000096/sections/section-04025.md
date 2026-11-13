---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.150 OrderQuantityType2Code"]
file_pages: [5333]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.150 OrderQuantityType2Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5333 to 5333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5333

```text
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
the protections afforded by conduct of
business rules defined under MiFID.
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
66.2.2.150  OrderQuantityType2Code
Definition: Specifies how the order is placed, eg by quantity of units or by amount of money.
Type: CodeSet
CodeName Name Definition
UNIT Unit Order is placed by unit.
CASH Amount Order is placed by amount of money.
66.2.2.151  OrderStatus4Code
Definition: Specifies the current status of the order.
Type: CodeSet
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5333 May 2026
```

