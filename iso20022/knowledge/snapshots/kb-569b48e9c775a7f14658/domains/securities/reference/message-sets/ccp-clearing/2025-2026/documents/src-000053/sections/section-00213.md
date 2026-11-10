---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks"]
file_pages: [279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 279 to 279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 279

```text
– Error Text: At least one identification must be present.
C13 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: Max35Text on page 493
9.4.2 BuyInResponseDetails <BuyInRspnDtls>
Presence: [1..1]
Definition: Provides response details such as a request for delay and the number of days associated to
that request.
BuyInResponseDetails <BuyInRspnDtls> contains the following BuyIn3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BuyInNotificationIdentification <BuyInNtfctnId> [1..1] Text 279
   RequestForDelayIndicator <ReqForDelyInd> [1..1] Indicator 279
   NumberOfDays <NbOfDays> [1..1] Quantity 280
   InitialQuantity <InitlQty> [1..1] ± 280
   CoveredQuantity <CvrdQty> [1..1] ± 280
   UncoveredQuantity <UcvrdQty> [1..1] ± 280
9.4.2.1  BuyInNotificationIdentification <BuyInNtfctnId>
Presence: [1..1]
Definition: Indicates the reference of the BuyInNotification message.
Datatype: Max35Text on page 493
9.4.2.2  RequestForDelayIndicator <ReqForDelyInd>
Presence: [1..1]
Definition: Specific continuous net settlement case where the central counterparty can call for buy-in at
a date anterior to "theoretical" buy-in date, the clearing member may request a delay.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 279
```

