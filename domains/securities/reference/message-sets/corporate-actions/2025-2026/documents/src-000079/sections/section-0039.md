---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Announcement ", "Announcement"]
content_origin: "source-transcription"
---

# Announcement

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Announcement  / Announcement.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P207** Announcement

**P208** This scenario illustrates a classical sequence of corporate action messages for the announcement phase of a corporate action event. However, depending on the type of corporate action event and on its processing evolution during its life cycle, not all messages illustrated here will necessarily be sent.

**P209** The account servicer sends a new CorporateActionNotification to the account owner as a preliminary announcement of a corporate action event concerning a security in which the account owner has holdings on its account. As the event details communicated to the account Servicer are updated or modified, the account servicer may send other replacement CorporateActionNotification messages indicating each time the processing status of the event.

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

**P211** Once the information about the corporate action event is complete and confirmed, the account servicer sends a replacement CorporateActionNotification to the account owner as a confirmed announcement indicating the status is complete and confirmed.

**P212** If appropriate for the corporate action event, the account servicer may send a replacement CorporateActionNotification containing the information on the event stage reached in the corporate action event life cycle.

**P213** For corporate action events having an entitlement date (for example, stock dividend), the account servicer sends on entitlement date an entitlement CorporateActionMovemmentPreliminaryAdvice containing the eligible balance and possibly resulting securities and/or cash movements to the account servicer.

**P214** For corporate action events that have an entitlement date and that do not require an election phase (for example, mandatory events without options), once the entitlement date is reached, the account servicer may send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

**P215** In the case of plain vanilla predictable events such as an interest payment, a preliminary announcement and a confirmed announcement are not always necessary and therefore the related CorporateActionNotification messages may not necessarily be sent by the account servicer. The account servicer might directly send a final entitlement CorporateActionMovementPreliminaryAdvice message to the account owner as a first message concerning this type of corporate action event (see also section 2 about election, entitlement and reminder).

**P216** Should a corporate action event processing not be fully completed by the announced payment date, the account servicer may send a CorporateActionEventProcessingStatusAdvice to the account owner to inform about the processing status and optionally, the reason for this status.

