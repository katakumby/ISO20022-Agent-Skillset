---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
participant_id: "participant-src-000052-clearing-member-cm"
title: "Clearing Member (CM)"
source_labels: ["Clearing Member (CM)"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Trade Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[3]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Trade Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Netting Process"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[3]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Netting Process"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[3]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[8]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[10]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[12]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Margining Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[13]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Risk Management – Default Fund Contribution Process"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[4]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[7]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[3]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[5]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[7]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "Settlement Management – Buy-In Process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[8]", "paragraph_id": null, "table_id": "T17"}]
flows: ["flow-src-000052-p191-business-process-trade-management", "flow-src-000052-p194-business-process-risk-management-netting-process", "flow-src-000052-p196-business-process-risk-management-margining-process", "flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process", "flow-src-000052-p201-business-process-settlement-management-settlement-netting-process", "flow-src-000052-p204-settlement-management-buy-in-process"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Clearing Member (CM)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Clearing Member (CM)

Business context: CCP Clearing. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 3 | Process the trade information: <br>Technical and business validation of the transaction before further processing.<br>There are two cases:<br>1) The CM receives trades from the CCP and from its Trading Member Firm. If the CM does not pair or match the trade received from the CCP with a trade received from a trading member firm, the CM contacts this trading member firm (out of scope).<br>2) The CM only received trades from the CCP and in this case, the CM can never identify an incorrect trade (since the CM has not received the trade confirmation from the trading firm. No matching can be done). | Clearing Member (CM) | [T12](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0012.md) row 3 |
| Source activity row 4 | Process cancellation: <br>Technical and business validation of the details of the cancellation. | Clearing Member (CM) | [T12](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0012.md) row 4 |
| Source activity row 3 | The CM receives a business session status message (once all End of day milestones from all markets have been received) (out of scope). | Clearing Member (CM) | [T13](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0013.md) row 3 |
| Source activity row 4 | Process Information: <br>The CM is informed of the netting results and it reconciles its netting calculation with the CCP results (based on the netting parameters). | Clearing Member (CM) | [T13](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0013.md) row 4 |
| Source activity row 3 | Process information: <br>The CM reconciles its calculation with the CCP results (if possible, since the calculation comparison may be very difficult). | Clearing Member (CM) | [T14](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0014.md) row 3 |
| Source activity row 8 | Optional: <br>Based on the margin call, the CM may propose to deliver specific collateral. | Clearing Member (CM) | [T14](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0014.md) row 8 |
| Source activity row 10 | If Yes, deliver the securities/cash/other:<br>The CM delivers the securities/cash accepted as new collateral (out of scope). | Clearing Member (CM) | [T14](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0014.md) row 10 |
| Source activity row 12 | Propose new collateral? | Clearing Member (CM) | [T14](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0014.md) row 12 |
| Source activity row 13 | If Yes, then process starts again.<br>If No, then process ends. | Clearing Member (CM) | [T14](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0014.md) row 13 |
| Source activity row 4 | Process information: <br>Internal validation of  the information. | Clearing Member (CM) | [T15](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0015.md) row 4 |
| Source activity row 7 | Process the information:<br>The CMs will send the settlement instructions to their paying agent unless they have signed a power of attorney with the central counterparty.<br>In the latter case, the CCP is responsible for sending the settlement instructions to the CSD on behalf of the CM. | Clearing Member (CM) | [T16](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0016.md) row 7 |
| Source activity row 3 | Process the information:<br>The CM may send a response to the CCP asking for some delay (only valid for continuous netting systems). | Clearing Member (CM) | [T17](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0017.md) row 3 |
| Source activity row 5 | Process the information:<br>Internal validation of the information. | Clearing Member (CM) | [T17](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0017.md) row 5 |
| Source activity row 7 | Process the information:<br>Internal validation of the information. | Clearing Member (CM) | [T17](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0017.md) row 7 |
| Source activity row 8 | Cancel settlement instruction: <br>The clearing member cancels the settlement instruction sent previously to the settlement agent/ CSD (settlement process – out of scope). | Clearing Member (CM) | [T17](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0017.md) row 8 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [BusinessProcess - Trade Management](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Risk Management – Netting Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p194-business-process-risk-management-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Risk Management – Margining Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p196-business-process-risk-management-margining-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Risk Management – Default Fund Contribution Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [BusinessProcess - Settlement Management – Settlement Netting Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settlement Management – Buy-In Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Clearing Member (CM)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000052](../../../evidence/omitted/b45c53bac2be08dee677b607.md).
