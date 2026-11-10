---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p118-unsolicited-push-reporting"
title: "Unsolicited operational cash reports and warnings"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.019.001.07", "camt.017.001.05", "camt.021.001.06"]
source_locations: [{"source_id": "src-000014", "paragraphs": ["P75", "P118", "P143", "P276", "P293", "P306"]}]
limitations: ["No separate source drawing depicts this unsolicited path. No request is introduced."]
---

# Unsolicited operational cash reports and warnings

At an agreed time or when a problem/event occurs, the administrator/account servicing institution sends information to the member/account owner without a preceding Get. The member receives the information; general business information may request further action. Details, triggers and warning conditions remain publication-specific.

**P75** These messages may be exchanged at pre-agreed times, upon request of the account owner or at the initiative of the account servicing institution, that is either triggered by a request from the account owner ('pull' mechanism), or initiated by the account servicing institution ('push' mechanism).

**P118** Return messages can however also be sent without a previous Get message. This is called push mode. The push of information can take place either at pre-agreed times or as a warning or alarm when a problem has occurred.

**P143** As explained earlier, Return messages could also be sent spontaneously by the transaction administrator.

**P276** The transaction administrator may also send a ReturnBusinessDayInformation message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs attention.

**P293** The transaction administrator may also send a Return Currency Exchange Rate message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs the member(s) attention.

**P306** The transaction administrator can send general business information messages to the members, which may request further action from them. General business information can contain either, static data announcing foreseen events affecting the system, or dynamic data, warning or notifying about unexpected events.

[src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx)

- [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md)
- [System / Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md)
- [Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md)
- [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md)

- [camt.019.001.07](../../../../messages/camt.019.001.07/index.md)
- [camt.017.001.05](../../../../messages/camt.017.001.05/index.md)
- [camt.021.001.06](../../../../messages/camt.021.001.06/index.md)
