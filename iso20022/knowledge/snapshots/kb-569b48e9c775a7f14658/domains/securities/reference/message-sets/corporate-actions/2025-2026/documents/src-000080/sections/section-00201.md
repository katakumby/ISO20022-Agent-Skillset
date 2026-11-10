---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09", "4.4 Message Building Blocks"]
file_pages: [268]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.032.001.09"]
---

# 4.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 268 to 268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 268

```text
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and
not by the securities holders.
C4 EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event
code is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the
issuer and not by the securities holders.
C5 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C6 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 NotificationIdentification <NtfctnId>
Presence: [0..1]
Definition: Identification of a previously sent notification document.
NotificationIdentification <NtfctnId> contains the following elements (see "DocumentIdentification9"
on page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
4.4.2 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.032.001.09
CorporateActionEventProcessingStatusAdviceV09
Corporate Actions - Maintenance 2025 - 2026 268 February 2026
```

