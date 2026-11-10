---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Query related messages"]
content_origin: "source-transcription"
---

# Query related messages

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Query related messages.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P113** Query related messages

**P114** Intra-balance Movement Query (camt.078) provides a user, granted with the appropriate rights, with the possibility to query previously sent Intra-balance Movements based on a criteria of business attributes. 

**P115** The user must specify an identification to uniquely and unambiguously identify the message, and the criteria to perform the query. 

**P116** The Intra-balance Movement Query Response (camt.079) provides the corresponding reply based on the business search criteria.

**P117** Intra-balance Movement Modification Query (camt.080) provides a user, granted with the appropriate rights, with the possibility to query either full details or the current status of Intra-balance Modification Instructions based on a set of business attributes. 

**P118** The user has to specify an identification to uniquely and unambiguously identify the message, and the criteria to perform the query. 

**P119** The Intra-balance Movement Modification Report (camt.081) provides the information of those Intra-balance Modification Instructions that fulfilled the criteria specified previously on the Query Message.

**P120** Intra-balance Movement Cancellation Query (camt.082) provides a user, granted with the appropriate rights, with the possibility to query either full details or the current status of Intra-balance Cancellation Instructions based on a set of business attributes. 

**P121** The user has to specify an identification to uniquely and unambiguously identify the message, and the criteria to perform the query. 

**P122** The Intra-balance Movement Cancellation Report (camt.083) provides the information of those Intra-balance Cancellation Instructions that fulfilled the criteria specified previously on the Query Message.

